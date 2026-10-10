import {
  DEFAULT_SETTINGS,
  STORAGE_KEYS,
  type Mask,
  type MindmapNode,
  type Settings,
  byId,
  cardStateKey,
  escapeAttribute,
  escapeHtml,
  flagMapToList,
  listToFlagMap,
  loadSessionState,
  loadSettings,
  mountAudio,
  normalizeCard,
  normalizeMasks,
  normalizeMathHtml,
  normalizeOcclusionImageHtml,
  queueMathTypeset,
  readFields,
  renderCloze,
  renderInlineCloze,
  renderTags,
  revealAnswer,
  saveSessionState,
  saveSettings,
  setTheme,
  sortMasks,
  splitItems,
  trim,
} from "./shared";

interface ChoiceOption {
  key: string;
  label: string;
}

interface FrontState {
  selectedMap: Record<string, boolean>;
  fillDraft: Record<string, string>;
  visibleMasks: Record<string, boolean>;
  optionOrder: string[];
}

const card = normalizeCard(readFields());
const settings = loadSettings();
const stateKey = cardStateKey(card);
const state: FrontState = {
  selectedMap: listToFlagMap(splitItems(loadSessionState(STORAGE_KEYS.selectedPrefix, stateKey, ""))),
  fillDraft: parseDraft(loadSessionState(STORAGE_KEYS.fillPrefix, stateKey, "{}")),
  visibleMasks: listToFlagMap(splitItems(loadSessionState(STORAGE_KEYS.occlusionPrefix, stateKey, ""))),
  optionOrder: splitItems(loadSessionState(STORAGE_KEYS.orderPrefix, stateKey, "")),
};
let choiceOptionsVisible = settings.choiceDisplay === "immediate" || flagMapToList(state.selectedMap).length > 0;
let choiceRevealTimer: number | undefined;

function parseDraft(raw: string): Record<string, string> {
  try {
    return raw ? (JSON.parse(raw) as Record<string, string>) : {};
  } catch {
    return {};
  }
}

function renderHeader(): void {
  byId("card-id").textContent = `#${card.id}`;
  byId("card-type").textContent = settings.showType ? card.label : "";
  byId("deck-name").textContent = settings.showDeck ? card.deck : "";
  byId("tag-bar").innerHTML = renderTags(card.tags);
}

function renderPrompt(): void {
  const prompt = byId("prompt");
  prompt.innerHTML = card.kind === "fill"
    ? renderCloze(card.question, "front", settings.fillMode, state.fillDraft)
    : normalizeMathHtml(card.question);
}

function persistSelectedMap(): void {
  saveSessionState(STORAGE_KEYS.selectedPrefix, stateKey, flagMapToList(state.selectedMap).join("||"));
}

function countSelected(): number {
  return flagMapToList(state.selectedMap).length;
}

function getChoiceOrder(): ChoiceOption[] {
  const items = card.options.map((label, index) => ({ key: String(index + 1), label }));
  if (!settings.randomOptions) {
    return items;
  }
  if (state.optionOrder.length === items.length) {
    const arranged = state.optionOrder
      .map((key) => items.find((item) => item.key === key))
      .filter((item): item is ChoiceOption => Boolean(item));
    if (arranged.length === items.length) {
      return arranged;
    }
  }
  const shuffled = [...items];
  for (let index = shuffled.length - 1; index > 0; index -= 1) {
    const randomIndex = Math.floor(Math.random() * (index + 1));
    [shuffled[index], shuffled[randomIndex]] = [shuffled[randomIndex], shuffled[index]];
  }
  state.optionOrder = shuffled.map((item) => item.key);
  saveSessionState(STORAGE_KEYS.orderPrefix, stateKey, state.optionOrder.join("||"));
  return shuffled;
}

function bindChoiceButtons(): void {
  document.querySelectorAll<HTMLElement>("[data-option-key]").forEach((button) => {
    button.onclick = () => {
      const key = button.getAttribute("data-option-key") || "";
      if (!key) {
        return;
      }
      if (card.answers.length > 1) {
        state.selectedMap[key] = !state.selectedMap[key];
      } else {
        state.selectedMap = { [key]: true };
      }
      persistSelectedMap();
      renderChoice();
      if (settings.autoFlip && countSelected() === (card.answers.length || 1)) {
        revealAnswer();
      }
    };
  });
}

function clearChoiceRevealTimer(): void {
  if (choiceRevealTimer !== undefined) {
    window.clearTimeout(choiceRevealTimer);
    choiceRevealTimer = undefined;
  }
}

function resetChoiceVisibility(): void {
  clearChoiceRevealTimer();
  choiceOptionsVisible = settings.choiceDisplay === "immediate" || countSelected() > 0;
}

