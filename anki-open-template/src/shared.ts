export interface TemplateFields {
  id: string;
  type: string;
  question: string;
  options: string;
  answer: string;
  notes: string;
  extra: string;
  audio: string;
  occlusionImage: string;
  tags: string;
  deck: string;
}

export interface CardData {
  id: string;
  kind: "choice" | "qa" | "fill" | "occlusion" | "mindmap";
  question: string;
  options: string[];
  answers: string[];
  notes: string;
  extra: Record<string, unknown>;
  audio: string;
  occlusionImage: string;
  tags: string[];
  deck: string;
  label: string;
}

export interface Settings {
  showType: boolean;
  showDeck: boolean;
  showNotesFront: boolean;
  autoFlip: boolean;
  randomOptions: boolean;
  choiceStats: boolean;
  choiceDisplay: "immediate" | "delay" | "manual";
  choiceDelayMs: number;
  fillMode: "line" | "box" | "mask";
  occlusionOrder: "tb-lr" | "lr-tb";
  theme: "warm" | "mint" | "slate";
}

export interface ClozeToken {
  answer: string;
  hint: string;
}

export interface Mask {
  id?: string;
  x?: number;
  y?: number;
  w?: number;
  h?: number;
  label?: string;
}

export interface MindmapNode {
  text?: string;
  children?: MindmapNode[];
}

export const DEFAULT_SETTINGS: Settings = {
  showType: true,
  showDeck: false,
  showNotesFront: true,
  autoFlip: true,
  randomOptions: false,
  choiceStats: true,
  choiceDisplay: "immediate",
  choiceDelayMs: 1500,
  fillMode: "line",
  occlusionOrder: "tb-lr",
  theme: "warm",
};

export const STORAGE_KEYS = {
  settings: "AAS-SETTINGS",
  selectedPrefix: "AAS-SELECTED-",
  fillPrefix: "AAS-FILL-",
  occlusionPrefix: "AAS-OCCLUSION-",
  orderPrefix: "AAS-ORDER-",
};

const OPEN_BRACE = String.fromCharCode(123);
const CLOSE_BRACE = String.fromCharCode(125);
const CLOZE_START = `${OPEN_BRACE}${OPEN_BRACE}c`;
const CLOZE_END = `${CLOSE_BRACE}${CLOSE_BRACE}`;

export function trim(value: unknown): string {
  return String(value ?? "").replace(/^\s+|\s+$/g, "");
}

function getText(id: string): string {
  const element = document.getElementById(id);
  return element ? element.textContent || "" : "";
}

function cloneHtmlWithResolvedImages(element: HTMLElement): string {
  const clone = element.cloneNode(true) as HTMLElement;
  const originalImages = element.querySelectorAll<HTMLImageElement>("img[src]");
  const cloneImages = clone.querySelectorAll<HTMLImageElement>("img[src]");
  for (let index = 0; index < originalImages.length; index += 1) {
    const cloneImage = cloneImages[index];
    const originalImage = originalImages[index];
    if (!cloneImage || !originalImage) {
      continue;
    }
    cloneImage.setAttribute("src", originalImage.src || originalImage.getAttribute("src") || "");
  }
  return clone.innerHTML || "";
}

function getHtml(id: string): string {
  const element = document.getElementById(id);
  return element ? cloneHtmlWithResolvedImages(element as HTMLElement) : "";
}

export function readFields(): TemplateFields {
  return {
    id: trim(getText("raw-id")) || "0",
    type: trim(getText("raw-type")),
    question: getHtml("raw-question"),
    options: getHtml("raw-options"),
    answer: trim(getText("raw-answer")),
    notes: getHtml("raw-notes"),
    extra: trim(getText("raw-extra")),
    audio: trim(getHtml("raw-audio")),
    occlusionImage: getHtml("raw-occlusion-image"),
    tags: trim(getText("raw-tags")),
    deck: trim(getText("raw-deck")),
  };
}

