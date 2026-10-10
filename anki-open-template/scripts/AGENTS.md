# SCRIPTS KNOWLEDGE BASE

## OVERVIEW

`scripts/` owns the artifact pipeline: Node builds inline Anki HTML, Python packages generated templates into APKG decks.

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Build root HTML templates | `build_templates.mjs` | esbuild + template placeholder replacement. |
| Generate regression APKG | `generate_apkg.py` | Base model, test notes, media package. |
| Generate automata APKG | `generate_automata_apkg.py` | Reuses base model/note helper. |

## BUILD GRAPH

```text
src/front.ts + templates/front.template.html ─┐
src/back.ts  + templates/back.template.html  ├─ build_templates.mjs ──> front.html / back.html
styles.css + front.html + back.html + media/ ─┴─ generate_apkg.py ─────> anki-open-template-test.apkg
generate_apkg.py model helpers ──────────────── generate_automata_apkg.py -> anki-open-template-automata-theory.apkg
```

## NODE SIDE

- `build_templates.mjs` bundles `src/front.ts` and `src/back.ts` with esbuild.
- Bundle format is `iife`, platform `browser`, target `es2018`, charset `utf8`.
- It replaces the literal string `/*__SCRIPT__*/` in `templates/{front,back}.template.html`.
- Outputs are root `front.html` and `back.html`; these are generated artifacts consumed by Anki and Python packaging.
- Do not rename `src/front.ts`, `src/back.ts`, or template filenames without changing the script.

## PYTHON SIDE

- Run APKG scripts with `uv run scripts/<generator>.py`; dependencies are locked by `pyproject.toml` and `uv.lock`. Existing `.venv/bin/python` entry points remain compatible for established local environments.
- `generate_apkg.py` defines the shared `MODEL_ID = 1607392319` and the 9-field note model.
- Test deck `DECK_ID = 2059400111`; automata deck `DECK_ID = 2059400211`; data-structures decks use `205940031x`; RISC-V deck `DECK_ID = 2059400611` to avoid that range.
- Consumer APKG scripts import shared helpers from `generate_apkg.py` instead of duplicating model or package-writing logic. Ordinary strings are escaped; intentional rich HTML must wrap the final complete field value with `trusted_html(...)`.
- `write_deck()` assigns stable note GUIDs from `(DECK_ID, card id)` and rejects duplicate card IDs within a deck, so repeated imports update existing notes instead of creating duplicates.
- `ensure_test_audio()` creates `media/test.wav` if absent; PNG media still must be present for image cards.

## GOTCHAS

- Build order matters: run `npm run build` before APKG generation so Python reads current `front.html` and `back.html`.
- APKG scripts fail fast when generated `front.html` / `back.html` are older than their TypeScript or template sources; run `npm run build` first.
- Changing the note model field list affects both APKG generators and Anki import compatibility.
- Media references in test notes must match files under `media/` or Anki imports with missing assets.
- `ROOT` is derived from `Path(__file__).resolve().parent.parent`, so scripts tolerate different working directories.
- `build_templates.mjs` trims bundled JS text before injection; do not rely on trailing whitespace.

## COMMANDS

```bash
npm run build
npm test
uv run scripts/generate_apkg.py
uv run scripts/generate_automata_apkg.py
uv run -m unittest discover -s tests -p "test_*.py"
```