function showChoiceOptions(focusFirst: boolean): void {
  choiceOptionsVisible = true;
  renderChoice();
  queueMathTypeset(["front-interaction"]);
  if (focusFirst) {
    document.querySelector<HTMLElement>("[data-option-key]")?.focus();
  }
}

function renderChoice(): void {
  clearChoiceRevealTimer();
  if (!choiceOptionsVisible && settings.choiceDisplay === "manual") {
    byId("front-interaction").innerHTML = '<div class="choice-gate" role="status" aria-live="polite"><div class="choice-gate-message">请先在心中作答，再手动显示选项。</div></div>';
    byId("front-controls").innerHTML = '<button class="ghost-button" id="choice-reveal" type="button">显示选项</button>';
    byId<HTMLButtonElement>("choice-reveal").onclick = () => showChoiceOptions(true);
    return;
  }
  if (!choiceOptionsVisible && settings.choiceDisplay === "delay" && settings.choiceDelayMs > 0) {
    byId("front-interaction").innerHTML = `<div class="choice-gate" role="status" aria-live="polite"><div class="choice-gate-message">请先在心中作答，选项将在 ${settings.choiceDelayMs} ms 后显示。</div></div>`;
    byId("front-controls").innerHTML = "";
    choiceRevealTimer = window.setTimeout(() => showChoiceOptions(false), settings.choiceDelayMs);
    return;
  }
  choiceOptionsVisible = true;
  const options = getChoiceOrder();
  const html = options
    .map((option, index) => {
      const selectedClass = state.selectedMap[option.key] ? " selected-option" : "";
      return `<button class="option-card${selectedClass}" type="button" data-option-key="${option.key}"><span class="option-index">${String.fromCharCode(65 + index)}</span><span class="option-label">${normalizeMathHtml(option.label)}</span></button>`;
    })
    .join("");
  byId("front-interaction").innerHTML = `<div class="option-list">${html}</div>`;
  byId("front-controls").innerHTML = "";
  bindChoiceButtons();
}

function persistFillDraft(): void {
  const draft: Record<string, string> = {};
  document.querySelectorAll<HTMLInputElement>(".fill-input").forEach((input) => {
    const index = input.getAttribute("data-fill-index") || "";
    if (index) {
      draft[index] = input.value;
    }
  });
  state.fillDraft = draft;
  saveSessionState(STORAGE_KEYS.fillPrefix, stateKey, JSON.stringify(draft));
}

function bindFillInputs(): void {
  document.querySelectorAll<HTMLInputElement>(".fill-input").forEach((input) => {
    input.oninput = () => {
      persistFillDraft();
    };
    input.onkeydown = (event) => {
      if (event.key === "Enter") {
        persistFillDraft();
        if (settings.autoFlip) {
          revealAnswer();
        }
      }
    };
  });
}

function renderFillControls(): void {
  byId("front-interaction").innerHTML = '<div class="info-card">填写答案后，可点击检查或直接翻到背面。</div>';
  byId("front-controls").innerHTML = '<button class="ghost-button" type="button" id="fill-submit">检查填写</button><button class="ghost-button" type="button" id="fill-clear">清空输入</button>';
  byId<HTMLElement>("fill-submit").onclick = () => {
    persistFillDraft();
    if (settings.autoFlip) {
      revealAnswer();
    }
  };
  byId<HTMLElement>("fill-clear").onclick = () => {
    state.fillDraft = {};
    saveSessionState(STORAGE_KEYS.fillPrefix, stateKey, "{}");
    renderPrompt();
    bindFillInputs();
  };
  bindFillInputs();
}

function getOcclusionMasks(): Mask[] {
  return sortMasks(normalizeMasks(card.extra.masks), settings.occlusionOrder);
}

function persistVisibleMasks(masks: Mask[]): void {
  const visible = masks
    .map((mask, index) => String(mask.id || index + 1))
    .filter((id) => state.visibleMasks[id]);
  saveSessionState(STORAGE_KEYS.occlusionPrefix, stateKey, visible.join("||"));
}

function bindOcclusionButtons(masks: Mask[]): void {
  document.querySelectorAll<HTMLElement>("[data-mask-id]").forEach((button) => {
    button.onclick = () => {
      const id = button.getAttribute("data-mask-id") || "";
      if (!id) {
        return;
      }
      state.visibleMasks[id] = !state.visibleMasks[id];
      persistVisibleMasks(masks);
      renderOcclusion();
    };
  });
  byId<HTMLElement>("mask-next").onclick = () => {
    for (let index = 0; index < masks.length; index += 1) {
      const id = String(masks[index].id || index + 1);
      if (!state.visibleMasks[id]) {
        state.visibleMasks[id] = true;
        break;
      }
    }
    persistVisibleMasks(masks);
    renderOcclusion();
  };
  byId<HTMLElement>("mask-toggle").onclick = () => {
    const allShown = masks.every((mask, index) => state.visibleMasks[String(mask.id || index + 1)]);
    state.visibleMasks = {};
    if (!allShown) {
      masks.forEach((mask, index) => {
        state.visibleMasks[String(mask.id || index + 1)] = true;
      });
    }
    persistVisibleMasks(masks);
    renderOcclusion();
  };
}