export function parseJSON<T>(value: string, fallback: T): T {
  try {
    return value ? (JSON.parse(value) as T) : fallback;
  } catch {
    return fallback;
  }
}

export function loadSettings(): Settings {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEYS.settings);
    const parsed = parseJSON<Record<string, unknown>>(raw || "", {});
    return {
      showType: typeof parsed.showType === "boolean" ? parsed.showType : DEFAULT_SETTINGS.showType,
      showDeck: typeof parsed.showDeck === "boolean" ? parsed.showDeck : DEFAULT_SETTINGS.showDeck,
      showNotesFront: typeof parsed.showNotesFront === "boolean" ? parsed.showNotesFront : DEFAULT_SETTINGS.showNotesFront,
      autoFlip: typeof parsed.autoFlip === "boolean" ? parsed.autoFlip : DEFAULT_SETTINGS.autoFlip,
      randomOptions: typeof parsed.randomOptions === "boolean" ? parsed.randomOptions : DEFAULT_SETTINGS.randomOptions,
      choiceStats: typeof parsed.choiceStats === "boolean" ? parsed.choiceStats : DEFAULT_SETTINGS.choiceStats,
      choiceDisplay: parsed.choiceDisplay === "delay" || parsed.choiceDisplay === "manual" || parsed.choiceDisplay === "immediate"
        ? parsed.choiceDisplay
        : DEFAULT_SETTINGS.choiceDisplay,
      choiceDelayMs: typeof parsed.choiceDelayMs === "number" && Number.isFinite(parsed.choiceDelayMs)
        ? Math.min(60000, Math.max(0, Math.round(parsed.choiceDelayMs)))
        : DEFAULT_SETTINGS.choiceDelayMs,
      fillMode: parsed.fillMode === "box" || parsed.fillMode === "mask" || parsed.fillMode === "line"
        ? parsed.fillMode
        : DEFAULT_SETTINGS.fillMode,
      occlusionOrder: parsed.occlusionOrder === "lr-tb" || parsed.occlusionOrder === "tb-lr"
        ? parsed.occlusionOrder
        : DEFAULT_SETTINGS.occlusionOrder,
      theme: parsed.theme === "mint" || parsed.theme === "slate" || parsed.theme === "warm"
        ? parsed.theme
        : DEFAULT_SETTINGS.theme,
    };
  } catch {
    return { ...DEFAULT_SETTINGS };
  }
}

export function saveSettings(settings: Settings): void {
  try {
    window.localStorage.setItem(STORAGE_KEYS.settings, JSON.stringify(settings));
  } catch {
    // Ignore storage failures in restrictive environments.
  }
}

export function cardStateKey(card: Pick<CardData, "deck" | "id">): string {
  return `${encodeURIComponent(card.deck || "_")}::${encodeURIComponent(card.id)}`;
}

export function loadSessionState(prefix: string, stateKey: string, fallback: string): string {
  try {
    const value = window.sessionStorage.getItem(prefix + stateKey);
    return value == null ? fallback : value;
  } catch {
    return fallback;
  }
}

export function saveSessionState(prefix: string, stateKey: string, value: string): void {
  try {
    window.sessionStorage.setItem(prefix + stateKey, value);
  } catch {
    // Ignore storage failures in restrictive environments.
  }
}

export function clearSessionState(prefix: string, stateKey: string): void {
  try {
    window.sessionStorage.removeItem(prefix + stateKey);
  } catch {
    // Ignore storage failures in restrictive environments.
  }
}

export function clearReviewState(stateKey: string): void {
  clearSessionState(STORAGE_KEYS.selectedPrefix, stateKey);
  clearSessionState(STORAGE_KEYS.fillPrefix, stateKey);
  clearSessionState(STORAGE_KEYS.occlusionPrefix, stateKey);
  clearSessionState(STORAGE_KEYS.orderPrefix, stateKey);
}

