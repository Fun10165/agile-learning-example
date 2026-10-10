from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck, trusted_html

DECK_ID = 2059400711
OUTPUT = ROOT / "anki-Rust-第一章-入门指南.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════════════════════════════════════════════════════
        # §1.1 安装 · 工具链基础
        # ═══════════════════════════════════════════════════════════

        # ── RQ01 · rustup 是什么 ──
        note(
            model,
            [
                "RQ01",
                "qa",
                "[Rust 工具链] 管理 Rust 工具链版本和交叉编译目标安装的命令行工具叫什么？",
                "",
                "rustup",
                "rustup 通过 rustup update 更新版本、rustup target add 添加编译目标。类比 nvm（Node）或 pyenv（Python）。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "tools", "rustup", "qa"],
        ),
        # ── RQ02 · rustup 翻转 ──
        note(
            model,
            [
                "RQ02",
                "qa",
                "[Rust 工具链] rustup 是什么？",
                "",
                "管理 Rust 工具链版本和编译目标的命令行工具。",
                "双向记忆——RQ01 从功能问名称，本卡从名称问功能。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "tools", "rustup", "qa", "flip"],
        ),
        # ── RF01 · rustup update ──
        note(
            model,
            [
                "RF01",
                "fill",
                "[Rust 工具链] 通过 rustup 安装 Rust 之后，更新到最新稳定版的命令是 {{c1::rustup update}}。",
                "",
                "rustup update",
                "来源：TRPL §1.1「更新与卸载」节。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "tools", "rustup", "fill"],
        ),
        # ── RF02 · rustup self uninstall ──
        note(
            model,
            [
                "RF02",
                "fill",
                "[Rust 工具链] 卸载 Rust 和 rustup 的命令是 {{c1::rustup self uninstall}}。",
                "",
                "rustup self uninstall",
                "来源：TRPL §1.1「更新与卸载」节。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "tools", "rustup", "fill"],
        ),
        # ── RF03 · rustup doc ──
        note(
            model,
            [
                "RF03",
                "fill",
                "[Rust 工具链] 在浏览器中打开 Rust 本地离线文档的命令是 {{c1::rustup doc}}。",
                "",
                "rustup doc",
                "Rust 安装时附带标准库文档副本，rustup doc 在默认浏览器中打开。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "tools", "rustup", "fill"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §1.2 Hello, World! · 编译模型与程序结构
        # ═══════════════════════════════════════════════════════════

        # ── RQ03 · AOT 编译 ──
        note(
            model,
            [
                "RQ03",
                "qa",
                "[Rust 编译模型] Rust 属于哪一类编译模型的语言？",
                "",
                "预先编译（ahead-of-time compiled，AOT）",
                "来源：TRPL §1.2「编译与运行」。AOT 意味着编译和运行是两个独立的步骤，编译产出独立二进制文件。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "compilation", "aot", "qa"],
        ),
        # ── RQ04 · AOT 分发优势 ──
        note(
            model,
            [
                "RQ04",
                "qa",
                "[Rust 编译模型] Rust 是 AOT 编译语言。这带来了什么分发优势？",
                "",
                "可以把编译好的二进制文件直接交给别人运行，对方无需安装 Rust。",
                "来源：TRPL §1.2。对比：Python/Ruby/JS 需要对方安装对应运行时。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "compilation", "aot", "qa"],
        ),
        # ── RF04 · rustc 编译命令 ──
        note(
            model,
            [
                "RF04",
                "fill",
                "[Rust 工具链] 不借助 Cargo，直接用命令行把 main.rs 编译成可执行文件：{{c1::rustc main.rs}}。",
                "",
                "rustc main.rs",
                "rustc 是 Rust 编译器。输出为可执行文件 main（或 main.exe），与源文件同目录。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "tools", "rustc", "fill"],
        ),
        # ── RF05 · 源文件命名 ──
        note(
            model,
            [
                "RF05",
                "fill",
                "[Rust 基础] Rust 源文件以 {{c1::.rs}} 扩展名结尾。文件名含多个单词时用 {{c2::下划线 _}} 分隔（如 hello_world.rs）。",
                "",
                ".rs||下划线 _",
                "Rust 代码风格统一使用 snake_case 命名文件、变量和函数。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "basics", "naming", "fill", "multi-cloze"],
        ),
        # ── RQ05 · main 函数入口 ──
        note(
            model,
            [
                "RQ05",
                "qa",
                "[Rust 程序结构] 每个可执行的 Rust 程序中，最先运行的代码是什么？",
                "",
                "main 函数——由 fn main() { } 定义。",
                "来源：TRPL §1.2。main 是 Rust 可执行程序的入口点（entry point），操作系统启动程序后从这里开始执行。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "basics", "main", "entry-point", "qa"],
        ),
        # ── RF06 · fn main 语法 ──
        note(
            model,
            [
                "RF06",
                "fill",
                trusted_html("[Rust 语法] 定义 main 函数：\n<pre>fn main() {\n    // 函数体\n}</pre>\n关键字 {{c1::fn}} 声明函数，{{c2::main}} 是函数名，参数放 {{c3::()}} 中（此处无参数），函数体在 {{c4::{ }}} 中。"),
                "",
                "fn||main||()||{ }",
                "fn 是 Rust 声明函数的关键字（类比 C 的 void、Python 的 def）。Rust 强制所有函数体用花括号包裹。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "syntax", "fn", "main", "fill", "multi-cloze"],
        ),
        # ── RQ06 · println! 的 ! ──
        note(
            model,
            [
                "RQ06",
                "qa",
                "[Rust 语法] println!(\"Hello\"); 中的 ! 表示什么？",
                "",
                "表示 println! 是一个宏（macro），而非普通函数。宏用代码生成代码，调用规则与函数不完全相同。",
                "来源：TRPL §1.2。看到 ! 就代表调用的是宏。println 不带 ! 才是函数调用（但标准库没有叫 println 的函数）。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "syntax", "macro", "println", "qa"],
        ),
        # ── RF07 · 语句分号 ──
        note(
            model,
            [
                "RF07",
                "fill",
                "[Rust 语法] 在 Rust 中，一个语句的结束用 {{c1::;}}（分号）标记。",
                "",
                ";",
                "来源：TRPL §1.2。分号将表达式（expression）转为语句（statement）。后续章节会深入表达式与语句的区别。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "syntax", "semicolon", "fill"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §1.3 Hello, Cargo! · Cargo 构建系统
        # ═══════════════════════════════════════════════════════════

        # ── RQ07 · Cargo 是什么 ──
        note(
            model,
            [
                "RQ07",
                "qa",
                "[Cargo] Cargo 是什么？",
                "",
                "Cargo 是 Rust 的构建系统兼包管理器。构建系统负责编译代码；包管理器负责下载和管理依赖库（crate）。",
                "来源：TRPL §1.3。类比：Cargo ≈ Make/Ninja + npm/pip。是 Rust 开发的标准工具。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "build-system", "qa"],
        ),
        # ── RF08 · cargo new ──
        note(
            model,
            [
                "RF08",
                "fill",
                "[Cargo] 创建名为 my_project 的新项目：{{c1::cargo new my_project}}。",
                "",
                "cargo new my_project",
                "这会创建 my_project/ 目录，内含 Cargo.toml 配置文件和 src/main.rs。默认还初始化 Git 仓库。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "new", "fill"],
        ),
        # ── RF09 · cargo build ──
        note(
            model,
            [
                "RF09",
                "fill",
                "[Cargo] 编译 Cargo 项目（debug 模式）：{{c1::cargo build}}。",
                "",
                "cargo build",
                "编译产物放在 target/debug/ 目录。默认是 debug 构建，未优化但编译快。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "build", "fill"],
        ),
        # ── RF10 · cargo run ──
        note(
            model,
            [
                "RF10",
                "fill",
                "[Cargo] 一步完成编译 + 运行 Cargo 项目：{{c1::cargo run}}。",
                "",
                "cargo run",
                "cargo run = cargo build + 自动执行可执行文件。源文件未变化时跳过编译直接运行。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "run", "fill"],
        ),
        # ── RF11 · cargo check ──
        note(
            model,
            [
                "RF11",
                "fill",
                "[Cargo] 只检查代码能否编译（不生成可执行文件），比 cargo build 更快的命令是 {{c1::cargo check}}。",
                "",
                "cargo check",
                "跳过代码生成和链接步骤，速度更快。适合开发中频繁检查语法和类型错误。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "check", "fill"],
        ),
        # ── RF12 · cargo build --release ──
        note(
            model,
            [
                "RF12",
                "fill",
                "[Cargo] 以优化模式编译（适合最终发布），输出到 target/release/：{{c1::cargo build --release}}。",
                "",
                "cargo build --release",
                "release 构建开启编译优化，运行速度更快，但编译时间更长。做基准测试必须用 release 构建。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "release", "fill"],
        ),
        # ── RF13 · 构建输出路径 ──
        note(
            model,
            [
                "RF13",
                "fill",
                "[Cargo] 默认 debug 构建的可执行文件在 {{c1::target/debug/}} 目录；release 构建在 {{c2::target/release/}} 目录。",
                "",
                "target/debug/||target/release/",
                "Cargo 将构建产物统一放在 target/ 下，与源码目录 src/ 分离，保持项目整洁。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "build-output", "fill", "multi-cloze"],
        ),
        # ── RF14 · 项目结构 ──
        note(
            model,
            [
                "RF14",
                "fill",
                "[Cargo] Cargo 项目中，源代码放在 {{c1::src/}} 目录，项目配置文件是 {{c2::Cargo.toml}}。",
                "",
                "src/||Cargo.toml",
                "Cargo 约定：src/ 放源码，项目根目录放 README、LICENSE 等非代码文件。Cargo.toml 用 TOML 格式编写。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "project-structure", "fill", "multi-cloze"],
        ),
        # ── RF15 · Cargo.toml [package] ──
        note(
            model,
            [
                "RF15",
                "fill",
                "[Cargo] Cargo.toml 中 [package] section 的三个基本字段：\n- {{c1::name}}：项目名称\n- {{c2::version}}：版本号\n- {{c3::edition}}：Rust Edition",
                "",
                "name||version||edition",
                "TOML 格式，[package] 是 section 标题。edition 指定 Rust 语言版本（如 \"2021\"、\"2024\"），决定编译器行为和可用特性。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "toml", "fill", "multi-cloze"],
        ),
        # ── RQ08 · crate 是什么 ──
        note(
            model,
            [
                "RQ08",
                "qa",
                "[Rust 生态] 在 Rust 中，代码的编译和分发单元叫什么？",
                "",
                "crate（常译为「包」或保留原文）",
                "来源：TRPL §1.3。crate 是 Rust 编译器一次处理的最小代码单元。Cargo 管理的依赖就是 crate。后续章节会区分 binary crate 和 library crate。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "ecosystem", "crate", "qa"],
        ),
        # ── RF16 · [dependencies] & crate ──
        note(
            model,
            [
                "RF16",
                "fill",
                "[Cargo] 在 Cargo.toml 中，项目依赖列在 {{c1::[dependencies]}} section 下。Rust 中代码包被称为 {{c2::crate}}。",
                "",
                "[dependencies]||crate",
                "Cargo.toml 示例：\n[dependencies]\nrand = \"0.8.5\"\n运行 cargo build 时 Cargo 自动下载并编译依赖。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "dependencies", "crate", "fill", "multi-cloze"],
        ),
        # ── RQ09 · Cargo.lock 作用 ──
        note(
            model,
            [
                "RQ09",
                "qa",
                "[Cargo] Cargo.lock 文件的作用是什么？需要手动修改吗？",
                "",
                "记录依赖的精确版本号，确保构建可复现。不需要手动修改，Cargo 自动管理。",
                "来源：TRPL §1.3。Cargo.toml 声明依赖范围（如 rand = \"0.8.5\"），Cargo.lock 锁定精确版本。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "lock", "qa"],
        ),
        # ── RC01 · Cargo 子命令区分 ──
        note(
            model,
            [
                "RC01",
                "choice",
                "[Cargo] 以下哪个 Cargo 命令不会生成可执行文件？",
                "cargo build||cargo run||cargo check||cargo build --release",
                "3",
                "cargo check 跳过代码生成和链接，只检查编译是否通过，因此最快。cargo build 和 cargo run 都生成可执行文件。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "commands", "choice"],
        ),
        # ── RC02 · debug vs release ──
        note(
            model,
            [
                "RC02",
                "choice",
                "[Cargo] 以下关于 debug 构建与 release 构建的说法，哪项正确？",
                "debug 构建运行更快，适合基准测试||release 构建编译更快，适合开发中频繁构建||release 构建开启优化，运行更快但编译更慢，适合最终发布||debug 构建的可执行文件在 target/release/ 目录",
                "3",
                "debug（默认）：无优化，编译快，适合开发。release（--release）：开启优化，编译慢，运行快，适合发布和基准测试。",
                "",
                "",
                "",
            ],
            ["ch1", "rust", "cargo", "debug", "release", "choice"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "Rust TRPL · 第一章：入门指南", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
