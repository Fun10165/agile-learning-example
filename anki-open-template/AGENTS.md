# PROJECT KNOWLEDGE BASE

**Generated:** 2026-04-20 Asia/Shanghai
**Commit:** e12e28f
**Branch:** master

## OVERVIEW

Anki Open Template is a multi-format Anki card template bundle for choice, QA, fill, image occlusion, mindmap, and audio cards. TypeScript is the source of truth; `front.html` and `back.html` are generated inline templates for Anki import and APKG packaging.

## STRUCTURE

```text
anki-awesome-select/
├── src/                 # runtime source: field parsing, front/back behavior
├── templates/           # static Anki HTML shells with /*__SCRIPT__*/ injection point
├── scripts/             # Node template build + Python APKG generators
├── skills/              # Codex skills: template maintenance vs card authoring
├── styles.css           # Anki stylesheet; not inlined by build_templates.mjs
├── TEST_DATA.md         # manual regression dataset
├── front.html           # generated Anki front template; do not hand-maintain
└── back.html            # generated Anki back template; do not hand-maintain
```

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Runtime field parsing, card normalization, storage, MathJax | `src/shared.ts` | Shared by front/back; most invariants live here. |
| Front-side interaction | `src/front.ts` | Choice selection, fill drafts, occlusion reveal, settings modal. |
| Back-side result rendering | `src/back.ts` | Answer summary, result states, review state cleanup. |
| Static DOM shell or Anki field placeholders | `templates/*.template.html` | Keep `raw-*` IDs and `/*__SCRIPT__*/` exact. |
| Visual styling | `styles.css` | Themes, night-mode selectors, mobile layouts, card type styles. |
| Template build pipeline | `scripts/build_templates.mjs` | Bundles `src/front.ts` and `src/back.ts` into root HTML. |
| Test deck export | `scripts/generate_apkg.py` | Uses genanki and root generated templates. |
| Automata sample deck | `scripts/generate_automata_apkg.py` | Reuses the base model from `generate_apkg.py`. |
| Manual validation cases | `TEST_DATA.md` | No automated test suite exists. |
| Agent-facing workflows | `skills/` | Separate repo maintenance from card authoring. |

## CODE MAP

| Symbol | Type | Location | Role |
|--------|------|----------|------|
| `TemplateFields` | interface | `src/shared.ts` | DOM/Anki field contract read from `#raw-*` elements. |
| `CardData` | interface | `src/shared.ts` | Normalized runtime card model. |
| `Settings` / `DEFAULT_SETTINGS` | interface/const | `src/shared.ts` | Persisted user settings and defaults. |
| `STORAGE_KEYS` | const | `src/shared.ts` | Local/session storage key prefixes. |
| `readFields()` | function | `src/shared.ts` | Reads hidden Anki field-store HTML. |
| `normalizeType()` | function | `src/shared.ts` | Maps aliases and infers card kind. |
| `renderCloze()` | function | `src/shared.ts` | Front/back cloze rendering. |
| `revealAnswer()` | function | `src/shared.ts` | Cross-client Anki answer bridge. |
| `main()` | function | `src/front.ts`, `src/back.ts` | Runs synchronously at module load. |

## CONVENTIONS

- Edit `src/` for runtime logic; edit `templates/` only for static HTML skeletons.
- Regenerate `front.html` and `back.html` with `npm run build`; generated root HTML is not source.
- `styles.css` is Anki stylesheet content and stays separate from generated HTML.
- Required note fields: `id`, `type`, `question`, `options`, `answer`, `notes`, `extra`, `audio`, `occlusion_image`.
- Choice options and multi-answer values use `||`; fill cards use `{{c1::answer::hint}}` in `question` and canonical answers joined with `||`.
- Image occlusion uses field-provided `occlusion_image` HTML so media paths resolve through Anki.
- Settings may persist in `localStorage`; answer/session state is per-card and cleared on the back side.
- TypeScript is strict, no emit, ES2018 target; ESLint rejects explicit `any`, inconsistent type imports, and unused variables except `_` args.

## ANTI-PATTERNS (THIS PROJECT)

- Do not hand-edit large logic in `front.html` or `back.html`; rebuild from `src/` and `templates/`.
- Do not inject raw field HTML into JavaScript strings without escaping.
- Do not assume `localStorage`, `sessionStorage`, or modern browser APIs work in every Anki embedded webview.
- Do not change field names or hidden `raw-*` IDs without updating the model, templates, runtime, and deck generation together.
- Do not let selected options, fill drafts, occlusion visibility, or random order leak across cards.
- Do not expose runtime storage keys, generated HTML internals, or build internals when doing simple card authoring.

## UNIQUE STYLES

- Runtime supports Chinese aliases such as `选择题`, `填空题`, `图片遮挡`, and `思维导图` in `normalizeType()`.
- Math text is normalized from `$...$` / `$$...$$` to MathJax delimiters before typesetting.
- Night mode supports several Anki class spellings: `nightMode`, `night-mode`, and `night_mode`.
- Debug bootstrap and startup probe live in templates and are copied into generated HTML.
- `skills/` is part of the repo contract: one skill for maintaining the template, one for authoring cards without internals.

## COMMANDS

```bash
npm run typecheck
npm run lint
npm run build
./.venv/bin/python scripts/generate_apkg.py
./.venv/bin/python scripts/generate_automata_apkg.py
```

## VALIDATION

- There is no automated test framework or CI workflow; `.github/workflows/` is empty.
- Code validation is `npm run build` (`tsc` → ESLint → template bundling).
- Behavior validation is manual with `TEST_DATA.md` and generated/imported APKG decks.
- For behavior changes, verify at least: single-choice, multi-choice, fill, image occlusion, mindmap, audio, and math on relevant Anki clients.

## NOTES

- `.venv/bin/python` is expected for genanki scripts; Python dependencies are not pinned in repo metadata.
- Root `.apkg` files are generated deck artifacts and ignored by git according to project conventions.
- `screens/`, `media/`, and `images/` are asset/demo areas, not logic boundaries.