export function splitItems(value: string): string[] {
  const normalized = trim(value);
  if (!normalized) {
    return [];
  }
  if (normalized.indexOf("||") > -1) {
    return normalized.split("||").map((item) => trim(item)).filter(Boolean);
  }
  return normalized.split("\n").map((item) => trim(item)).filter(Boolean);
}

export function normalizeType(rawType: string, fields: TemplateFields, extra: Record<string, unknown>): CardData["kind"] {
  const value = trim(rawType).toLowerCase();
  if (value === "choice" || value === "single" || value === "multiple" || value === "选择题") {
    return "choice";
  }
  if (value === "fill" || value === "cloze" || value === "填空题") {
    return "fill";
  }
  if (value === "occlusion" || value === "mixed" || value === "挖空混合" || value === "图片遮挡") {
    return "occlusion";
  }
  if (value === "mindmap" || value === "思维导图") {
    return "mindmap";
  }
  if (trim(fields.options)) {
    return "choice";
  }
  if (fields.question.indexOf(CLOZE_START) > -1) {
    return "fill";
  }
  if (typeof extra.image === "string" && Array.isArray(extra.masks)) {
    return "occlusion";
  }
  if (Array.isArray(extra.mindmap)) {
    return "mindmap";
  }
  return "qa";
}

export function typeLabel(kind: CardData["kind"], answers: string[]): string {
  if (kind === "choice") {
    return answers.length > 1 ? "多选题" : "单选题";
  }
  if (kind === "fill") {
    return "填空题";
  }
  if (kind === "occlusion") {
    return "图片遮挡";
  }
  if (kind === "mindmap") {
    return "思维导图";
  }
  return "问答题";
}

export function normalizeCard(fields: TemplateFields): CardData {
  const extra = parseJSON<Record<string, unknown>>(fields.extra, {});
  const answers = splitItems(fields.answer);
  const kind = normalizeType(fields.type, fields, extra);
  return {
    id: fields.id,
    kind,
    question: fields.question,
    options: splitItems(fields.options),
    answers,
    notes: fields.notes,
    extra,
    audio: fields.audio,
    occlusionImage: fields.occlusionImage,
    tags: fields.tags ? fields.tags.split(" ").map((item) => trim(item)).filter(Boolean) : [],
    deck: fields.deck,
    label: typeLabel(kind, answers),
  };
}

export function setTheme(theme: Settings["theme"]): void {
  document.documentElement.setAttribute("data-theme", theme);
}

export function byId<T extends HTMLElement>(id: string): T {
  const element = document.getElementById(id);
  if (!element) {
    throw new Error(`Missing element: ${id}`);
  }
  return element as T;
}

export function listToFlagMap(items: string[]): Record<string, boolean> {
  const flags: Record<string, boolean> = {};
  items.forEach((item) => {
    if (item) {
      flags[item] = true;
    }
  });
  return flags;
}

export function flagMapToList(flags: Record<string, boolean>): string[] {
  return Object.keys(flags)
    .filter((key) => flags[key])
    .sort();
}

export function escapeHtml(value: unknown): string {
  return String(value ?? "")
    .split("&").join("&amp;")
    .split("<").join("&lt;")
    .split(">").join("&gt;");
}

export function escapeAttribute(value: string): string {
  return escapeHtml(value).split('"').join("&quot;");
}

export function htmlToText(html: string): string {
  const wrapper = document.createElement("div");
  wrapper.innerHTML = sanitizeRichHtml(html);
  return wrapper.textContent || "";
}