function renderOcclusion(): void {
  const masks = getOcclusionMasks();
  const occlusionImage = normalizeOcclusionImageHtml(card.occlusionImage);
  if (!trim(occlusionImage) || !masks.length) {
    byId("front-interaction").innerHTML = '<div class="info-card">图片遮挡数据无效，已跳过交互渲染。</div>';
    byId("front-controls").innerHTML = "";
    return;
  }
  const maskHtml = masks
    .map((mask, index) => {
      const id = String(mask.id || index + 1);
      const label = mask.label || `遮挡 ${index + 1}`;
      const revealed = state.visibleMasks[id] ? " is-revealed" : "";
      return `<button class="occlusion-mask${revealed}" type="button" data-mask-id="${escapeAttribute(id)}" aria-label="${escapeAttribute(label)}" style="left:${mask.x}%;top:${mask.y}%;width:${mask.w}%;height:${mask.h}%;"><span>${escapeHtml(mask.label || "")}</span></button>`;
    })
    .join("");
  byId("front-interaction").innerHTML = `<div class="occlusion-shell"><div class="occlusion-canvas">${occlusionImage}${maskHtml}</div></div>`;
  byId("front-controls").innerHTML = '<button class="ghost-button" type="button" id="mask-next">显示下一个挖空</button><button class="ghost-button" type="button" id="mask-toggle">切换全部遮挡</button>';
  bindOcclusionButtons(masks);
}

function renderMindmapNode(node: MindmapNode, depth: number, budget: { count: number }): string {
  if (depth > 32 || budget.count >= 1000) {
    return "";
  }
  budget.count += 1;
  const children = Array.isArray(node.children) ? node.children : [];
  const childHtml = children
    .map((child) => renderMindmapNode(child, depth + 1, budget))
    .filter(Boolean)
    .join("");
  const toggle = childHtml
    ? '<button class="mindmap-toggle" type="button" aria-expanded="true" aria-label="折叠子节点">▾</button>'
    : '<span class="mindmap-toggle" aria-hidden="true">•</span>';
  const childrenMarkup = childHtml ? `<ul class="mindmap-children">${childHtml}</ul>` : "";
  return `<li class="mindmap-node">${toggle}<div class="mindmap-label">${renderInlineCloze(String(node.text || ""), "front")}</div>${childrenMarkup}</li>`;
}

function bindMindmapButtons(): void {
  document.querySelectorAll<HTMLElement>(".mindmap-toggle").forEach((button) => {
    button.onclick = () => {
      const node = button.parentElement;
      if (node) {
        const collapsed = node.classList.toggle("is-collapsed");
        button.setAttribute("aria-expanded", String(!collapsed));
        button.setAttribute("aria-label", collapsed ? "展开子节点" : "折叠子节点");
        button.textContent = collapsed ? "▸" : "▾";
      }
    };
  });
}

function renderMindmap(): void {
  const tree = Array.isArray(card.extra.mindmap) ? (card.extra.mindmap as MindmapNode[]) : [];
  const budget = { count: 0 };
  byId("front-interaction").innerHTML = `<ul class="mindmap-root">${tree.map((node) => renderMindmapNode(node, 0, budget)).join("")}</ul>`;
  byId("front-controls").innerHTML = "";
  bindMindmapButtons();
}

function renderNotes(): void {
  const notes = byId("front-notes");
  if (!settings.showNotesFront || !trim(card.notes)) {
    notes.className = "notes-panel notes-panel-front hidden";
    notes.innerHTML = "";
    return;
  }
  notes.className = "notes-panel notes-panel-front";
  notes.innerHTML = `<div class="notes-title">解析 / 笔记</div><div class="notes-content">${normalizeMathHtml(card.notes)}</div>`;
}

function bindBooleanSetting(
  id: string,
  key: "showType" | "showDeck" | "showNotesFront" | "autoFlip" | "randomOptions" | "choiceStats",
): void {
  const input = byId<HTMLInputElement>(id);
  input.checked = settings[key];
  input.onchange = () => {
    settings[key] = input.checked;
    saveSettings(settings);
    if (key === "randomOptions") {
      state.optionOrder = [];
      saveSessionState(STORAGE_KEYS.orderPrefix, stateKey, "");
    }
    renderAll();
  };
}

function updateChoiceDelaySettingVisibility(): void {
  const row = byId("setting-choice-delay-row");
  const input = byId<HTMLInputElement>("setting-choice-delay-ms");
  const active = settings.choiceDisplay === "delay";
  row.classList.toggle("hidden", !active);
  input.disabled = !active;
}

