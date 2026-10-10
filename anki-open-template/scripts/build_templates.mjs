import { build } from "esbuild";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SCRIPT_PLACEHOLDER = "/*__SCRIPT__*/";
const SCRIPT_PLACEHOLDER_PATTERN = /\/\*__SCRIPT__\*\//g;

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));

function assertSingleScriptPlaceholder(template, templatePath) {
  const count = template.match(SCRIPT_PLACEHOLDER_PATTERN)?.length ?? 0;
  if (count === 0) {
    throw new Error(
      `${templatePath} is missing the ${SCRIPT_PLACEHOLDER} placeholder.`,
    );
  }
  if (count > 1) {
    throw new Error(
      `${templatePath} contains ${count} ${SCRIPT_PLACEHOLDER} placeholders; expected exactly one.`,
    );
  }
}

async function bundle(entry) {
  const result = await build({
    entryPoints: [path.join(root, "src", `${entry}.ts`)],
    bundle: true,
    write: false,
    format: "iife",
    platform: "browser",
    target: ["es2018"],
    charset: "utf8",
    logLevel: "silent",
  });
  return result.outputFiles[0].text.trim();
}

async function render(name) {
  const templatePath = path.join(root, "templates", `${name}.template.html`);
  const outputPath = path.join(root, `${name}.html`);
  const [template, script] = await Promise.all([
    fs.readFile(templatePath, "utf8"),
    bundle(name),
  ]);
  assertSingleScriptPlaceholder(template, templatePath);
  const rendered = template.replace(SCRIPT_PLACEHOLDER, script);
  await fs.writeFile(outputPath, rendered, "utf8");
}

await render("front");
await render("back");
