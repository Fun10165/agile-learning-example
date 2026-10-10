from __future__ import annotations

import ast
import html
import json
import re
import runpy
import sqlite3
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

import genanki

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import generate_apkg  # noqa: E402


class FieldContractTests(unittest.TestCase):
    def base_fields(self) -> list[str]:
        return ["ID", "qa", "Question", "", "Answer", "", "", "", ""]

    def test_plain_text_is_escaped_without_html_guessing(self) -> None:
        fields = self.base_fields()
        fields[2] = "What does <div> mean? std::vector<int> & x < y"
        prepared = generate_apkg.prepare_note_fields(fields)
        self.assertEqual(
            prepared[2],
            "What does &lt;div&gt; mean? std::vector&lt;int&gt; &amp; x &lt; y",
        )

    def test_trusted_html_is_explicit_and_field_limited(self) -> None:
        fields = self.base_fields()
        fields[2] = generate_apkg.trusted_html('<code>echo $HOME</code>')
        self.assertEqual(generate_apkg.prepare_note_fields(fields)[2], '<code>echo $HOME</code>')
        fields = self.base_fields()
        fields[4] = generate_apkg.trusted_html("<b>answer</b>")
        with self.assertRaisesRegex(ValueError, "does not accept trusted HTML"):
            generate_apkg.prepare_note_fields(fields)

    def test_exact_field_count_and_nonempty_id_are_required(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly 9"):
            generate_apkg.prepare_note_fields(self.base_fields()[:-1])
        fields = self.base_fields()
        fields[0] = " "
        with self.assertRaisesRegex(ValueError, "must not be empty"):
            generate_apkg.prepare_note_fields(fields)

    def test_extra_json_is_strict_except_for_explicit_negative_fixture(self) -> None:
        fields = self.base_fields()
        fields[6] = '{"masks":[}'
        with self.assertRaisesRegex(ValueError, "valid JSON"):
            generate_apkg.prepare_note_fields(fields)
        fields[6] = generate_apkg.invalid_json_fixture('{"masks":[}')
        self.assertEqual(generate_apkg.prepare_note_fields(fields)[6], '{"masks":[}')


class GeneratedApkgTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temporary_directory = tempfile.TemporaryDirectory()
        output = Path(cls.temporary_directory.name) / "regression.apkg"
        media_files = [
            generate_apkg.ensure_test_audio(),
            generate_apkg.MEDIA_DIR / "red.png",
            generate_apkg.MEDIA_DIR / "fields.png",
            generate_apkg.MEDIA_DIR / "settings.png",
            generate_apkg.MEDIA_DIR / "1-mac-single.png",
            generate_apkg.MEDIA_DIR / "2-windows-single.png",
            generate_apkg.MEDIA_DIR / "3-ubuntu-single.png",
        ]
        generate_apkg.write_deck(
            generate_apkg.DECK_ID,
            "Anki Open Template :: Test",
            output,
            generate_apkg.build_notes,
            media_files,
        )
        cls.notes: dict[str, tuple[str, list[str]]] = {}
        with zipfile.ZipFile(output) as archive:
            cls.media = json.loads(archive.read("media"))
            with tempfile.TemporaryDirectory() as directory:
                archive.extract("collection.anki2", directory)
                database = sqlite3.connect(Path(directory) / "collection.anki2")
                try:
                    rows = database.execute("SELECT guid, flds FROM notes").fetchall()
                finally:
                    database.close()
        cls.row_count = len(rows)
        cls.guids = [guid for guid, _ in rows]
        for guid, packed_fields in rows:
            fields = packed_fields.split("\x1f")
            cls.notes[fields[0]] = (guid, fields)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temporary_directory.cleanup()

    def test_note_and_media_structure(self) -> None:
        self.assertEqual(self.row_count, 22)
        self.assertEqual(len(self.notes), 22)
        self.assertEqual(len(set(self.guids)), 22)
        self.assertTrue(all(len(fields) == 9 for _, fields in self.notes.values()))
        self.assertEqual(
            set(self.media.values()),
            {
                "test.wav",
                "red.png",
                "fields.png",
                "settings.png",
                "1-mac-single.png",
                "2-windows-single.png",
                "3-ubuntu-single.png",
            },
        )

    def test_guids_are_stable(self) -> None:
        for card_id, (guid, _) in self.notes.items():
            self.assertEqual(guid, genanki.guid_for(str(generate_apkg.DECK_ID), card_id))

    def test_rich_and_plain_fields_keep_distinct_storage_contracts(self) -> None:
        self.assertIn('<br><img src="fields.png">', self.notes["Q02"][1][2])
        self.assertIn('<img class="occlusion-image" src="red.png">', self.notes["O01"][1][8])
        self.assertIn("<br><br>", self.notes["C03"][1][2])
        self.assertIn("<code>echo $HOME</code>", self.notes["R08"][1][2])
        self.assertIn("What does &lt;div&gt; mean?", self.notes["R07"][1][2])
        self.assertEqual(self.notes["R07"][1][4], "std::vector&lt;int&gt;")

    def test_media_references_are_packaged(self) -> None:
        packaged = set(self.media.values())
        references: set[str] = set()
        for _, fields in self.notes.values():
            for field in fields:
                references.update(Path(match).name for match in re.findall(r'src=["\']([^"\']+)', field))
                references.update(re.findall(r'\[sound:([^\]]+)\]', field))
        self.assertTrue(references <= packaged, f"Missing packaged media: {sorted(references - packaged)}")

    def test_escaped_extra_decodes_to_valid_json(self) -> None:
        stored_extra = self.notes["R09"][1][6]
        decoded = html.unescape(stored_extra)
        parsed = json.loads(decoded)
        self.assertEqual(
            parsed["mindmap"][0]["text"],
            "<img src=x onerror=document.documentElement.dataset.injected=1>",
        )

    def test_invalid_extra_fixture_remains_available(self) -> None:
        self.assertEqual(self.notes["R03"][1][6], '{"image":"broken.png","masks":[}')


class ImportSafetyTests(unittest.TestCase):
    def test_generator_deck_ids_are_unique(self) -> None:
        ids_by_path: dict[int, Path] = {}
        for path in sorted(SCRIPTS.glob("generate*_apkg.py")):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            assignments = [
                node.value.value
                for node in tree.body
                if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == "DECK_ID" for target in node.targets)
                and isinstance(node.value, ast.Constant)
                and isinstance(node.value.value, int)
            ]
            self.assertEqual(len(assignments), 1, f"{path.name} must define one integer DECK_ID")
            deck_id = assignments[0]
            self.assertNotIn(deck_id, ids_by_path, f"{path.name} reuses DECK_ID from {ids_by_path.get(deck_id)}")
            ids_by_path[deck_id] = path

    def test_all_generator_notes_use_the_nine_field_contract(self) -> None:
        model = generate_apkg.build_model()
        for path in sorted(SCRIPTS.glob("generate*_apkg.py")):
            if path.name == "generate_apkg.py":
                continue
            namespace = runpy.run_path(str(path), run_name=f"contract_{path.stem}")
            build_notes = namespace.get("build_notes")
            self.assertTrue(callable(build_notes), f"{path.name} must expose build_notes")
            notes = list(build_notes(model))
            self.assertGreater(len(notes), 0, f"{path.name} produced no notes")
            self.assertTrue(
                all(len(note.fields) == generate_apkg.NOTE_FIELD_COUNT for note in notes),
                f"{path.name} produced a note with the wrong field count",
            )

    def test_rust_generator_import_has_no_write_side_effect(self) -> None:
        output = ROOT / "anki-Rust-第一章-入门指南.apkg"
        before = output.stat().st_mtime_ns if output.exists() else None
        runpy.run_path(str(SCRIPTS / "generate_rust_ch1_apkg.py"), run_name="generator_import_test")
        after = output.stat().st_mtime_ns if output.exists() else None
        self.assertEqual(after, before)


if __name__ == "__main__":
    unittest.main()