function sanitizeRichHtml(html: string): string {
  const wrapper = document.createElement("div");
  wrapper.innerHTML = String(html || "");
  const allowedTags: Record<string, true> = {
    A: true,
    B: true,
    BLOCKQUOTE: true,
    BR: true,
    CODE: true,
    DIV: true,
    EM: true,
    HR: true,
    I: true,
    IMG: true,
    LI: true,
    OL: true,
    P: true,
    PRE: true,
    RP: true,
    RT: true,
    RUBY: true,
    SPAN: true,
    STRONG: true,
    SUB: true,
    SUP: true,
    TABLE: true,
    TBODY: true,
    TD: true,
    TFOOT: true,
    TH: true,
    THEAD: true,
    TR: true,
    UL: true,
  };
  const droppedTags: Record<string, true> = {
    BASE: true,
    BUTTON: true,
    EMBED: true,
    FORM: true,
    IFRAME: true,
    INPUT: true,
    LINK: true,
    MATH: true,
    META: true,
    OBJECT: true,
    OPTION: true,
    SCRIPT: true,
    SELECT: true,
    STYLE: true,
    SVG: true,
    TEXTAREA: true,
  };
  const commonAttributes: Record<string, true> = {
    "aria-hidden": true,
    "aria-label": true,
    class: true,
    role: true,
    title: true,
  };
  const attributesByTag: Record<string, Record<string, true>> = {
    A: { href: true, rel: true, target: true },
    IMG: { alt: true, height: true, loading: true, src: true, width: true },
    TD: { colspan: true, rowspan: true },
    TH: { colspan: true, rowspan: true, scope: true },
  };
  const hasSafeUrl = (value: string, image: boolean): boolean => {
    const normalized = value.replace(/[\u0000-\u0020]+/g, "").toLowerCase();
    const scheme = normalized.match(/^([a-z][a-z0-9+.-]*):/);
    if (!scheme) {
      return true;
    }
    if (image && normalized.startsWith("data:image/")) {
      return /^data:image\/(?:gif|jpeg|png|webp);base64,/.test(normalized);
    }
    const allowedSchemes: Record<string, true> = image
      ? { anki: true, blob: true, file: true, http: true, https: true }
      : { http: true, https: true, mailto: true };
    return Boolean(allowedSchemes[scheme[1]]);
  };
  const sanitize = (element: Element): void => {
    Array.from(element.children).forEach((child) => {
      if (droppedTags[child.tagName]) {
        child.remove();
        return;
      }
      if (!allowedTags[child.tagName]) {
        sanitize(child);
        child.replaceWith(...Array.from(child.childNodes));
        return;
      }
      const tagAttributes = attributesByTag[child.tagName] || {};
      Array.from(child.attributes).forEach((attribute) => {
        const name = attribute.name.toLowerCase();
        if (!commonAttributes[name] && !tagAttributes[name]) {
          child.removeAttribute(attribute.name);
          return;
        }
        if ((name === "src" || name === "href") && !hasSafeUrl(attribute.value, child.tagName === "IMG")) {
          child.removeAttribute(attribute.name);
        }
      });
      if (child.tagName === "A" && child.getAttribute("target") === "_blank") {
        child.setAttribute("rel", "noopener noreferrer");
      }
      sanitize(child);
    });
  };
  sanitize(wrapper);
  return wrapper.innerHTML;
}

export function normalizeOcclusionImageHtml(html: string): string {
  const wrapper = document.createElement("div");
  wrapper.innerHTML = sanitizeRichHtml(html);
  wrapper.querySelectorAll("img").forEach((image) => image.classList.add("occlusion-image"));
  return wrapper.innerHTML;
}

export function convertMathDelimiters(text: string): string {
  let result = "";
  let index = 0;
  let inInline = false;
  let inBlock = false;
  while (index < text.length) {
    const current = text.charAt(index);
    const next = text.charAt(index + 1);
    if (current === "\\") {
      if (next === "$") {
        result += "$";
        index += 2;
        continue;
      }
      result += current;
      index += 1;
      continue;
    }
    if (current === "$" && next === "$" && !inInline) {
      result += inBlock ? "\\]" : "\\[";
      inBlock = !inBlock;
      index += 2;
      continue;
    }
    if (current === "$" && !inBlock) {
      result += inInline ? "\\)" : "\\(";
      inInline = !inInline;
      index += 1;
      continue;
    }
    result += current;
    index += 1;
  }
  return result;
}

