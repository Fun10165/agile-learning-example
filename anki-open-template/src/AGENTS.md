# SRC KNOWLEDGE BASE

## OVERVIEW

`src/` is the runtime source of truth for the Anki template. `front.ts` and `back.ts` execute immediately after esbuild injects them into the template shell.

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Field/model contract | `shared.ts` | `TemplateFields`, `CardData`, `readFields()`. |
| Card type inference | `shared.ts` | `normalizeType()` aliases and fallback detection. |
| Settings and storage | `shared.ts` | `DEFAULT_SETTINGS`, `STORAGE_KEYS`, storage fallbacks. |
| Cloze parsing/rendering | `shared.ts` | `collectClozeTokens()`, `renderCloze()`. |
| MathJax | `shared.ts` | `normalizeMathHtml()`, `queueMathTypeset()`. |
| Front interaction | `front.ts` | Choice/fill/occlusion/mindmap input state. |
| Back results | `back.ts` | Choice stats, fill comparison, answer reveal. |
| State cleanup | `back.ts` | `clearReviewState(card.id)` in `main()`. |

## RUNTIME INVARIANTS

- `front.ts` and `back.ts` compute `card`, `settings`, and session state at module load, then call `main()` synchronously.
- Hidden template IDs are the field bindings: `raw-id`, `raw-type`, `raw-question`, `raw-options`, `raw-answer`, `raw-notes`, `raw-extra`, `raw-audio`, `raw-occlusion-image`, `raw-tags`, `raw-deck`.
- `TemplateFields.occlusionImage` maps to the Anki field named `occlusion_image`.
- `byId<T>()` throws on missing DOM nodes; templates must provide every referenced element.
- Storage helpers intentionally catch and fall back because some Anki webviews restrict storage.
- Back-side `main()` clears selected options, fill drafts, occlusion visibility, and option order for the current card.

## CARD TYPE RULES

- `choice`, `single`, `multiple`, `选择题` normalize to `choice`.
- `fill`, `cloze`, `填空题` normalize to `fill`.
- `occlusion`, `mixed`, `挖空混合`, `图片遮挡` normalize to `occlusion`.
- `mindmap`, `思维导图` normalize to `mindmap`.
- Empty/unknown type can still infer from `options`, cloze syntax, `extra.masks`, or `extra.mindmap`.
- Cloze syntax is `{{c1::answer::hint}}`; hint is optional, but parsing depends on `::` boundaries.

## INTERACTION STATE

- Choice answers use numeric string keys; multi-answer toggles, single-answer replaces the selection map.
- Random option order is generated on the front side, saved in session storage, and replayed on the back side.
- Fill drafts persist per card until the back side clears review state.
- Occlusion mask IDs are `mask.id` when present, otherwise 1-based index strings.
- `revealAnswer()` tries `pycmd`, `study.drawAnswer`, `showAnswer`, then `anki.sendMessage2` for cross-client support.

## CHANGE RULES

- When adding a setting, update both `Settings` and `DEFAULT_SETTINGS`; wire persistence through existing helpers.
- When adding session state, add a `STORAGE_KEYS` entry and clear it in `clearReviewState()` if it is review-scoped.
- Preserve silent fallback behavior around storage and MathJax unless the UI gains an explicit error surface.
- Use `escapeAttribute()` or equivalent escaping before placing user/card content into HTML attributes.
- After runtime changes, rebuild templates and manually validate affected card types from `TEST_DATA.md`.
