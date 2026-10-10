from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck, trusted_html

DECK_ID = 2059400751
OUTPUT = ROOT / "anki-Rust-第五章-结构体.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════════════════════════════════════════════════════
        # §5.1 结构体定义和实例化
        # ═══════════════════════════════════════════════════════════

        # ── RF47 · struct 定义语法 ──
        note(
            model,
            [
                "RF47",
                "fill",
                trusted_html("[Rust 结构体] 定义一个 User 结构体：<br><pre>struct User {\n    {{c1::username}}: String,\n    {{c2::email}}: String,\n    {{c3::active}}: bool,\n    {{c4::sign_in_count}}: u64,\n}</pre>"),
                "",
                "username||email||active||sign_in_count",
                "来源：TRPL §5.1 示例 5-1。struct 关键字 + 结构体名 + { 字段名: 类型, ... }。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "struct", "definition", "fill", "multi-cloze"],
        ),
        # ── RF48 · 字段访问 ──
        note(
            model,
            [
                "RF48",
                "fill",
                trusted_html("[Rust 结构体] 访问 User 实例 user1 的 email 字段：<br><pre>let e = user1{{c1::.email}};</pre>"),
                "",
                ".email",
                "来源：TRPL §5.1 示例 5-2。instance.field 访问结构体字段。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "struct", "field-access", "fill"],
        ),
        # ── RQ72 · 整个实例必须可变 ──
        note(
            model,
            [
                "RQ72",
                "qa",
                "[Rust 结构体] 想修改 user1.email，user1 必须怎么声明？能只把 email 字段标为可变吗？",
                "",
                "user1 必须声明为 let mut user1 = ...;（整个实例可变）。Rust 不允许只标记单个字段为 mut——要么整个实例可变，要么整个不可变。",
                "来源：TRPL §5.1 第 37 行。Rust 可变性粒度是整个变量，struct 实例是一个变量。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "struct", "mutability", "qa"],
        ),
        # ── RF49 · 字段初始化简写 ──
        note(
            model,
            [
                "RF49",
                "fill",
                trusted_html("[Rust 结构体] 函数参数名与结构体字段名相同时的简写：<br><pre>fn build_user(email: String, username: String) -> User {\n    User {\n        active: true,\n        sign_in_count: 1,\n        {{c1::email}},   // 等价于 email: email\n        {{c2::username}}, // 等价于 username: username\n    }\n}</pre>"),
                "",
                "email||username",
                "来源：TRPL §5.1 示例 5-5。简称 field init shorthand。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "struct", "shorthand", "fill", "multi-cloze"],
        ),
        # ── RF50 · 结构体更新语法 ──
        note(
            model,
            [
                "RF50",
                "fill",
                trusted_html("[Rust 结构体] 用 user1 创建 user2，只改 email：<br><pre>let user2 = User {\n    email: String::from(\"new@...\"),\n    {{c1::..user1}}\n};</pre>"),
                "",
                "..user1",
                "来源：TRPL §5.1 示例 5-7。..old_instance = 其余字段照抄。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "struct", "update-syntax", "fill"],
        ),
        # ── RQ73 · 更新语法所有权影响 ──
        note(
            model,
            [
                "RQ73",
                "qa",
                "[Rust 结构体] let user2 = User { email: ..., ..user1 }; 之后 user1 还能用吗？",
                "",
                "取决于 ..user1 移动了哪些字段。非 Copy 字段（如 username: String）被 move 到 user2，user1 整体失效。如果复用的字段全是 Copy 类型（如只用了 active: bool 和 sign_in_count: u64），user1 仍有效。",
                "来源：TRPL §5.1 第 93-95 行。结构更新语法 = 逐字段赋值 = 服从 move/copy 规则。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "struct", "update-syntax", "move", "qa"],
        ),
        # ── RQ74 · 元组结构体定义 ──
        note(
            model,
            [
                "RQ74",
                "qa",
                trusted_html("[Rust 结构体] 下面定义的是什么？如何访问字段？<br><pre>struct Color(i32, i32, i32);</pre>"),
                "",
                "元组结构体（tuple struct）。有类型名 Color，字段没有名字只有类型。通过索引访问：let c = Color(0, 0, 0); let red = c.0;",
                "来源：TRPL §5.1。struct Name(T1, T2, ...); 定义，用 .0 .1 访问。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "tuple-struct", "qa"],
        ),
        # ── RQ75 · 元组结构体 vs 普通结构体 ──
        note(
            model,
            [
                "RQ75",
                "qa",
                "[Rust 结构体] struct Point(i32, i32);（元组结构体）和 struct Point { x: i32, y: i32 }（普通结构体）在使用上有什么区别？",
                "",
                "元组结构体用索引访问（p.0, p.1），普通结构体用字段名访问（p.x, p.y）。字段名比索引更清晰。",
                "来源：TRPL §5.1。核心区别：有没有字段名。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "tuple-struct", "comparison", "qa"],
        ),
        # ── RQ76 · 元组结构体类型独立 ──
        note(
            model,
            [
                "RQ76",
                "qa",
                "[Rust 结构体] struct Color(i32, i32, i32); 和 struct Point(i32, i32, i32); 字段类型完全相同，能互相赋值吗？",
                "",
                "不能。Color 和 Point 是不同的类型，即使字段类型相同。接收 Color 的函数不接受 Point。",
                "来源：TRPL §5.1 第 111 行。每一个结构体有其自己的类型。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "tuple-struct", "type-system", "qa"],
        ),
        # ── RQ77 · 类单元结构体 ──
        note(
            model,
            [
                "RQ77",
                "qa",
                "[Rust 结构体] struct AlwaysEqual; 定义了什么？什么时候用？",
                "",
                "类单元结构体（unit-like struct）——没有任何字段。用于想在某个类型上实现 trait，但不需要存储数据时。",
                "来源：TRPL §5.1「定义类单元结构体」。struct Name; 定义，实例化写 let x = Name;",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "unit-like-struct", "qa"],
        ),
        # ── RQ78 · String vs &str 设计选择 ──
        note(
            model,
            [
                "RQ78",
                "qa",
                "[Rust 结构体] 定义结构体时，字段通常用 String 而不是 &str。为什么不直接用 &str 引用？",
                "",
                "用 &str（引用）编译器会要求标注生命周期（第十章）。用 String（拥有所有权的类型）无需生命周期标注——结构体自己拥有数据，结构体有效则数据有效。",
                "来源：TRPL §5.1「结构体数据的所有权」。初学者优先用 String，学会生命周期后再考虑 &str。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "struct", "ownership", "lifetime", "qa"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §5.2 示例程序 & Debug trait
        # ═══════════════════════════════════════════════════════════

        # ── RQ79 · 结构体 vs 元组动机 ──
        note(
            model,
            [
                "RQ79",
                "qa",
                "[Rust 结构体·动机] 用元组 (u32, u32) 表示矩形的宽高，和用结构体 Rectangle { width: u32, height: u32 } 相比，后者有什么优势？",
                "",
                "结构体的字段有名称——rect.width 比 rect.0 更清晰地表达了意图。元组依赖索引顺序，容易混淆宽和高。结构体自文档化。",
                "来源：TRPL §5.2。数据有关联 → 元组能打包但不命名 → 结构体命名字段 → 代码自解释。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "struct", "motivation", "qa"],
        ),
        # ── RQ80 · Display 报错原因 ──
        note(
            model,
            [
                "RQ80",
                "qa",
                "[Rust 结构体] println!(\"{}\", rect) 对自定义结构体报错。为什么？",
                "",
                "println!(\"{}\") 要求类型实现 Display trait（给终端用户的显示格式）。自定义结构体默认没有实现 Display——因为结构体有很多种可能的显示方式，Rust 不替你做选择。",
                "来源：TRPL §5.2「通过派生 trait 增加功能」。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "struct", "display", "qa"],
        ),
        # ── RQ81 · #[derive(Debug)] 解决方案 ──
        note(
            model,
            [
                "RQ81",
                "qa",
                "[Rust 结构体] 想让自定义结构体能用 println! 打印调试信息，需要加什么？用什么占位符？",
                "",
                "结构体定义前加 #[derive(Debug)]，然后用 {:?}（紧凑）或 {:#?}（带缩进的多行 pretty-print）。",
                "来源：TRPL §5.2 示例 5-12。derive 自动生成 Debug trait 实现。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "derive", "debug", "qa"],
        ),
        # ── RF51 · dbg! 文件行号 + stderr ──
        note(
            model,
            [
                "RF51",
                "fill",
                trusted_html("[Rust 结构体] dbg! 宏输出的两个特点：<br>- 打印{{c1::文件和行号}}（文件名:行号）和表达式结果<br>- 输出到{{c2::stderr}}（不是 stdout）"),
                "",
                "文件和行号||stderr",
                "来源：TRPL §5.2。dbg! 输出含位置信息方便定位，输出到 stderr 与正常输出分离。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "dbg", "stderr", "fill", "multi-cloze"],
        ),
        # ── RQ82 · dbg! 所有权处理 ──
        note(
            model,
            [
                "RQ82",
                "qa",
                "[Rust 结构体] dbg!(expr) 对 expr 做了什么所有权处理？如果不想转移所有权怎么办？",
                "",
                "dbg! 拿走表达式的所有权，打印后返回该值。不想转移所有权就传引用：dbg!(&rect)。",
                "来源：TRPL §5.2。dbg! 拿走所有权 → 打印 → 返回 → 可链式使用。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "dbg", "ownership", "qa"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §5.3 方法语法
        # ═══════════════════════════════════════════════════════════

        # ── RQ83 · impl 块定义 ──
        note(
            model,
            [
                "RQ83",
                "qa",
                "[Rust 方法] impl Rectangle { ... } 中的 impl 是什么？",
                "",
                "impl 是 implementation 块。其中的函数与 Rectangle 类型关联。是给类型添加方法和关联函数的语法。",
                "来源：TRPL §5.3。impl 是 implementation 的缩写。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "impl", "method", "qa"],
        ),
        # ── RQ84 · 方法 vs 函数调用区别 ──
        note(
            model,
            [
                "RQ84",
                "qa",
                "[Rust 方法] fn area(&self)（方法）和 fn area(rect: &Rectangle)（普通函数），在调用方式上的区别是什么？",
                "",
                "方法：rect.area()——实例在前，编译器自动把实例传给 self。普通函数：area(&rect)——显式传参。",
                "来源：TRPL §5.3 示例 5-13。方法放进 impl，第一个参数改 &self，调用用 .method()。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "method", "function", "comparison", "qa"],
        ),
        # ── RQ85 · impl 组织性好处 ──
        note(
            model,
            [
                "RQ85",
                "qa",
                "[Rust 方法] 把 area 写成方法放进 impl Rectangle，而不是写成独立函数，在代码组织上有什么好处？",
                "",
                "与 Rectangle 相关的功能集中在一个 impl 块中——使用者不需要到处找这个类型有哪些可用操作。",
                "来源：TRPL §5.3 第 27 行。组织性是可维护性的基础。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "impl", "organization", "qa"],
        ),
        # ── RF52 · &self ──
        note(
            model,
            [
                "RF52",
                "fill",
                "[Rust 方法] 方法只需读取实例数据、不修改时，第一个参数写 {{c1::&self}}。这是最常用的形式。",
                "",
                "&self",
                "来源：TRPL §5.3。&self 是 self: &Self 的缩写 = 不可变借用。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "method", "self", "fill"],
        ),
        # ── RF53 · &mut self ──
        note(
            model,
            [
                "RF53",
                "fill",
                "[Rust 方法] 方法需要修改实例的数据时，第一个参数写 {{c1::&mut self}}。",
                "",
                "&mut self",
                "来源：TRPL §5.3。&mut self = 可变借用。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "method", "mut-self", "fill"],
        ),
        # ── RQ86 · self 获取所有权 ──
        note(
            model,
            [
                "RQ86",
                "qa",
                "[Rust 方法] 方法的第一个参数写 self（不带 &）意味着什么？为什么很少用？",
                "",
                "方法获取实例的所有权。调用后原实例不能再使用（被 move 进方法了）。很少用——只在方法需要将 self 转换为其他类型时使用，防止调用者之后误用原实例。",
                "来源：TRPL §5.3 第 25 行。self 对应 move 语义。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "method", "self-ownership", "qa"],
        ),
        # ── RQ87 · 自动引用和解引用 ──
        note(
            model,
            [
                "RQ87",
                "qa",
                "[Rust 方法] p1.distance(&p2) 和 (&p1).distance(&p2) 都能工作。Rust 在方法调用时做了什么让前者也合法？",
                "",
                "Rust 有自动引用和解引用（automatic referencing and dereferencing）。方法调用时，编译器自动为调用者添加 &、&mut 或 *，使调用者类型与方法签名的 self 类型匹配。这就是 Rust 没有 C++ 的 -> 运算符的原因。",
                "来源：TRPL §5.3「-> 运算符到哪去了？」。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "method", "auto-ref", "qa"],
        ),
        # ── RQ88 · 关联函数（非方法）──
        note(
            model,
            [
                "RQ88",
                "qa",
                "[Rust 方法] impl 块中不以 self 为第一参数的函数叫什么？如何调用？典型用途？",
                "",
                "叫关联函数（associated function，非方法）。用 Type::function() 调用（:: 语法）。典型用途：构造函数——如 String::new()、Rectangle::square(size)。",
                "来源：TRPL §5.3「关联函数」。有 self = 方法（用 .）；无 self = 关联函数（用 ::）。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "associated-function", "impl", "qa"],
        ),
        # ── RQ89 · 多个 impl 块 ──
        note(
            model,
            [
                "RQ89",
                "qa",
                "[Rust 方法] 一个结构体可以有多个 impl 块吗？",
                "",
                "可以。impl Rectangle { ... } 写多个完全合法。这在泛型和 trait 实现时尤其有用（第十章）。",
                "来源：TRPL §5.3 第 121-129 行。",
                "",
                "",
                "",
            ],
            ["ch5", "rust", "impl", "multiple", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "Rust TRPL · 第五章：结构体", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