function normalizeMathInSafeHtml(html: string): string {
  if (!trim(html)) {
    return html;
  }
  const wrapper = document.createElement("div");
  wrapper.innerHTML = html;
  const skippedTags: Record<string, true> = { CODE: true, PRE: true, MATH: true };
  const walk = (node: Node): void => {
    let child = node.firstChild;
    while (child) {
      const next = child.nextSibling;
      if (child.nodeType === Node.TEXT_NODE) {
        child.nodeValue = convertMathDelimiters(child.nodeValue || "");
      } else if (child.nodeType === Node.ELEMENT_NODE) {
        const element = child as Element;
        if (!skippedTags[element.tagName] && !element.classList.contains("MathJax") && !element.closest("mjx-container")) {
          walk(child);
        }
      }
      child = next;
    }
  };
  walk(wrapper);
  return wrapper.innerHTML;
}

export function normalizeMathHtml(html: string): string {
  return normalizeMathInSafeHtml(sanitizeRichHtml(html));
}

export function queueMathTypeset(ids: string[]): void {
  const globalMathJax = window as Window & {
    MathJax?: {
      startup?: { promise: Promise<unknown> };
      typesetClear?: () => void;
      typesetPromise?: (nodes: HTMLElement[]) => Promise<unknown>;
    };
  };
  try {
    const api = globalMathJax.MathJax;
    if (!api || !api.startup || !api.typesetPromise) {
      return;
    }
    const nodes = ids
      .map((id) => document.getElementById(id))
      .filter((node): node is HTMLElement => Boolean(node));
    if (!nodes.length) {
      return;
    }
    api.startup.promise
      .then(() => {
        if (api.typesetClear) {
          api.typesetClear();
        }
        return api.typesetPromise ? api.typesetPromise(nodes) : Promise.resolve();
      })
      .catch(() => {
        // Ignore MathJax failures and leave raw text visible.
      });
  } catch {
    // Ignore MathJax failures and leave raw text visible.
  }
}

function parseClozeContent(content: string): ClozeToken {
  let separator = -1;
  for (let index = 0; index < content.length - 1; index += 1) {
    if (content[index] !== ":" || content[index + 1] !== ":") {
      continue;
    }
    let precedingBackslashes = 0;
    for (let slash = index - 1; slash >= 0 && content[slash] === "\\"; slash -= 1) {
      precedingBackslashes += 1;
    }
    if (precedingBackslashes % 2 === 0) {
      separator = index;
      break;
    }
  }
  const decode = (value: string): string => htmlToText(value.replace(/\\::/g, "::"));
  return {
    answer: decode(separator === -1 ? content : content.substring(0, separator)),
    hint: decode(separator === -1 ? "" : content.substring(separator + 2)),
  };
}

export function collectClozeTokens(question: string): ClozeToken[] {
  const tokens: ClozeToken[] = [];
  let cursor = 0;
  while (cursor < question.length) {
    const start = question.indexOf(CLOZE_START, cursor);
    if (start === -1) {
      break;
    }
    const firstSep = question.indexOf("::", start);
    const end = question.indexOf(CLOZE_END, firstSep + 2);
    if (firstSep === -1 || end === -1) {
      break;
    }
    const content = question.substring(firstSep + 2, end);
    tokens.push(parseClozeContent(content));
    cursor = end + 2;
  }
  return tokens;
}

