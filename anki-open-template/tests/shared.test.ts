// @vitest-environment jsdom

import { beforeEach, describe, expect, it } from "vitest";
import {
  DEFAULT_SETTINGS,
  cardStateKey,
  collectClozeTokens,
  loadSettings,
  normalizeMasks,
  normalizeMathHtml,
  normalizeOcclusionImageHtml,
  renderCloze,
  renderInlineCloze,
  saveSettings,
} from "../src/shared";

describe("safe field rendering", () => {
  it("keeps code dollars literal while converting surrounding math", () => {
    const result = normalizeMathHtml('<code>echo $HOME</code><pre>$5</pre><span>$x$</span>');
    expect(result).toContain("<code>echo $HOME</code>");
    expect(result).toContain("<pre>$5</pre>");
    expect(result).toContain("<span>\\(x\\)</span>");
  });

  it("removes executable markup from rich HTML", () => {
    const result = normalizeMathHtml('<script>window.pwned=1</script><img src="x" onerror="window.pwned=1"><a href="javascript:alert(1)">safe</a>');
    const container = document.createElement("div");
    container.innerHTML = result;
    expect(container.querySelector("script")).toBeNull();
    expect(container.querySelector("img")?.hasAttribute("onerror")).toBe(false);
    expect(container.querySelector("a")?.hasAttribute("href")).toBe(false);
  });

  it("drops forms, SVG, MathML, and unsafe URL actions", () => {
    const result = normalizeMathHtml('<form action="javascript:alert(1)"><input type="submit"></form><svg onload="alert(1)"><circle></circle></svg><math><mtext>x</mtext></math>');
    const container = document.createElement("div");
    container.innerHTML = result;
    expect(container.querySelector("form, input, svg, math")).toBeNull();
  });

  it("preserves the supported formatting and media tags", () => {
    const source = '<div><strong>strong</strong><em>em</em><br><img class="content-image" src="media.png" alt="media"><table><thead><tr><th scope="col">H</th></tr></thead><tbody><tr><td colspan="1">D</td></tr></tbody></table><a href="https://example.com" target="_blank">link</a></div>';
    const result = normalizeMathHtml(source);
    const container = document.createElement("div");
    container.innerHTML = result;
    expect(container.querySelector("strong")?.textContent).toBe("strong");
    expect(container.querySelector("em")?.textContent).toBe("em");
    expect(container.querySelector("img")?.getAttribute("src")).toBe("media.png");
    expect(container.querySelector("table td")?.textContent).toBe("D");
    expect(container.querySelector("a")?.getAttribute("href")).toBe("https://example.com");
    expect(container.querySelector("a")?.getAttribute("rel")).toBe("noopener noreferrer");
  });

  it("preserves generated fill inputs while dropping field-provided controls", () => {
    const result = renderCloze('Answer {{c1::42}}<input onclick="window.pwned=1">', "front", "line", { "1": "draft" });
    const container = document.createElement("div");
    container.innerHTML = result;
    const inputs = container.querySelectorAll("input.fill-input");
    expect(inputs).toHaveLength(1);
    expect(inputs[0].getAttribute("value")).toBe("draft");
    expect(inputs[0].hasAttribute("onclick")).toBe(false);
  });

  it("renders mindmap text as text rather than HTML", () => {
    const result = renderInlineCloze('<img src=x onerror="window.pwned=1">', "front");
    const container = document.createElement("div");
    container.innerHTML = result;
    expect(container.querySelector("img")).toBeNull();
    expect(container.textContent).toContain("<img src=x onerror=");
  });

  it("adds the occlusion image class and removes handlers", () => {
    const result = normalizeOcclusionImageHtml('<img src="red.png" onerror="window.pwned=1">');
    const container = document.createElement("div");
    container.innerHTML = result;
    const image = container.querySelector("img");
    expect(image?.classList.contains("occlusion-image")).toBe(true);
    expect(image?.hasAttribute("onerror")).toBe(false);
  });
});

describe("normalized state and data", () => {
  beforeEach(() => {
    const values = new Map<string, string>();
    const storage: Storage = {
      get length() {
        return values.size;
      },
      clear: () => values.clear(),
      getItem: (key) => values.get(key) ?? null,
      key: (index) => Array.from(values.keys())[index] ?? null,
      removeItem: (key) => values.delete(key),
      setItem: (key, value) => values.set(key, value),
    };
    Object.defineProperty(window, "localStorage", { configurable: true, value: storage });
  });

  it("namespaces review state by deck and card id", () => {
    expect(cardStateKey({ deck: "Deck A", id: "C01" })).not.toBe(cardStateKey({ deck: "Deck B", id: "C01" }));
  });

  it("rejects invalid persisted settings values", () => {
    window.localStorage.setItem("AAS-SETTINGS", JSON.stringify({
      showType: "yes",
      fillMode: "invalid",
      theme: "unknown",
      randomOptions: true,
    }));
    const settings = loadSettings();
    expect(settings.showType).toBe(true);
    expect(settings.fillMode).toBe("line");
    expect(settings.theme).toBe("warm");
    expect(settings.randomOptions).toBe(true);
  });

  it("persists choice display settings and clamps delay boundaries", () => {
    saveSettings({ ...DEFAULT_SETTINGS, choiceDisplay: "manual", choiceDelayMs: -250 });
    expect(loadSettings()).toMatchObject({ choiceDisplay: "manual", choiceDelayMs: 0 });

    window.localStorage.setItem("AAS-SETTINGS", JSON.stringify({ choiceDisplay: "delay", choiceDelayMs: 99999 }));
    expect(loadSettings()).toMatchObject({ choiceDisplay: "delay", choiceDelayMs: 60000 });
  });

  it("filters invalid masks and clamps valid coordinates", () => {
    const masks = normalizeMasks([
      { id: "a", x: -10, y: 90, w: 40, h: 30, label: "safe" },
      { id: "b", x: 10, y: 10, w: 0, h: 10 },
      { id: "c", x: "nan", y: 10, w: 10, h: 10 },
    ]);
    expect(masks).toEqual([{ id: "a", x: 0, y: 90, w: 40, h: 10, label: "safe" }]);
  });

  it("decodes escaped cloze answers for comparison and display", () => {
    expect(collectClozeTokens("{{c1::String\\::new()}}")).toEqual([
      { answer: "String::new()", hint: "" },
    ]);
    expect(renderCloze("{{c1::String\\::new()}}", "back")).toContain("String::new()");
    expect(collectClozeTokens("{{c1::vector&lt;int&gt;::type}}")).toEqual([
      { answer: "vector<int>", hint: "type" },
    ]);
  });
});
