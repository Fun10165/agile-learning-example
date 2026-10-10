from __future__ import annotations
from collections.abc import Callable, Iterable
from html import escape

import json
import math
import wave
from pathlib import Path

import genanki


ROOT = Path(__file__).resolve().parent.parent
MEDIA_DIR = ROOT / "media"
OUTPUT = ROOT / "anki-open-template-test.apkg"

MODEL_ID = 1607392319
DECK_ID = 2059400111


def ensure_test_audio() -> Path:
    MEDIA_DIR.mkdir(exist_ok=True)
    audio_path = MEDIA_DIR / "test.wav"
    if audio_path.exists():
        return audio_path

    sample_rate = 22050
    duration_seconds = 1.2
    frequency = 523.25
    amplitude = 12000
    frames = []
    for index in range(int(sample_rate * duration_seconds)):
        value = int(amplitude * math.sin(2 * math.pi * frequency * index / sample_rate))
        frames.append(value.to_bytes(2, byteorder="little", signed=True))

    with wave.open(str(audio_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(b"".join(frames))

    return audio_path


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ensure_generated_templates_current() -> None:
    build_script = ROOT / "scripts" / "build_templates.mjs"
    pairs = [
        (
            ROOT / "front.html",
            [build_script, ROOT / "src" / "front.ts", ROOT / "src" / "shared.ts", ROOT / "templates" / "front.template.html"],
        ),
        (
            ROOT / "back.html",
            [build_script, ROOT / "src" / "back.ts", ROOT / "src" / "shared.ts", ROOT / "templates" / "back.template.html"],
        ),
    ]
    stale_outputs = []
    for output_path, source_paths in pairs:
        output_mtime = output_path.stat().st_mtime
        if any(source_path.stat().st_mtime > output_mtime for source_path in source_paths):
            stale_outputs.append(output_path.name)
    if stale_outputs:
        names = ", ".join(stale_outputs)
        raise RuntimeError(f"Generated template(s) stale: {names}. Run `npm run build` before exporting APKG files.")


def build_model() -> genanki.Model:
    ensure_generated_templates_current()
    return genanki.Model(
        MODEL_ID,
        "Anki Open Template Test Model",
        fields=[
            {"name": "id"},
            {"name": "type"},
            {"name": "question"},
            {"name": "options"},
            {"name": "answer"},
            {"name": "notes"},
            {"name": "extra"},
            {"name": "audio"},
            {"name": "occlusion_image"},
        ],
        templates=[
            {
                "name": "Late Template",
                "qfmt": load_text(ROOT / "front.html"),
                "afmt": load_text(ROOT / "back.html"),
            }
        ],
        css=load_text(ROOT / "styles.css"),
    )


NOTE_FIELD_COUNT = 9
EXTRA_FIELD_INDEX = 6
RICH_HTML_FIELD_INDEXES = frozenset({2, 3, 5, 8})


class TrustedHtml(str):
    """Explicitly marks repository-authored rich HTML for an Anki field."""


class InvalidJsonFixture(str):
    """Explicitly marks the one malformed-extra regression fixture."""


def trusted_html(value: str) -> TrustedHtml:
    return TrustedHtml(value)


def invalid_json_fixture(value: str) -> InvalidJsonFixture:
    return InvalidJsonFixture(value)


def prepare_note_fields(fields: list[str | TrustedHtml | InvalidJsonFixture]) -> list[str]:
    if len(fields) != NOTE_FIELD_COUNT:
        raise ValueError(f"Expected exactly {NOTE_FIELD_COUNT} note fields, got {len(fields)}")
    if not str(fields[0]).strip():
        raise ValueError("Card id must not be empty")

    extra = str(fields[EXTRA_FIELD_INDEX]).strip()
    extra_field = fields[EXTRA_FIELD_INDEX]
    if isinstance(extra_field, InvalidJsonFixture):
        pass
    elif extra:
        try:
            parsed_extra = json.loads(extra)
        except json.JSONDecodeError as error:
            raise ValueError("extra must be valid JSON") from error
        if not isinstance(parsed_extra, dict):
            raise ValueError("extra must be a JSON object")

    prepared: list[str] = []
    for index, value in enumerate(fields):
        if not isinstance(value, str):
            raise TypeError(f"Field {index + 1} must be a string")
        if isinstance(value, TrustedHtml):
            if index not in RICH_HTML_FIELD_INDEXES:
                raise ValueError(f"Field {index + 1} does not accept trusted HTML")
            prepared.append(str(value))
        elif isinstance(value, InvalidJsonFixture):
            if index != EXTRA_FIELD_INDEX:
                raise ValueError("InvalidJsonFixture is only valid for the extra field")
            prepared.append(escape(value, quote=False))
        else:
            prepared.append(escape(value, quote=False))
    return prepared


def note(
    model: genanki.Model,
    fields: list[str | TrustedHtml | InvalidJsonFixture],
    tags: list[str] | None = None,
) -> genanki.Note:
    return genanki.Note(model=model, fields=prepare_note_fields(fields), tags=tags or [])


def write_deck(
    deck_id: int,
    deck_name: str,
    output_path: Path,
    notes_source: Iterable[genanki.Note] | Callable[[genanki.Model], Iterable[genanki.Note]],
    media_files: Iterable[Path] = (),
) -> None:
    if not isinstance(deck_id, int) or deck_id <= 0:
        raise ValueError("deck_id must be a positive integer")
    if not deck_name.strip():
        raise ValueError("deck_name must not be empty")
    if not output_path.parent.is_dir():
        raise FileNotFoundError(f"Output directory does not exist: {output_path.parent}")
    media_paths = list(media_files)
    missing_media = [path for path in media_paths if not path.is_file()]
    if missing_media:
        raise FileNotFoundError(f"Missing media file(s): {', '.join(str(path) for path in missing_media)}")
    media_names = [path.name for path in media_paths]
    if len(media_names) != len(set(media_names)):
        raise ValueError("Media filenames must be unique because Anki stores media in a flat namespace")

    model = build_model()
    notes = notes_source(model) if callable(notes_source) else notes_source
    deck = genanki.Deck(deck_id, deck_name)
    seen_card_ids: set[str] = set()
    card_count = 0
    for item in notes:
        card_id = item.fields[0]
        if card_id in seen_card_ids:
            raise ValueError(f"Duplicate card id {card_id!r} in deck {deck_name!r}")
        seen_card_ids.add(card_id)
        item.guid = genanki.guid_for(str(deck_id), card_id)
        deck.add_note(item)
        card_count += 1

    package = genanki.Package(deck)
    package.media_files = [str(path) for path in media_paths]
    package.write_to_file(str(output_path))
    print(f"Wrote {output_path}")
    print(f"Deck: {deck_name}")
    print(f"Cards: {card_count}")


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        note(
            model,
            [
                "C01",
                "choice",
                "中国的首都是哪座城市？",
                "北京||上海||广州||深圳",
                "1",
                "北京是中国首都。此卡用于验证单选、自动翻面、答案回填、解析显示。",
                "",
                "",
                "",
            ],
            ["base", "choice", "single"],
        ),
        note(
            model,
            [
                "C02",
                "choice",
                "下列哪些属于编程语言？",
                "Python||Banana||Rust||Notebook||Go",
                "1||3||5",
                "Python、Rust、Go 都是编程语言。本卡用于测试多选、统计、漏选、误选。",
                "",
                "",
                "",
            ],
            ["base", "choice", "multi"],
        ),
        note(
            model,
            [
                "Q01",
                "qa",
                "简述 TCP 三次握手的目的。",
                "",
                "建立可靠连接并确认双方的发送与接收能力。",
                "三次握手的核心是同步双方的初始序列号，并确认收发链路可用。本卡用于测试问答题正反面展示与解析编辑。",
                "",
                "",
                "",
            ],
            ["base", "qa"],
        ),
        note(
            model,
            [
                "F01",
                "fill",
                "HTTP 默认端口是 {{c1::80::请输入端口号}}。",
                "",
                "80",
                "用于测试单空输入、Enter 提交、背面回显。",
                "",
                "",
                "",
            ],
            ["base", "fill"],
        ),
        note(
            model,
            [
                "F02",
                "fill",
                "React 中用于状态管理的基础 Hook 是 {{c1::useState::Hook 名称}}，用于副作用处理的是 {{c2::useEffect::Hook 名称}}，用于引用 DOM 或可变值的是 {{c3::useRef::Hook 名称}}。",
                "",
                "useState||useEffect||useRef",
                "用于测试多空输入、长文本、状态持久化和逐项回显。",
                "",
                "",
                "",
            ],
            ["base", "fill", "multi-cloze"],
        ),
        note(
            model,
            [
                "O01",
                "occlusion",
                "请指出图中的两个重点区域。",
                "",
                "",
                "用于测试图片遮挡的点击显隐、显示下一个挖空、切换全部遮挡。",
                '{"image":"red.png","masks":[{"id":"1","x":10,"y":10,"w":25,"h":30,"label":"区域1"},{"id":"2","x":55,"y":45,"w":25,"h":30,"label":"区域2"}]}',
                "",
                trusted_html('<img class="occlusion-image" src="red.png">'),
            ],
            ["base", "occlusion"],
        ),
        note(
            model,
            [
                "M01",
                "mindmap",
                "观察下面的思维导图结构。",
                "",
                "",
                "用于测试思维导图节点渲染、折叠展开、移动端布局。",
                '{"mindmap":[{"text":"计算机网络","children":[{"text":"分层模型"},{"text":"TCP/IP"},{"text":"HTTP"}]}]}',
                "",
                "",
            ],
            ["base", "mindmap"],
        ),
        note(
            model,
            [
                "A01",
                "qa",
                "播放下面的音频并测试播放器。",
                "",
                "",
                "用于测试播放、暂停、倍速切换。",
                "",
                "[sound:test.wav]",
                "",
            ],
            ["base", "audio"],
        ),
        note(
            model,
            [
                "C03",
                "choice",
                trusted_html('若行内公式为 $a^2+b^2=c^2$，下列哪一项是块级展示？<br><br>注意测试公式与多段解析。'),
                trusted_html('$x+y$||$$x^2+y^2=z^2$$||普通文本||<img src="1-mac-single.png">'),
                "2",
                trusted_html('第一段：用于测试行内公式和块级公式。<br><br>第二段：这里加入较长解析文本，用于测试前面解析区域的滚动行为。你可以继续复制这一段多次，让内容足够长，以观察滚动是否稳定。<br><br>第三段：测试图片在解析中的缩放行为。<br><img src="2-windows-single.png">'),
                "",
                "",
                "",
            ],
            ["complex", "choice", "math"],
        ),
        note(
            model,
            [
                "Q02",
                "qa",
                trusted_html('下面这张图展示了什么？<br><img src="fields.png">'),
                "",
                "这是模板字段示意图。",
                trusted_html('<b>粗体测试</b><br><i>斜体测试</i><br><br><img src="settings.png"><br>用于测试问答题中图片和 HTML 的显示。'),
                "",
                "",
                "",
            ],
            ["complex", "qa", "image"],
        ),
        note(
            model,
            [
                "F03",
                "fill",
                "在公式 $$E = mc^2$$ 中，{{c1::E::符号}} 表示能量，speed of light 是 {{c2::c::符号}}，而质量是 {{c3::m::符号}}。",
                "",
                "E||c||m",
                "用于测试公式环境中多个填空、英文提示、中英混排。",
                "",
                "",
                "",
            ],
            ["complex", "fill", "math"],
        ),
        note(
            model,
            [
                "O02",
                "occlusion",
                "用于测试“显示下一个挖空”的顺序。",
                "",
                "",
                "先把显示顺序设为“先上下后左右”，测一遍；再改成“先左右后上下”，重测。",
                '{"image":"3-ubuntu-single.png","masks":[{"id":"1","x":8,"y":10,"w":12,"h":10,"label":"A"},{"id":"2","x":60,"y":12,"w":12,"h":10,"label":"B"},{"id":"3","x":12,"y":45,"w":12,"h":10,"label":"C"},{"id":"4","x":62,"y":50,"w":12,"h":10,"label":"D"}]}',
                "",
                trusted_html('<img class="occlusion-image" src="3-ubuntu-single.png">'),
            ],
            ["complex", "occlusion", "order"],
        ),
        note(
            model,
            [
                "M02",
                "mindmap",
                "验证导图节点内挖空。",
                "",
                "",
                "用于测试导图节点内的挖空展示和背面答案。",
                '{"mindmap":[{"text":"前端","children":[{"text":"框架：{{c1::React}}"},{"text":"样式：CSS"},{"text":"构建：Vite","children":[{"text":"插件系统"},{"text":"热更新"}]}]}]}',
                "",
                "",
            ],
            ["complex", "mindmap", "cloze"],
        ),
        note(
            model,
            [
                "R01",
                "qa",
                '特殊字符测试：&lt;div&gt; "quote" \'single\' [brackets] {braces} #hash',
                "",
                "特殊字符不应让模板崩溃。",
                '解析里也加入相同字符：&lt;tag&gt; "double" \'single\' {json}',
                "",
                "",
                "",
            ],
            ["edge", "special-char"],
        ),
        note(
            model,
            [
                "R02",
                "qa",
                "这是一个没有解析的问答题。",
                "",
                "无解析时不应显示空白解析壳。",
                "",
                "",
                "",
                "",
            ],
            ["edge", "empty-notes"],
        ),
        note(
            model,
            [
                "R03",
                "occlusion",
                "非法 extra JSON 测试。",
                "",
                "",
                "用于测试 extra 非法时模板的降级能力。",
                invalid_json_fixture('{"image":"broken.png","masks":[}'),
                "",
                "",
            ],
            ["edge", "bad-extra"],
        ),
        note(
            model,
            [
                "R04",
                "qa",
                "长标签显示测试。",
                "",
                "标签应换行显示。",
                "给这张卡添加多个 tag，用于测试标签区换行。",
                "",
                "",
                "",
            ],
            ["edge", "tag-01", "tag-02", "tag-03", "tag-04", "tag-05", "tag-06", "tag-07", "tag-08"],
        ),
        note(
            model,
            [
                "R05",
                "choice",
                "这张卡专门用于验证随机顺序正反面一致。",
                "选项A||选项B||选项C||选项D||选项E",
                "4",
                "开启随机顺序后，正面与背面的选项顺序必须完全一致。",
                "",
                "",
                "",
            ],
            ["edge", "random-order"],
        ),
        note(
            model,
            [
                "R06",
                "fill",
                "第一个空 {{c1::alpha}}，第二个空 {{c2::beta}}。",
                "",
                "alpha||beta",
                "本卡用于和 F02、O01 交叉测试状态隔离。",
                "",
                "",
                "",
            ],
            ["edge", "state-isolation"],
        ),
        note(
            model,
            [
                "R07",
                "qa",
                "What does <div> mean? C++ 类型 std::vector<int> 中的尖括号必须保留。",
                "",
                "std::vector<int>",
                "普通文本中的 <div>、<int> 和 x < y > z 不得被识别成 HTML。",
                "",
                "",
                "",
            ],
            ["edge", "literal-angle-brackets"],
        ),
        note(
            model,
            [
                "R08",
                "qa",
                trusted_html("Shell 示例：<code>echo $HOME</code>；价格示例：<code>$5</code>。"),
                "",
                "代码元素中的美元符号不是数学分隔符。",
                "普通文本中的 $x$ 仍应作为行内数学公式处理。",
                "",
                "",
                "",
            ],
            ["edge", "math-code"],
        ),
        note(
            model,
            [
                "R09",
                "mindmap",
                "extra 中的节点文本必须按纯文本渲染。",
                "",
                "",
                "节点文本不可创建 img 元素或执行事件属性。",
                '{"mindmap":[{"text":"<img src=x onerror=document.documentElement.dataset.injected=1>"}]}',
                "",
                "",
            ],
            ["edge", "json-text-injection"],
        ),
    ]


def main() -> None:
    media_files = [
        ensure_test_audio(),
        MEDIA_DIR / "red.png",
        MEDIA_DIR / "fields.png",
        MEDIA_DIR / "settings.png",
        MEDIA_DIR / "1-mac-single.png",
        MEDIA_DIR / "2-windows-single.png",
        MEDIA_DIR / "3-ubuntu-single.png",
    ]
    write_deck(
        DECK_ID,
        "Anki Open Template :: Manual Test Deck",
        OUTPUT,
        build_notes,
        media_files,
    )


if __name__ == "__main__":
    main()
