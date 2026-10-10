// @vitest-environment node

import fs from "node:fs";
import path from "node:path";
import { JSDOM } from "jsdom";
import { afterEach, describe, expect, it, vi } from "vitest";

interface TemplateFieldValues {
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

const EMPTY_FIELDS: TemplateFieldValues = {
  id: "TEST",
  type: "qa",
  question: "Question",
  options: "",
  answer: "Answer",
  notes: "",
  extra: "",
  audio: "",
  occlusionImage: "",
  tags: "test",
  deck: "Tests",
};

function renderTemplate(
  side: "front" | "back",
  overrides: Partial<TemplateFieldValues>,
  storedSettings?: Record<string, unknown>,
): JSDOM {
  const fields = { ...EMPTY_FIELDS, ...overrides };
  let template = fs.readFileSync(path.join(process.cwd(), `${side}.html`), "utf8");
  const replacements: Record<string, string> = {
    "{{id}}": fields.id,
    "{{type}}": fields.type,
    "{{question}}": fields.question,
    "{{options}}": fields.options,
    "{{answer}}": fields.answer,
    "{{notes}}": fields.notes,
    "{{extra}}": fields.extra,
    "{{audio}}": fields.audio,
    "{{occlusion_image}}": fields.occlusionImage,
    "{{Tags}}": fields.tags,
    "{{Deck}}": fields.deck,
  };
  Object.entries(replacements).forEach(([placeholder, value]) => {
    template = template.split(placeholder).join(value);
  });
  return new JSDOM(`<!doctype html><html><body class="card">${template}</body></html>`, {
    runScripts: "dangerously",
    url: "https://anki-template.test/",
    beforeParse(window) {
      if (storedSettings) {
        window.localStorage.setItem("AAS-SETTINGS", JSON.stringify(storedSettings));
      }
    },
  });
}

const CHOICE_FIELDS: Partial<TemplateFieldValues> = {
  id: "CHOICE-DISPLAY",
  type: "choice",
  question: "Question",
  options: "One||Two||Three||Four",
  answer: "2",
};

afterEach(() => {
  vi.useRealTimers();
});

describe("generated template field contract", () => {
  it("preserves literal angle brackets in the prompt and QA answer", () => {
    const dom = renderTemplate("back", {
      id: "R07",
      question: "What does &lt;div&gt; mean? C++ 类型 std::vector&lt;int&gt;。",
      answer: "std::vector&lt;int&gt;",
    });
    const document = dom.window.document;
    expect(document.getElementById("prompt")?.textContent).toContain("<div>");
    expect(document.getElementById("prompt")?.textContent).toContain("std::vector<int>");
    expect(document.getElementById("back-interaction")?.textContent).toContain("std::vector<int>");
    expect(document.querySelector("#back-interaction int")).toBeNull();
  });

  it("keeps dollars literal inside code elements", () => {
    const dom = renderTemplate("front", {
      id: "R08",
      question: "Shell 示例：<code>echo $HOME</code>；价格示例：<code>$5</code>；公式 $x$。",
    });
    const document = dom.window.document;
    const code = Array.from(document.querySelectorAll("#prompt code")).map((element) => element.textContent);
    expect(code).toEqual(["echo $HOME", "$5"]);
    expect(document.getElementById("prompt")?.innerHTML).toContain("\\(x\\)");
  });

  it("parses escaped extra JSON and renders its node as inert text", () => {
    const dom = renderTemplate("front", {
      id: "R09",
      type: "mindmap",
      extra: '{"mindmap":[{"text":"&lt;img src=x onerror=document.documentElement.dataset.injected=1&gt;"}]}',
    });
    const document = dom.window.document;
    const label = document.querySelector(".mindmap-label");
    expect(label?.textContent).toContain("<img src=x onerror=");
    expect(label?.querySelector("img")).toBeNull();
    expect(document.documentElement.dataset.injected).toBeUndefined();
  });

  it("sanitizes rich HTML and normalizes occlusion images", () => {
    const dom = renderTemplate("front", {
      id: "O-SAFE",
      type: "occlusion",
      extra: '{"masks":[{"id":"1","x":10,"y":10,"w":20,"h":20,"label":"&lt;img src=x onerror=alert(1)&gt;"}]}',
      occlusionImage: '<img src="red.png" onerror="document.documentElement.dataset.injected=1">',
    });
    const document = dom.window.document;
    const image = document.querySelector(".occlusion-canvas img");
    expect(image?.classList.contains("occlusion-image")).toBe(true);
    expect(image?.hasAttribute("onerror")).toBe(false);
    expect(document.querySelector(".occlusion-mask img")).toBeNull();
    expect(document.documentElement.dataset.injected).toBeUndefined();
  });

  it("shows choice options immediately by default", () => {
    const dom = renderTemplate("front", CHOICE_FIELDS);
    expect(dom.window.document.querySelectorAll(".option-card")).toHaveLength(4);
    expect(dom.window.document.getElementById("choice-reveal")).toBeNull();
    dom.window.close();
  });

  it("keeps manual choice options inaccessible until explicitly revealed", () => {
    const dom = renderTemplate("front", CHOICE_FIELDS, { choiceDisplay: "manual" });
    const document = dom.window.document;
    const revealCommands: string[] = [];
    Object.assign(dom.window, { pycmd: (command: string) => revealCommands.push(command) });
    expect(document.querySelectorAll(".option-card")).toHaveLength(0);
    expect(document.getElementById("setting-choice-delay-row")?.classList.contains("hidden")).toBe(true);
    expect((document.getElementById("setting-choice-delay-ms") as HTMLInputElement).disabled).toBe(true);
    const reveal = document.getElementById("choice-reveal") as HTMLButtonElement;
    expect(reveal.textContent).toBe("显示选项");
    reveal.click();
    expect(document.querySelectorAll(".option-card")).toHaveLength(4);
    expect(document.querySelectorAll(".selected-option")).toHaveLength(0);
    expect(dom.window.sessionStorage.length).toBe(0);
    expect(revealCommands).toEqual([]);
    dom.window.close();
  });

  it("reveals delayed choice options only after the configured interval", () => {
    vi.useFakeTimers();
    const dom = renderTemplate("front", CHOICE_FIELDS, { choiceDisplay: "delay", choiceDelayMs: 750 });
    const document = dom.window.document;
    expect(document.querySelectorAll(".option-card")).toHaveLength(0);
    expect(document.getElementById("setting-choice-delay-row")?.classList.contains("hidden")).toBe(false);
    expect((document.getElementById("setting-choice-delay-ms") as HTMLInputElement).disabled).toBe(false);
    expect(document.querySelector(".choice-gate")?.textContent).toContain("750 ms");
    vi.advanceTimersByTime(749);
    expect(document.querySelectorAll(".option-card")).toHaveLength(0);
    vi.advanceTimersByTime(1);
    expect(document.querySelectorAll(".option-card")).toHaveLength(4);
    dom.window.close();
  });

  it("cancels a pending delay when switching to manual mode", () => {
    vi.useFakeTimers();
    const dom = renderTemplate("front", CHOICE_FIELDS, { choiceDisplay: "delay", choiceDelayMs: 750 });
    const document = dom.window.document;
    const select = document.getElementById("setting-choice-display") as HTMLSelectElement;
    select.value = "manual";
    select.dispatchEvent(new dom.window.Event("change", { bubbles: true }));
    vi.advanceTimersByTime(750);
    expect(document.querySelectorAll(".option-card")).toHaveLength(0);
    expect(document.getElementById("choice-reveal")).not.toBeNull();
    dom.window.close();
  });

  it("persists the manual display mode across a template refresh", () => {
    const first = renderTemplate("front", CHOICE_FIELDS);
    const select = first.window.document.getElementById("setting-choice-display") as HTMLSelectElement;
    select.value = "manual";
    select.dispatchEvent(new first.window.Event("change", { bubbles: true }));
    const persisted = JSON.parse(first.window.localStorage.getItem("AAS-SETTINGS") || "{}");
    first.window.close();

    const refreshed = renderTemplate("front", CHOICE_FIELDS, persisted);
    expect(refreshed.window.document.querySelectorAll(".option-card")).toHaveLength(0);
    expect(refreshed.window.document.getElementById("choice-reveal")).not.toBeNull();
    refreshed.window.close();
  });

  it("does not render the startup probe and exposes dialog semantics", () => {
    const dom = renderTemplate("front", {});
    const document = dom.window.document;
    expect(document.getElementById("anki-startup-probe")).toBeNull();
    const modal = document.getElementById("settings-modal");
    expect(modal?.getAttribute("role")).toBe("dialog");
    expect(modal?.getAttribute("aria-modal")).toBe("true");
    expect(modal?.getAttribute("aria-hidden")).toBe("true");
  });
});
