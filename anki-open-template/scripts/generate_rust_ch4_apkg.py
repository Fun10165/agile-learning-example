from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck, trusted_html

DECK_ID = 2059400741
OUTPUT = ROOT / "anki-Rust-第四章-所有权.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════════════════════════════════════════════════════
        # 前置动机 & 栈与堆
        # ═══════════════════════════════════════════════════════════

        # ── RQ49 · 三种内存管理策略 ──
        note(
            model,
            [
                "RQ49",
                "qa",
                "[Rust 所有权·动机] 编程语言管理堆内存的三种策略是什么？Rust 选择了哪种？",
                "",
                "1. 垃圾回收（GC）：运行时自动寻找和释放不再使用的内存（如 Java、Go）。\n2. 手动管理：程序员显式分配和释放（如 C 的 malloc/free）。\n3. 所有权系统：编译器在编译时通过规则自动插入释放代码——无需 GC 也无需手动 free。Rust 选择了第三种。",
                "来源：TRPL §4.1。所有权 = 零运行时开销 + 内存安全，不需要 GC 的停顿。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "ownership", "motivation", "qa"],
        ),
        # ── RQ50 · 栈与堆对比 ──
        note(
            model,
            [
                "RQ50",
                "qa",
                "[Rust 所有权·内存] 栈（stack）和堆（heap）的核心区别是什么？什么数据放栈上，什么放堆上？",
                "",
                "栈：LIFO（后进先出），数据必须大小已知且固定。入栈/出栈极快，无需搜索空闲空间。编译时大小确定的类型（如 i32、bool）放栈上。\n堆：大小未知或可变的数据。分配时需搜索足够大的空闲空间，返回指针（指针本身存栈上）。访问堆数据需通过指针间接访问，较慢。\n所有权系统主要管理堆数据。",
                "来源：TRPL §4.1「栈与堆」提示框。理解栈和堆是理解 move/copy/clone 的前提。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "stack", "heap", "memory", "qa"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §4.1 所有权规则
        # ═══════════════════════════════════════════════════════════

        # ── RF42 · 所有权三规则 ──
        note(
            model,
            [
                "RF42",
                "fill",
                trusted_html("[Rust 所有权] 所有权的三条规则：<br>1. Rust 中每一个值都有一个{{c1::所有者（owner）}}。<br>2. 值在任一时刻有且只有{{c2::一}}个所有者。<br>3. 当所有者离开{{c3::作用域}}，这个值将被丢弃（调用 drop）。"),
                "",
                "所有者（owner）||一||作用域",
                "来源：TRPL §4.1。这三条是所有 move/copy/clone/borrow 行为的公理。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "ownership", "rules", "fill", "multi-cloze"],
        ),
        # ── RQ51 · String 内存结构 ──
        note(
            model,
            [
                "RQ51",
                "qa",
                "[Rust 所有权] String 类型在内存中由哪三部分组成？它们分别放在栈上还是堆上？",
                "",
                "三部分：指针（指向堆上的字符串内容）、长度（当前用了多少字节）、容量（总共分配了多少字节）。全部在栈上。实际字符串内容在堆上。",
                "来源：TRPL §4.1 图 4-1。String 不是\"一个值\"而是\"栈上元数据 + 堆上内容\"。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "string", "memory", "stack", "heap", "qa"],
        ),
        # ── RQ52 · Move 语义 ──
        note(
            model,
            [
                "RQ52",
                "qa",
                "[Rust 所有权] let s2 = s1;（s1 是 String）之后，s1 还能用吗？为什么？",
                "",
                "不能。s1 的栈上数据（指针、长度、容量）被移动（move）到了 s2，Rust 标记 s1 为无效。这防止了 s1 和 s2 离开作用域时同时对同一块堆内存调用 drop（二次释放 / double free）。",
                "来源：TRPL §4.1「使用移动的变量与数据交互」。Move 是 Rust 所有权系统最可见的行为。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "move", "ownership", "double-free", "qa"],
        ),
        # ── RQ53 · Move vs 浅拷贝 ──
        note(
            model,
            [
                "RQ53",
                "qa",
                "[Rust 所有权] Rust 的 move（s2 = s1 后 s1 失效）和传统语言的浅拷贝（shallow copy）有什么本质区别？",
                "",
                "浅拷贝只复制栈数据，两个变量都有效，都指向同一堆数据——存在 double free 风险。Rust 的 move 在复制栈数据后使原变量失效——所以 move 不是浅拷贝。",
                "来源：TRPL §4.1。Rust 永远不自动创建数据的深拷贝。任何自动复制都可以认为对运行时性能影响较小。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "move", "shallow-copy", "qa"],
        ),
        # ── RF43 · Clone ──
        note(
            model,
            [
                "RF43",
                "fill",
                trusted_html("[Rust 所有权] 如果确实需要深度复制 String 的堆数据，应该用 {{c1::clone()}} 方法：<br>let s2 = s1.{{c1::clone()}};  // s1 和 s2 各自独立"),
                "",
                "clone()",
                "来源：TRPL §4.1。clone 显式深拷贝，调用处一眼可见有开销。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "clone", "deep-copy", "fill"],
        ),
        # ── RQ54 · Copy trait 概念 ──
        note(
            model,
            [
                "RQ54",
                "qa",
                "[Rust 所有权] let y = x; 其中 x 是 i32，之后 x 还能用。这和 String 的 move 行为为什么不同？",
                "",
                "i32 等类型实现了 Copy trait。这些类型的值整个存储在栈上，复制时直接拷贝全部数据，不存在\"两个变量共享堆内存\"的问题。因此不需要 move——原变量保持有效。",
                "来源：TRPL §4.1「只在栈上的数据：拷贝」。Copy 类型：简单标量值的组合，不需要分配内存或管理资源。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "copy", "trait", "stack", "qa"],
        ),
        # ── RF44 · Copy 类型枚举 ──
        note(
            model,
            [
                "RF44",
                "fill",
                trusted_html("[Rust 所有权] 哪些类型实现了 Copy？（填是/否）<br>所有整数类型：{{c1::是}} &nbsp; bool：{{c2::是}} &nbsp; 所有浮点类型：{{c3::是}}<br>char：{{c4::是}} &nbsp; String：{{c5::否}}<br>(i32, i32) 元组：{{c6::是}} &nbsp; (i32, String) 元组：{{c7::否}}"),
                "",
                "是||是||是||是||否||是||否",
                "来源：TRPL §4.1。通用规则：简单标量组合 → Copy；需要分配内存或含非 Copy 类型 → 非 Copy。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "copy", "types", "fill", "multi-cloze"],
        ),
        # ── RQ55 · Copy 和 Drop 互斥 ──
        note(
            model,
            [
                "RQ55",
                "qa",
                "[Rust 所有权] 一个类型能同时实现 Copy 和 Drop 吗？为什么？",
                "",
                "不能。Rust 禁止。Copy 意味着\"简单复制栈数据即可\"，Drop 意味着\"离开作用域时需要特殊清理\"。两者语义冲突——如果允许，drop 该对哪个副本执行？",
                "来源：TRPL §4.1。Rust 不允许自身或其任何部分实现了 Drop trait 的类型使用 Copy trait。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "copy", "drop", "exclusive", "qa"],
        ),
        # ── RQ56 · 传参 = move 或 copy ──
        note(
            model,
            [
                "RQ56",
                "qa",
                "[Rust 所有权] 把一个 String 传给函数后，调用方还能继续使用它吗？把 i32 传进去呢？",
                "",
                "String 传进去后不能继续使用——所有权被 move 进函数了。i32 传进去后还能用——i32 是 Copy 类型，传参时自动复制。规则和变量赋值完全一致。",
                "来源：TRPL §4.1 示例 4-3。给函数传值相当于赋值给函数的参数变量。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "function", "move", "copy", "ownership", "qa"],
        ),
        # ── RQ57 · 返回值转移所有权 ──
        note(
            model,
            [
                "RQ57",
                "qa",
                "[Rust 所有权] 函数返回一个 String 时，所有权发生了什么？",
                "",
                "所有权从函数内部转移（move）到调用方。例如 let s = gives_ownership(); 将返回值移动到 s。",
                "来源：TRPL §4.1 示例 4-4。返回值的所有权规律与赋值一致——从函数体内 move 出。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "return", "move", "ownership", "qa"],
        ),
        # ── RQ58 · 赋值替换立即 drop ──
        note(
            model,
            [
                "RQ58",
                "qa",
                "[Rust 所有权] let mut s = String::from(\"hello\"); s = String::from(\"ahoy\"); 第一行的 \"hello\" 何时被释放？",
                "",
                "在 s = String::from(\"ahoy\"); 这一行立即释放。给已有变量赋全新值时，Rust 会立刻 drop 原来的值。",
                "来源：TRPL §4.1「作用域与赋值」。不等作用域结束才释放——赋值替换时立即释放旧值。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "drop", "reassignment", "ownership", "qa"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §4.2 引用与借用
        # ═══════════════════════════════════════════════════════════

        # ── RQ59 · 引用 & 概念 ──
        note(
            model,
            [
                "RQ59",
                "qa",
                "[Rust 引用] &s1 创建了什么？&s1 拥有 s1 的所有权吗？",
                "",
                "创建了一个指向 s1 的引用（reference）。不拥有所有权——引用只是\"借用\"数据。引用离开作用域时，它指向的值不会被 drop。",
                "来源：TRPL §4.2。引用 = 给你\"访问权\"但不给你\"所有权\"。这就是借用（borrowing）。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "reference", "borrowing", "ownership", "qa"],
        ),
        # ── RQ60 · 借用术语 ──
        note(
            model,
            [
                "RQ60",
                "qa",
                "[Rust 引用] 在 Rust 术语中，\"借用（borrowing）\"是什么意思？",
                "",
                "通过引用（&）访问某个值而不获取其所有权的行为。就像借东西——用完之后要\"还\"，但东西的所有权始终在出借人那里。",
                "来源：TRPL §4.2。创建一个引用的行为称为借用。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "borrowing", "reference", "qa"],
        ),
        # ── RQ61 · 可变引用 &mut ──
        note(
            model,
            [
                "RQ61",
                "qa",
                "[Rust 引用] 要通过引用修改被指向的值，需要用哪种引用？创建它需满足什么前提？",
                "",
                "需要可变引用 &mut。前提：原变量必须声明为 mut（let mut s = ...），且创建时写 &mut s。",
                "来源：TRPL §4.2「可变引用」。引用默认不可变——就像变量默认不可变一样。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "mutable-reference", "mut", "qa"],
        ),
        # ── RQ62 · 可变引用排他性 ──
        note(
            model,
            [
                "RQ62",
                "qa",
                "[Rust 引用] 在同一作用域内，同一时间对一个变量最多能有几个可变引用？为什么这样限制？",
                "",
                "最多一个可变引用。目的：防止数据竞争（data race）——两个指针同时访问同一数据、至少一个在写、无同步机制。Rust 在编译时就杜绝了这种 bug。",
                "来源：TRPL §4.2。数据竞争会导致未定义行为，难以在运行时追踪和修复。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "mutable-reference", "exclusive", "data-race", "qa"],
        ),
        # ── RQ63 · 不可变 + 可变互斥 ──
        note(
            model,
            [
                "RQ63",
                "qa",
                "[Rust 引用] 在同一作用域内，能同时持有不可变引用和可变引用吗？多个不可变引用呢？",
                "",
                "不能同时持有不可变引用和可变引用。但可以同时持有多个不可变引用（都只读，不会有数据竞争）。",
                "来源：TRPL §4.2。不可变引用的借用者不希望在借用时值会突然被改变。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "immutable-reference", "mutable-reference", "mutual-exclusion", "qa"],
        ),
        # ── RQ64 · NLL 引用作用域 ──
        note(
            model,
            [
                "RQ64",
                "qa",
                "[Rust 引用] 一个引用的作用域从声明处到哪结束？与变量的作用域规则有什么不同？",
                "",
                "引用作用域从声明处到最后一次使用为止（不是到花括号 } 结束）。编译器可以提前结束不再使用的引用的作用域——这就是非词法作用域生命周期（NLL）。",
                "来源：TRPL §4.2。NLL 让更多合法代码能通过编译。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "nll", "reference", "scope", "qa"],
        ),
        # ── RQ65 · 悬垂引用 ──
        note(
            model,
            [
                "RQ65",
                "qa",
                "[Rust 引用] 什么是悬垂引用（dangling reference）？Rust 如何处理？",
                "",
                "悬垂引用：指向已被释放内存的引用。Rust 编译器在编译时就阻止悬垂引用的产生——如果函数试图返回一个局部变量的引用，编译直接报错。",
                "来源：TRPL §4.2「悬垂引用」。解决方法：直接返回 String 而非 &String——所有权被 move 出去。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "dangling-reference", "lifetime", "compile-error", "qa"],
        ),
        # ── RF45 · 引用两条总规则 ──
        note(
            model,
            [
                "RF45",
                "fill",
                trusted_html("[Rust 引用] 引用的两条总规则：<br>1. 在任意给定时间，要么只能有{{c1::一}}个可变引用，要么只能有{{c2::多个}}不可变引用。<br>2. 引用必须总是{{c3::有效的（valid）}}。"),
                "",
                "一||多个||有效的（valid）",
                "来源：TRPL §4.2。规则1 = 读写互斥（防数据竞争）；规则2 = 无悬垂引用（内存安全）。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "reference", "rules", "fill", "multi-cloze"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §4.3 Slice
        # ═══════════════════════════════════════════════════════════

        # ── RQ66 · Slice 概念 ──
        note(
            model,
            [
                "RQ66",
                "qa",
                "[Rust Slice] 什么是切片（slice）？它拥有所有权吗？",
                "",
                "切片是对集合中一段连续元素的引用，而不是对整个集合的引用。不拥有所有权——slice 本身也是一种引用。",
                "来源：TRPL §4.3。slice 存储了指向起始位置的指针和长度。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "slice", "reference", "qa"],
        ),
        # ── RQ67 · 为什么需要 Slice ──
        note(
            model,
            [
                "RQ67",
                "qa",
                "[Rust Slice·动机] 不用 slice 时，如果从函数返回\"字符串第一个单词\"的 usize 索引，有什么问题？",
                "",
                "索引与原始字符串脱钩——字符串被 clear() 清空后，索引仍然是一个独立的数字（如 5），用它切片会得到错误结果，编译器不报错。Slice 把引用和数据生命周期绑定，编译器能检测出持有引用后修改原字符串的错误。",
                "来源：TRPL §4.3 示例 4-7/4-8。slice 让 bug 在编译时暴露。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "slice", "motivation", "index", "safety", "qa"],
        ),
        # ── RF46 · 字符串 slice 语法 ──
        note(
            model,
            [
                "RF46",
                "fill",
                trusted_html("[Rust Slice] 字符串 slice 各种写法（设 s = \"hello world\"）：<br>&s[0..5] → \"hello\"<br>&s[..5] 等价于 &s[{{c1::0..5}}] —— 从开头<br>&s[6..] 等价于 &s[6..{{c2::len}}] —— 到结尾<br>&s[..] 等价于 &s[0..{{c3::len}}] —— 整个字符串"),
                "",
                "0..5||len||len",
                "来源：TRPL §4.3。.. range 语法——省略起点 = 0，省略终点 = 长度。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "slice", "syntax", "range", "fill", "multi-cloze"],
        ),
        # ── RQ68 · &str 类型 ──
        note(
            model,
            [
                "RQ68",
                "qa",
                "[Rust Slice] 字符串 slice 的类型叫什么？它和 String 是什么关系？",
                "",
                "类型写作 &str（读作\"string slice\"）。&str 是对 String（或字符串字面值）的一部分或全部的不可变引用。String 拥有数据，&str 借用数据。",
                "来源：TRPL §4.3。&str 是引用，不拥有数据——离开作用域不会释放 String 的堆内存。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "&str", "string", "slice", "qa"],
        ),
        # ── RQ69 · 字符串字面值就是 &str ──
        note(
            model,
            [
                "RQ69",
                "qa",
                "[Rust Slice] let s = \"hello\"; 中的 s 是什么类型？存在哪里？为什么不可变？",
                "",
                "类型是 &str。字符串字面值被直接硬编码在二进制文件中（静态存储区），s 是指向它的引用。&str 是不可变引用，所以不能修改。",
                "来源：TRPL §4.3「字符串字面值就是 slice」。\"hello\" 的类型不是 String，而是 &str。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "&str", "string-literal", "binary", "qa"],
        ),
        # ── RQ70 · 函数参数用 &str ──
        note(
            model,
            [
                "RQ70",
                "qa",
                "[Rust Slice] 写 fn first_word(s: &str) -> &str 而非 fn first_word(s: &String) -> &str 有什么好处？",
                "",
                "&str 参数可以同时接受 &String（自动通过 deref coercion 转换）和 &str（字符串字面值或已有的 slice）。API 更通用，不损失任何功能。",
                "来源：TRPL §4.3 示例 4-9。这是 Rust 的惯用做法——优先用 &str 而不是 &String 作为参数类型。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "&str", "api-design", "deref-coercion", "qa"],
        ),
        # ── RQ71 · 数组 slice ──
        note(
            model,
            [
                "RQ71",
                "qa",
                "[Rust Slice] 数组的 slice 类型是什么？举个例子。",
                "",
                "类型是 &[i32]（元素类型包在 [] 中）。例如 let a = [1, 2, 3, 4, 5]; let slice = &a[1..3]; 得到 &[2, 3]。和字符串 slice 机制完全一样。",
                "来源：TRPL §4.3「其他类型的 slice」。slice 是通用概念——不仅 String 有，数组、Vec 等都有。",
                "",
                "",
                "",
            ],
            ["ch4", "rust", "slice", "array", "&[T]", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "Rust TRPL · 第四章：所有权", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