export function renderCloze(
  question: string,
  mode: "front" | "back",
  fillMode?: Settings["fillMode"],
  draft?: Record<string, string>,
): string {
  question = sanitizeRichHtml(question);
  let html = "";
  let cursor = 0;
  let order = 0;
  while (cursor < question.length) {
    const start = question.indexOf(CLOZE_START, cursor);
    if (start === -1) {
      html += question.substring(cursor);
      break;
    }
    const firstSep = question.indexOf("::", start);
    const end = question.indexOf(CLOZE_END, firstSep + 2);
    if (firstSep === -1 || end === -1) {
      html += question.substring(cursor);
      break;
    }
    html += question.substring(cursor, start);
    const content = question.substring(firstSep + 2, end);
    const { answer, hint } = parseClozeContent(content);
    order += 1;
    if (mode === "back") {
      html += `<span class="inline-answer">${escapeHtml(answer)}</span>`;
    } else if (fillMode) {
      const value = draft?.[String(order)] || "";
      const placeholder = hint || "请输入";
      html += `<span class="fill-slot fill-slot-${fillMode}"><input class="fill-input" data-fill-index="${order}" value="${escapeAttribute(value)}" placeholder="${escapeAttribute(placeholder)}"></span>`;
    } else {
      html += `<span class="inline-blank">${escapeHtml(hint || "请作答")}</span>`;
    }
    cursor = end + 2;
  }
  return normalizeMathInSafeHtml(html);
}

export function renderInlineCloze(question: string, mode: "front" | "back"): string {
  return renderCloze(escapeHtml(question), mode);
}

export function revealAnswer(): void {
  const globalWindow = window as Window & {
    pycmd?: (message: string) => void;
    study?: { drawAnswer: () => void };
    showAnswer?: () => void;
    anki?: unknown;
    sendMessage2?: (channel: string, message: string) => void;
  };
  if (typeof globalWindow.pycmd === "function") {
    globalWindow.pycmd("ans");
    return;
  }
  if (globalWindow.study && typeof globalWindow.study.drawAnswer === "function") {
    globalWindow.study.drawAnswer();
    return;
  }
  if (typeof globalWindow.showAnswer === "function") {
    globalWindow.showAnswer();
    return;
  }
  if (globalWindow.anki && typeof globalWindow.sendMessage2 === "function") {
    globalWindow.sendMessage2("ankitap", "midCenter");
  }
}

export function mountAudio(container: HTMLElement, audioField: string): void {
  if (!trim(audioField)) {
    container.innerHTML = "";
    return;
  }
  container.innerHTML = `<div class="audio-player audio-player-native"><div class="audio-native-label">音频</div><div class="audio-native-body">${audioField}</div></div>`;
}

export function renderTags(tags: string[]): string {
  return tags.map((tag) => `<span class="tag-chip">${escapeHtml(tag)}</span>`).join("");
}

export function normalizeMasks(value: unknown): Mask[] {
  if (!Array.isArray(value)) {
    return [];
  }
  const seenIds = new Set<string>();
  const masks: Mask[] = [];
  value.forEach((candidate, index) => {
    if (!candidate || typeof candidate !== "object") {
      return;
    }
    const x = Number("x" in candidate ? candidate.x : Number.NaN);
    const y = Number("y" in candidate ? candidate.y : Number.NaN);
    const w = Number("w" in candidate ? candidate.w : Number.NaN);
    const h = Number("h" in candidate ? candidate.h : Number.NaN);
    if (![x, y, w, h].every(Number.isFinite) || w <= 0 || h <= 0) {
      return;
    }
    let id = trim("id" in candidate ? candidate.id : "") || String(index + 1);
    if (seenIds.has(id)) {
      id = `${id}-${index + 1}`;
    }
    seenIds.add(id);
    const left = Math.max(0, Math.min(100, x));
    const top = Math.max(0, Math.min(100, y));
    masks.push({
      id,
      x: left,
      y: top,
      w: Math.max(0.1, Math.min(100 - left, w)),
      h: Math.max(0.1, Math.min(100 - top, h)),
      label: "label" in candidate && typeof candidate.label === "string" ? candidate.label : "",
    });
  });
  return masks;
}

export function sortMasks(masks: Mask[], order: Settings["occlusionOrder"]): Mask[] {
  return [...masks].sort((left, right) => {
    if (order === "lr-tb") {
      return Number(left.x || 0) - Number(right.x || 0) || Number(left.y || 0) - Number(right.y || 0);
    }
    return Number(left.y || 0) - Number(right.y || 0) || Number(left.x || 0) - Number(right.x || 0);
  });
}