function bindSelectSetting(id: string, key: "fillMode" | "occlusionOrder" | "theme" | "choiceDisplay"): void {
  const input = byId<HTMLSelectElement>(id);
  input.value = settings[key];
  input.onchange = () => {
    if (key === "fillMode") {
      settings.fillMode = input.value as Settings["fillMode"];
    } else if (key === "occlusionOrder") {
      settings.occlusionOrder = input.value as Settings["occlusionOrder"];
    } else if (key === "choiceDisplay") {
      settings.choiceDisplay = input.value as Settings["choiceDisplay"];
      resetChoiceVisibility();
      updateChoiceDelaySettingVisibility();
    } else {
      settings.theme = input.value as Settings["theme"];
    }
    saveSettings(settings);
    renderAll();
  };
}

function bindChoiceDelaySetting(): void {
  const input = byId<HTMLInputElement>("setting-choice-delay-ms");
  input.value = String(settings.choiceDelayMs);
  input.onchange = () => {
    const parsed = Number(input.value);
    settings.choiceDelayMs = Number.isFinite(parsed)
      ? Math.min(60000, Math.max(0, Math.round(parsed)))
      : DEFAULT_SETTINGS.choiceDelayMs;
    input.value = String(settings.choiceDelayMs);
    saveSettings(settings);
    if (settings.choiceDisplay === "delay") {
      resetChoiceVisibility();
      renderAll();
    }
  };
  updateChoiceDelaySettingVisibility();
}

function bindSettings(): void {
  const trigger = byId<HTMLButtonElement>("settings-trigger");
  const modal = byId("settings-modal");
  const closeButton = byId<HTMLButtonElement>("settings-close");
  const closeSettings = (): void => {
    modal.className = "modal hidden";
    modal.setAttribute("aria-hidden", "true");
    trigger.setAttribute("aria-expanded", "false");
    trigger.focus();
  };
  trigger.onclick = () => {
    modal.className = "modal";
    modal.setAttribute("aria-hidden", "false");
    trigger.setAttribute("aria-expanded", "true");
    closeButton.focus();
  };
  closeButton.onclick = closeSettings;
  modal.onclick = (event) => {
    if (event.target === modal) {
      closeSettings();
    }
  };
  modal.onkeydown = (event) => {
    if (event.key === "Escape") {
      event.preventDefault();
      closeSettings();
      return;
    }
    if (event.key !== "Tab") {
      return;
    }
    const focusable = Array.from(modal.querySelectorAll<HTMLElement>("button, input, select, [tabindex]:not([tabindex='-1'])"));
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (!first || !last) {
      return;
    }
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  };
  bindBooleanSetting("setting-show-type", "showType");
  bindBooleanSetting("setting-show-deck", "showDeck");
  bindBooleanSetting("setting-show-notes-front", "showNotesFront");
  bindBooleanSetting("setting-auto-flip", "autoFlip");
  bindBooleanSetting("setting-random-options", "randomOptions");
  bindBooleanSetting("setting-choice-stats", "choiceStats");
  bindSelectSetting("setting-choice-display", "choiceDisplay");
  bindChoiceDelaySetting();
  bindSelectSetting("setting-fill-mode", "fillMode");
  bindSelectSetting("setting-occlusion-order", "occlusionOrder");
  bindSelectSetting("setting-theme", "theme");
}

function bindSpaceFlip(): void {
  document.addEventListener("keydown", (event) => {
    const target = event.target as HTMLElement | null;
    const tagName = target?.tagName.toLowerCase() || "";
    const ignoresSpace = tagName === "input"
      || tagName === "textarea"
      || tagName === "select"
      || tagName === "button"
      || Boolean(target?.isContentEditable)
      || !byId("settings-modal").classList.contains("hidden");
    if (ignoresSpace || event.key !== " ") {
      return;
    }
    event.preventDefault();
    revealAnswer();
  });
}

function renderInteraction(): void {
  if (card.kind === "choice") {
    renderChoice();
    return;
  }
  if (card.kind === "fill") {
    renderFillControls();
    return;
  }
  if (card.kind === "occlusion") {
    renderOcclusion();
    return;
  }
  if (card.kind === "mindmap") {
    renderMindmap();
    return;
  }
  byId("front-interaction").innerHTML = '<div class="info-card">按空格或显示答案翻到背面。</div>';
  byId("front-controls").innerHTML = "";
}

function renderAll(): void {
  setTheme(settings.theme);
  renderHeader();
  renderPrompt();
  renderInteraction();
  renderNotes();
  mountAudio(byId("audio-panel"), card.audio);
  queueMathTypeset(["prompt", "front-interaction", "front-notes"]);
}

function main(): void {
  bindSettings();
  bindSpaceFlip();
  renderAll();
}

main();
