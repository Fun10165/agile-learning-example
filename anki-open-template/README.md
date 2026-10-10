# Anki Open Template

[![CI](https://github.com/Fun10165/anki-open-template/actions/workflows/ci.yml/badge.svg)](https://github.com/Fun10165/anki-open-template/actions/workflows/ci.yml)

`Anki Open Template` is a maintained multi-format Anki card template bundle for choice, QA, fill-in, image occlusion, mindmap, and audio cards.

The repository keeps TypeScript as the source of truth and generates inline `front.html` / `back.html` templates for Anki import and packaging.

## What It Supports

- Single-choice and multi-choice cards
- QA cards with notes / explanation panels
- Cloze-style fill cards with `{{c1::answer::hint}}`
- Image occlusion with per-mask reveal, reveal-next, and reveal-all
- Mindmap cards, including inline cloze inside nodes
- Native Anki audio embedding
- Theme switching, deck / type display, random option order, front-side notes, and choice-only option reveal controls
- MathJax delimiter normalization for `$...$` and `$$...$$`

### Choice option display

The card settings include three mutually exclusive modes that apply only to `choice` cards:

- **Immediate**: render all options normally.
- **Delayed**: keep options out of the DOM, keyboard order, and accessibility tree for a configurable `0`–`60000` ms, then reveal them automatically.
- **Manual**: keep options unavailable until the learner presses **显示选项**; revealing does not select an answer or flip the card.

## Repository Layout

```text
src/
  shared.ts          Shared runtime helpers
  front.ts           Front-side runtime
  back.ts            Back-side runtime
templates/
  front.template.html
  back.template.html
scripts/
  build_templates.mjs
  generate_apkg.py
styles.css
front.html           Generated template output
back.html            Generated template output
TEST_DATA.md         Manual test dataset
skills/
  anki-open-template/
```

## Build Workflow

1. Edit runtime logic in `src/`.
2. Edit HTML skeletons in `templates/`.
3. Run:

```bash
npm run build
```

This performs:

- `tsc -p tsconfig.json`
- `eslint src --ext .ts`
- template bundling through `scripts/build_templates.mjs`

`front.html` and `back.html` are build artifacts generated from `templates/` and `src/`. Always edit those source directories and rebuild; never hand-edit the generated output.

## Export Test Deck

Sync the pinned Python packaging environment with `uv`:

```bash
uv sync --frozen
```

Generate a ready-to-import APKG:

```bash
uv run scripts/generate_apkg.py
```

The generator verifies that `front.html` and `back.html` are newer than their TypeScript and template sources. If they are stale, it stops and asks you to run `npm run build` first.

Existing local `.venv/bin/python scripts/generate_apkg.py` entry points remain compatible for users who already created the repository virtualenv.

Output:

- `anki-open-template-test.apkg`

## Required Note Fields

The generated note model expects these fields:

1. `id`
2. `type`
3. `question`
4. `options`
5. `answer`
6. `notes`
7. `extra`
8. `audio`
9. `occlusion_image`

## Field Semantics

- `type`: `choice`, `qa`, `fill`, `occlusion`, `mindmap`
- `question`: main prompt; Anki editor formatting and intentional HTML are supported. In fill answers, escape answer-internal `::` as `\::` (for example, `{{c1::String\::new()}}`); keep the canonical `answer` value as `String::new()`
- `options`: choice options split by `||` or newlines; individual options may contain intentional HTML such as images
- `answer`: choice indices or plain free-text answer; HTML is not accepted
- `notes`: explanation area with optional Anki editor formatting or intentional HTML
- `extra`: strict JSON object; mask labels and mindmap node text are always rendered as plain text
- `audio`: usually Anki sound markup like `[sound:test.wav]`
- `occlusion_image`: image HTML generated or stored by Anki for occlusion cards

When creating cards manually, type ordinary text in Anki's editor. Use Anki's HTML editor only when you intentionally want markup; literal strings such as `<div>` should remain ordinary editor text. Rich fields are sanitized at runtime with a formatting/media allowlist: text formatting, lists, tables, images, and links are preserved; active forms, scripts, SVG/MathML, event handlers, unsupported attributes, and unsafe URL schemes are removed.

## Python Generator Safety Contract

Python deck scripts must pass exactly nine fields. Ordinary `str` values are always escaped, so literal text such as `<div>`, `std::vector<int>`, and `x < y` remains visible. Intentional HTML in `question`, `options`, `notes`, or `occlusion_image` must wrap the final complete field value with `trusted_html(...)`. This helper is only a Python API for `scripts/*.py`; it is not written into Anki fields. Concatenating a `TrustedHtml` value produces an ordinary `str`, so dynamically assembled HTML must be wrapped after the final concatenation.

Cloze fields use `{{c1::answer::hint}}`. Unescaped `::` separates the answer from its optional hint; escape literal answer-internal separators as `\::`, for example `{{c1::String\::new()}}`, while keeping the canonical `answer` field as `String::new()`.

## `extra` Examples

Image occlusion:

```json
{
  "image": "red.png",
  "masks": [
    { "id": "1", "x": 10, "y": 10, "w": 25, "h": 30, "label": "区域1" },
    { "id": "2", "x": 55, "y": 45, "w": 25, "h": 30, "label": "区域2" }
  ]
}
```

Mindmap:

```json
{
  "mindmap": [
    {
      "text": "前端",
      "children": [
        { "text": "框架：{{c1::React}}" },
        { "text": "样式：CSS" }
      ]
    }
  ]
}
```

## Compatibility Notes

- The runtime is optimized for modern Anki Desktop, AnkiWeb, AnkiDroid, and AnkiMobile.
- Session-only answer state is cleared on the back side to avoid stale fill / mask carryover.
- Image occlusion uses field-provided HTML so image paths resolve the same way Anki expects.

## Automated and Manual Testing

Run the automated regression suites after building generated templates:

```bash
npm run build
npm test
uv run -m unittest discover -s tests -p "test_*.py"
```

GitHub Actions runs this build and test pipeline for every push and pull request using the locked npm and uv dependencies.

Use [TEST_DATA.md](TEST_DATA.md) and the packaged `anki-open-template-test.apkg` for client-level manual checks.

Recommended order:

1. Base flow
2. Math and media
3. Occlusion and mindmap
4. Edge and regression cases

## Skills

This repository ships reusable skills in:

- `skills/anki-open-template/` — maintain template behavior and compatibility.
- `skills/guided-concept-learning/` — explain concepts and audit definitions; it does not create cards.
- `skills/anki-card-authoring/` — the lightweight, direct path for quick card authoring.
- `skills/rigorous-anki-card-authoring/` — design cards section by section, self-audit each section's text card plan, and obtain explicit user approval before any script or APKG work.

Choose `anki-card-authoring` for straightforward card creation. Choose `rigorous-anki-card-authoring` when the material needs an audited, approval-gated design process.

## License

This repository is licensed under [GPL-3.0-only](LICENSE).
