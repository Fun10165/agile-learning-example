from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck, trusted_html

DECK_ID = 2059400721
OUTPUT = ROOT / "anki-Rust-第二章-猜数字游戏.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════════════════════════════════════════════════════
        # §2.1 use 语句 & prelude
        # ═══════════════════════════════════════════════════════════

        # ── RQ10 · use 语句作用 ──
        note(
            model,
            [
                "RQ10",
                "qa",
                "[Rust 模块] use 语句的作用是什么？",
                "",
                "将标准库或外部 crate 中的类型/函数/模块引入当前作用域，以便直接使用其短名称。",
                "来源：TRPL §2「处理一次猜测」。例如 use std::io; 之后就可以写 io::stdin()，否则需要写 std::io::stdin()。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "use", "module", "qa"],
        ),
        # ── RF17 · use 语法 ──
        note(
            model,
            [
                "RF17",
                "fill",
                trusted_html("[Rust 模块] 引入标准库的输入输出模块到当前作用域：<pre>{{c1::use std\\::io}};</pre>"),
                "",
                "use std::io",
                "路径用 :: 分隔，std 是标准库根模块，io 是其子模块。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "use", "syntax", "fill"],
        ),
        # ── RQ11 · prelude 概念（桥接卡）──
        note(
            model,
            [
                "RQ11",
                "qa",
                "[Rust 模块] 什么是 Rust 的预导入（prelude）？",
                "",
                "Rust 自动将标准库中的一组常用类型和 trait 带入每个程序的作用域，无需手动 use。这组内容就是 prelude。",
                "来源：TRPL §2。不像 C++ 需要 #include <iostream>，Rust 通过 prelude 减少了样板代码。不在 prelude 中的内容才需要 use。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "prelude", "module", "qa"],
        ),
        # ── RC03 · prelude 辨析 ──
        note(
            model,
            [
                "RC03",
                "choice",
                "[Rust 模块] 以下哪个需要手动 use 才能使用？（不在 prelude 中）",
                "println!||Vec||std::io::stdin||Option",
                "3",
                "println!、Vec、Option 都在 prelude 中，直接用。std::io 不在 prelude，必须 use std::io 或用全路径。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "prelude", "use", "choice"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.2 let 变量绑定 & mut
        # ═══════════════════════════════════════════════════════════

        # ── RQ12 · 变量默认不可变 ──
        note(
            model,
            [
                "RQ12",
                "qa",
                "[Rust 变量] Rust 中变量的默认可变性是什么？",
                "",
                "默认不可变（immutable）。一旦用 let 绑定值后，就不能再修改。",
                "来源：TRPL §2「使用变量储存值」。let apples = 5; 之后 apples 不能改。对比：大多数语言（C/Java/Python）变量默认可变。这是 Rust 安全哲学的基础。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "variable", "immutability", "qa"],
        ),
        # ── RQ13 · mut 关键字 ──
        note(
            model,
            [
                "RQ13",
                "qa",
                "[Rust 变量] 如何让 Rust 变量变为可变的？",
                "",
                "在 let 声明的变量名前加 mut 关键字：let mut x = 5;",
                "来源：TRPL §2。let mut bananas = 5; // 可变。第三章会深入讨论可变性。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "mut", "variable", "qa"],
        ),
        # ── RF18 · let 与 let mut 语法 ──
        note(
            model,
            [
                "RF18",
                "fill",
                trusted_html("[Rust 变量] <pre>let apples = 5;       // {{c1::不可变}}\nlet {{c2::mut}} bananas = 5;  // 可变</pre>"),
                "",
                "不可变||mut",
                "Rust 变量默认不可变是核心设计。let x = 5; 之后 x = 6; 会编译错误。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "let", "mut", "fill", "multi-cloze"],
        ),
        # ── RF19 · 注释语法 ──
        note(
            model,
            [
                "RF19",
                "fill",
                "[Rust 语法] Rust 的行注释以 {{c1:://}} 开头，持续到行尾。",
                "",
                "//",
                "来源：TRPL §2。Rust 忽略 // 之后的所有内容。块注释用 /* ... */。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "comment", "syntax", "fill"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.3 String 类型 & 关联函数
        # ═══════════════════════════════════════════════════════════

        # ── RQ14 · String 类型 ──
        note(
            model,
            [
                "RQ14",
                "qa",
                "[Rust 类型] Rust 标准库的 String 类型是什么？",
                "",
                "UTF-8 编码的、可增长的字符串类型。",
                "来源：TRPL §2。String 是堆上分配的，可以追加内容。区别于字符串字面量 &str（固定、不可变、栈上/静态区）。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "string", "type", "qa"],
        ),
        # ── RQ15 · 关联函数 ::new ──
        note(
            model,
            [
                "RQ15",
                "qa",
                "[Rust 类型] String::new() 中的 :: 语法表示什么？",
                "",
                ":: 表示 new 是 String 类型的关联函数（associated function）——针对类型本身（而非实例）实现的函数。",
                "来源：TRPL §2。类比：静态方法。很多类型都有 new() 作为构造函数惯例。区别于实例方法（用 . 调用）。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "associated-function", "new", "syntax", "qa"],
        ),
        # ── RF20 · String::new ──
        note(
            model,
            [
                "RF20",
                "fill",
                trusted_html("[Rust 类型] 创建一个空的 String：<pre>{{c1::String\\::new()}}</pre>"),
                "",
                "String::new()",
                "String::new() 返回一个新的空字符串。常用作 let mut s = String::new();",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "string", "new", "fill"],
        ),
        # ── RC04 · 关联函数 vs 实例方法 ──
        note(
            model,
            [
                "RC04",
                "choice",
                "[Rust 类型] 关于关联函数和实例方法，哪项正确？",
                "关联函数用 . 调用，实例方法用 :: 调用||两者都用 . 调用||关联函数用 :: 调用（如 String::new()），实例方法用 . 调用（如 s.trim()）||两者都用 :: 调用",
                "3",
                "关联函数针对类型本身（Type::func()），实例方法针对实例（instance.method()）。:: 是路径分隔符，. 是方法调用符。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "associated-function", "method", "choice"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.4 stdin / read_line / 引用 / Result
        # ═══════════════════════════════════════════════════════════

        # ── RQ16 · stdin 函数 ──
        note(
            model,
            [
                "RQ16",
                "qa",
                "[Rust I/O] std::io::stdin() 函数返回什么？",
                "",
                "返回一个 std::io::Stdin 类型的实例，代表终端的标准输入句柄。",
                "来源：TRPL §2。通过它调用 read_line 方法读取用户输入。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "io", "stdin", "qa"],
        ),
        # ── RF21 · read_line 调用 ──
        note(
            model,
            [
                "RF21",
                "fill",
                trusted_html("[Rust I/O] 从标准输入读取一行到 String 变量 guess 中：<pre>io::stdin()\n    .{{c1::read_line}}(&amp;mut guess)\n    .expect(\"Failed to read line\");</pre>"),
                "",
                "read_line",
                "read_line 将用户输入追加（append）到 String 末尾，不会覆盖原内容。返回 Result 类型。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "io", "read_line", "fill"],
        ),
        # ── RQ17 · & 引用 ──
        note(
            model,
            [
                "RQ17",
                "qa",
                "[Rust 引用] & 符号在 &mut guess 中表示什么？",
                "",
                "表示 guess 是以引用（reference）方式传递的，允许多处代码访问同一数据而无需拷贝。",
                "来源：TRPL §2。第四章详解。引用默认不可变（&guess），需要可变引用时用 &mut guess。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "reference", "borrowing", "qa"],
        ),
        # ── RF22 · & 和 &mut ──
        note(
            model,
            [
                "RF22",
                "fill",
                "[Rust 引用] 不可变引用：{{c1::&}}x；可变引用：{{c2::&mut}} x。",
                "",
                "&||&mut",
                "引用默认不可变，就像变量默认不可变一样。&mut 表示可以通过引用修改数据。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "reference", "mut", "fill", "multi-cloze"],
        ),
        # ── RQ18 · Result 枚举 ──
        note(
            model,
            [
                "RQ18",
                "qa",
                "[Rust 错误处理] read_line 方法返回的 Result 类型是什么？它有哪些成员（variant）？",
                "",
                "Result 是一个枚举类型，用于编码操作结果。两个成员：Ok——操作成功，内部包含成功值；Err——操作失败，内部包含错误信息。",
                "来源：TRPL §2。Result 是 Rust 错误处理的核心类型（第九章详解）。第六章详解枚举。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "result", "enum", "error-handling", "qa"],
        ),
        # ── RC05 · Result 成员 ──
        note(
            model,
            [
                "RC05",
                "choice",
                "[Rust 错误处理] 当 read_line 成功读取一行，返回的 Result 是哪个成员？",
                "Err，包含错误信息||Ok，包含读取的字节数||None||panic!",
                "2",
                "成功时返回 Ok，其中包含本次读取的字节数。失败时返回 Err（如操作系统 I/O 错误）。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "result", "enum", "choice"],
        ),
        # ── RQ19 · expect 方法 ──
        note(
            model,
            [
                "RQ19",
                "qa",
                "[Rust 错误处理] Result 上的 expect 方法做什么？",
                "",
                "如果 Result 是 Ok，返回其中的值；如果是 Err，使程序 panic（崩溃）并打印传入的错误消息。",
                "来源：TRPL §2。expect 是\"快速失败\"策略——开发阶段可接受，生产代码应做真正的错误处理（第九章）。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "expect", "panic", "error-handling", "qa"],
        ),
        # ── RC06 · 未处理 Result 警告 ──
        note(
            model,
            [
                "RC06",
                "choice",
                "[Rust 错误处理] 调用 read_line 但不使用其返回的 Result，会发生什么？",
                "编译错误（error）||编译通过但运行时崩溃||编译通过但有警告（warning），提示未处理可能的错误||没有任何提示",
                "3",
                "Rust 编译器会发出警告（warning），提醒 Result 可能表示错误被忽略。程序仍可运行，但不符合 Rust 的\"显式处理错误\"哲学。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "result", "warning", "choice"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.5 println! 占位符
        # ═══════════════════════════════════════════════════════════

        # ── RF23 · println 占位符两种写法 ──
        note(
            model,
            [
                "RF23",
                "fill",
                "[Rust 宏] println! 打印变量的两种写法：\n- 变量名直接放入占位符：println!(\"x = {{c1::{x}}}\");\n- 空占位符 + 参数列表：println!(\"x = {{c2::{}}}\", x);",
                "",
                "{x}||{}",
                "第一种：变量名写在大括号内。第二种：空大括号，后面按顺序提供表达式。两者可混用。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "println", "format", "fill", "multi-cloze"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.6 二进制 crate vs 库 crate
        # ═══════════════════════════════════════════════════════════

        # ── RQ20 · 两类 crate ──
        note(
            model,
            [
                "RQ20",
                "qa",
                "[Rust 生态] 二进制 crate（binary crate）和库 crate（library crate）的区别？",
                "",
                "二进制 crate：编译生成可执行文件，有 main 函数。库 crate：编译生成 .rlib 库文件，供其他程序使用，没有 main 函数，不能独立运行。",
                "来源：TRPL §2。例如：guessing_game 项目是二进制 crate；rand 是库 crate。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "crate", "binary", "library", "qa"],
        ),
        # ── RC07 · crate 类型判断 ──
        note(
            model,
            [
                "RC07",
                "choice",
                "[Rust 生态] 以下哪个是库 crate 的特征？",
                "有 main 函数||有 src/main.rs||能直接 ctrl-c 执行||不包含 main 函数，编译为 .rlib，供其他 crate 依赖",
                "4",
                "库 crate 没有 main，入口在 src/lib.rs（而非 main.rs），产物是 .rlib。二进制 crate 入口是 src/main.rs，产物是可执行文件。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "crate", "binary", "library", "choice"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.7 依赖管理：SemVer / Crates.io / Cargo.lock / cargo update
        # ═══════════════════════════════════════════════════════════

        # ── RQ21 · Crates.io ──
        note(
            model,
            [
                "RQ21",
                "qa",
                "[Rust 生态] Crates.io 是什么？",
                "",
                "Rust 生态系统的公共包注册中心（registry），供开发者发布和发现开源 Rust crate。",
                "来源：TRPL §2。Cargo 默认从 Crates.io 下载依赖。类似 npm registry（Node）或 PyPI（Python）。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "crates.io", "registry", "qa"],
        ),
        # ── RQ22 · SemVer ^ ──
        note(
            model,
            [
                "RQ22",
                "qa",
                "[Cargo] Cargo.toml 中写 rand = \"0.8.5\" 实际等价于什么版本范围？",
                "",
                "等价于 ^0.8.5，表示 >= 0.8.5 且 < 0.9.0。即兼容的次版本（minor）范围内取最新。",
                "来源：TRPL §2。SemVer 格式：主版本.次版本.补丁。^ 约束允许补丁和次版本更新，禁止主版本变更（因为主版本变更 = 不兼容 API）。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "semver", "cargo", "dependencies", "qa"],
        ),
        # ── RF24 · cargo update ──
        note(
            model,
            [
                "RF24",
                "fill",
                "[Cargo] 忽略 Cargo.lock，重新计算并更新依赖到 Cargo.toml 允许的最新版本：{{c1::cargo update}}。",
                "",
                "cargo update",
                "cargo update 只升级 SemVer 范围内的版本（如 0.8.5→0.8.6）。要跨主版本，需手动修改 Cargo.toml。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "cargo", "update", "fill"],
        ),
        # ── RC08 · Cargo.lock vs Cargo.toml ──
        note(
            model,
            [
                "RC08",
                "choice",
                "[Cargo] 关于 Cargo.toml 和 Cargo.lock，哪项错误？",
                "Cargo.toml 声明依赖范围，Cargo.lock 锁定精确版本||Cargo.lock 应提交到版本控制||如果要升级跨主版本的依赖，只需 cargo update||cargo update 只升级 SemVer 兼容范围内的版本",
                "3",
                "cargo update 只升级兼容范围内的版本。要跨主版本需手动修改 Cargo.toml 中的版本号。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "cargo", "lock", "toml", "choice"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.8 Rng trait & rand crate
        # ═══════════════════════════════════════════════════════════

        # ── RQ23 · trait 初步概念 ──
        note(
            model,
            [
                "RQ23",
                "qa",
                "[Rust trait] 在猜数字游戏中，use rand::Rng; 引入的 Rng 是什么？",
                "",
                "Rng 是一个 trait（特征），定义了随机数生成器应实现的方法（如 gen_range）。引入 trait 到作用域后才能调用这些方法。",
                "来源：TRPL §2。trait 类似其他语言的接口（interface），第十章详解。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "trait", "rng", "qa"],
        ),
        # ── RF25 · thread_rng + gen_range ──
        note(
            model,
            [
                "RF25",
                "fill",
                trusted_html("[Rust 随机数] 生成 1 到 100 之间的随机数：<pre>rand::{{c1::thread_rng}}().{{c2::gen_range}}(1..=100)</pre>"),
                "",
                "thread_rng||gen_range",
                "thread_rng() 返回线程局部、OS 提供种子的随机数生成器。gen_range 由 Rng trait 提供，1..=100 是闭区间范围表达式。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "rand", "random", "fill", "multi-cloze"],
        ),
        # ── RF26 · 范围表达式 ──
        note(
            model,
            [
                "RF26",
                "fill",
                "[Rust 语法] 闭区间范围（包含两端）：{{c1::1..=100}}。半开区间（不含右端）：{{c2::1..100}}。",
                "",
                "1..=100||1..100",
                "..= 包含右端点，.. 不包含右端点。gen_range 参数需匹配区间类型。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "range", "syntax", "fill", "multi-cloze"],
        ),
        # ── RF27 · cargo doc --open ──
        note(
            model,
            [
                "RF27",
                "fill",
                "[Cargo] 为所有依赖构建文档并在浏览器中打开：{{c1::cargo doc --open}}。",
                "",
                "cargo doc --open",
                "来源：TRPL §2。非常实用——可以离线浏览所有依赖的 API 文档。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "cargo", "doc", "fill"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.9 match & Ordering
        # ═══════════════════════════════════════════════════════════

        # ── RQ24 · Ordering 枚举 ──
        note(
            model,
            [
                "RQ24",
                "qa",
                "[Rust 控制流] std::cmp::Ordering 枚举的三个成员是什么？",
                "",
                "Less（小于）、Greater（大于）、Equal（等于）。",
                "来源：TRPL §2。cmp 方法比较两个值后返回 Ordering 枚举，配合 match 使用。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "ordering", "cmp", "enum", "qa"],
        ),
        # ── RQ25 · match 表达式 ──
        note(
            model,
            [
                "RQ25",
                "qa",
                "[Rust 控制流] match 表达式如何工作？",
                "",
                "match 将值与一系列分支（arm）的模式逐一比较。第一个匹配的分支被执行，match 随即结束。match 是穷尽的——必须覆盖所有可能情况。",
                "来源：TRPL §2。类似其他语言的 switch，但更强大：支持模式匹配、保证穷尽性。第六章和第十九章详解。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "match", "control-flow", "qa"],
        ),
        # ── RF28 · match 语法 ──
        note(
            model,
            [
                "RF28",
                "fill",
                trusted_html("[Rust 控制流] 用 match 处理比较结果：<pre>match guess.cmp(&amp;secret_number) {\n    {{c1::Ordering\\::Less}} => println!(\"Too small!\"),\n    Ordering::Greater => println!(\"Too big!\"),\n    {{c2::Ordering\\::Equal}} => println!(\"You win!\"),\n}</pre>"),
                "",
                "Ordering::Less||Ordering::Equal",
                "每个分支 = 模式 => 表达式。模式来自 Ordering 枚举的三个 variant。match 保证三种情况都被处理。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "match", "ordering", "fill", "multi-cloze"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.10 类型系统：推断 / 注解 / shadowing
        # ═══════════════════════════════════════════════════════════

        # ── RQ26 · 类型推断与默认数值类型 ──
        note(
            model,
            [
                "RQ26",
                "qa",
                "[Rust 类型系统] 如果不加类型注解，Rust 中整数默认是什么类型？",
                "",
                "默认是 i32（32 位有符号整数）。",
                "来源：TRPL §2。Rust 有静态强类型 + 类型推断，多数情况无需手动标注。但比较 String 和 i32 时会报\"类型不匹配\"编译错误。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "type-inference", "i32", "default", "qa"],
        ),
        # ── RQ27 · Shadowing ──
        note(
            model,
            [
                "RQ27",
                "qa",
                "[Rust 变量] 什么是变量遮蔽（shadowing）？",
                "",
                "用 let 重新声明一个同名变量，新变量会\"遮蔽\"旧变量。此后该名称指向新变量。常用于类型转换。",
                "来源：TRPL §2。例如 let guess: u32 = guess.trim().parse().expect(...); 将 String 类型的 guess 转换为 u32 类型，复用变量名。第三章详解。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "shadowing", "let", "variable", "qa"],
        ),
        # ── RC09 · shadowing vs mut ──
        note(
            model,
            [
                "RC09",
                "choice",
                "[Rust 变量] shadowing 和 mut 的区别是？",
                "两者完全一样||shadowing 改变值但保持类型不变；mut 可以改变值也可以改变类型||mut 改变值但保持类型不变；shadowing 可以用 let 重新声明，类型可以改变||shadowing 不需要 let 关键字",
                "3",
                "mut：变量本身可变（x = 6），但类型固定。shadowing：用 let 重新声明（let x = 6），可以改变类型（如 String→u32）。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "shadowing", "mut", "choice"],
        ),
        # ── RF29 · trim + parse ──
        note(
            model,
            [
                "RF29",
                "fill",
                trusted_html("[Rust 类型转换] 将用户输入的字符串转换为 u32 并处理换行符：<pre>let guess: u32 = guess.{{c1::trim()}}.{{c2::parse()}}.expect(\"Please type a number!\");</pre>"),
                "",
                "trim()||parse()",
                "trim() 去除首尾空白（包括 read_line 追加的 \\n）。parse() 将字符串解析为数，返回 Result 类型。类型注解 : u32 告诉 parse 目标类型。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "trim", "parse", "type-conversion", "fill", "multi-cloze"],
        ),
        # ── RF30 · u32 类型注解 ──
        note(
            model,
            [
                "RF30",
                "fill",
                trusted_html("[Rust 类型系统] 声明 guess 为无符号 32 位整数类型：<pre>let guess: {{c1::u32}}</pre>"),
                "",
                "u32",
                "u32 = unsigned 32-bit integer。冒号 : 后跟类型注解。正整数场景的好默认选择。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "u32", "type-annotation", "fill"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.11 循环：loop / break / continue
        # ═══════════════════════════════════════════════════════════

        # ── RQ28 · loop 关键字 ──
        note(
            model,
            [
                "RQ28",
                "qa",
                "[Rust 控制流] loop 关键字创建什么？",
                "",
                "创建一个无限循环，反复执行循环体直到显式退出（break 或 panic）。",
                "来源：TRPL §2。Rust 有三种循环：loop（无限）、while（条件）、for（迭代）。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "loop", "control-flow", "qa"],
        ),
        # ── RF31 · break ──
        note(
            model,
            [
                "RF31",
                "fill",
                "[Rust 控制流] 在 loop 循环中，退出循环用 {{c1::break}}。",
                "",
                "break",
                "来源：TRPL §2「猜测正确后退出」。loop 没有自带退出条件，需要 break 显式退出。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "break", "loop", "fill"],
        ),
        # ── RF32 · continue ──
        note(
            model,
            [
                "RF32",
                "fill",
                "[Rust 控制流] 在 loop 循环中，跳过当前迭代直接进入下一轮用 {{c1::continue}}。",
                "",
                "continue",
                "来源：TRPL §2「处理无效输入」。continue 跳过本次循环的剩余代码，立即开始下一次迭代。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "continue", "loop", "fill"],
        ),
        # ── RC10 · loop/break/continue 辨析 ──
        note(
            model,
            [
                "RC10",
                "choice",
                "[Rust 控制流] 猜数字游戏中，match 到了 Err(_) 分支执行 continue。以下哪项描述最准确？",
                "程序立即停止运行||程序退出当前 loop 循环||程序跳过本次循环剩余代码，回到 loop 开头请求新输入||程序 panic",
                "3",
                "continue 不退出循环（区别于 break），不终止程序（区别于 panic），只是跳到下一次迭代。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "continue", "loop", "match", "choice"],
        ),
        # ── RQ29 · match 通配符 _ ──
        note(
            model,
            [
                "RQ29",
                "qa",
                "[Rust 控制流] match 分支中的 Err(_) 的 _ 表示什么？",
                "",
                "下划线 _ 是通配模式（catch-all），匹配所有 Err 值，但不绑定其中的具体错误信息。",
                "来源：TRPL §2。相当于\"不管是什么错误，都走这个分支\"。区别于 Err(e) 会把错误绑定到变量 e。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "match", "wildcard", "pattern", "qa"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §2.12 综合辨析卡
        # ═══════════════════════════════════════════════════════════

        # ── RC11 · let vs let mut vs shadowing ──
        note(
            model,
            [
                "RC11",
                "choice",
                "[Rust 变量] 以下代码中，最终 x 的值是多少？（提示：关注 shadowing）\nlet x = 5;\nlet x = x + 1;\n{\n    let x = x * 2;\n    println!(\"inner: {x}\");\n}\nprintln!(\"outer: {x}\");",
                "inner: 12, outer: 12||inner: 6, outer: 6||inner: 12, outer: 6||inner: 6, outer: 12",
                "3",
                "第一行 x=5。第二行 shadowing：x=6。花括号内创建新作用域，内部 shadowing：x=12（仅在花括号内）。离开花括号后，内部的 shadow 失效，恢复为 6。",
                "",
                "",
                "",
            ],
            ["ch2", "rust", "shadowing", "scope", "let", "choice"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "Rust TRPL · 第二章：猜数字游戏", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
