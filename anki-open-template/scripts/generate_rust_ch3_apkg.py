from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck, trusted_html

DECK_ID = 2059400731
OUTPUT = ROOT / "anki-Rust-第三章-常见编程概念.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════════════════════════════════════════════════════
        # §3.1 常量 const
        # ═══════════════════════════════════════════════════════════

        # ── RF33a · const vs let 可变性 ──
        note(
            model,
            [
                "RF33a",
                "fill",
                trusted_html("[Rust 变量] const 声明的常量和 let 声明的不可变变量，在可变性上的区别：<br>const 永远不可变——{{c1::不能}}使用 mut；而 let 变量{{c2::可以}}通过加 mut 变为可变。"),
                "",
                "不能||可以",
                "来源：TRPL §3.1「常量」。const 的设计意图是\"编译时确定、永不改变\"，语法上禁止 mut。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "const", "mut", "variable", "fill", "multi-cloze"],
        ),
        # ── RF33b · const vs let 类型注解 ──
        note(
            model,
            [
                "RF33b",
                "fill",
                trusted_html("[Rust 变量] const 和 let 在类型注解上的区别：<br>const{{c1::必须}}标注类型（如 const X: u32 = ...）；let{{c2::可以}}靠类型推断省略。"),
                "",
                "必须||可以",
                "来源：TRPL §3.1。const 可在全局声明，编译器缺少上下文推断类型，因此强制标注。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "const", "type-annotation", "fill", "multi-cloze"],
        ),
        # ── RF33c · const vs let 作用域与初始化 ──
        note(
            model,
            [
                "RF33c",
                "fill",
                trusted_html("[Rust 变量] const 和 let 在作用域和初始化值上的区别：<br>const 可在{{c1::任何作用域}}声明（包括全局），只能用{{c2::常量表达式}}（编译时可求值）初始化；let 只能在{{c3::函数/代码块}}内声明。"),
                "",
                "任何作用域||常量表达式||函数/代码块",
                "来源：TRPL §3.1。const 不依赖运行时状态，所以可以放全局。命名约定：SCREAMING_SNAKE_CASE。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "const", "scope", "fill", "multi-cloze"],
        ),
        # ── RF34 · const 语法 ──
        note(
            model,
            [
                "RF34",
                "fill",
                trusted_html("[Rust 变量] 声明一个常量，值为 3 小时的秒数：<br><pre>const THREE_HOURS_IN_SECONDS: {{c1::u32}} = {{c2::60 * 60 * 3}};</pre>"),
                "",
                "u32||60 * 60 * 3",
                "来源：TRPL §3.1。const 名全大写+下划线。右边必须是常量表达式（编译器在编译时计算出 10800）。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "const", "syntax", "fill", "multi-cloze"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §3.2 数据类型
        # ═══════════════════════════════════════════════════════════

        # ── RQ30 · 静态类型 ──
        note(
            model,
            [
                "RQ30",
                "qa",
                "[Rust 类型系统] Rust 属于静态类型还是动态类型语言？这带来什么实际影响？",
                "",
                "静态类型语言——编译时必须知道所有变量的类型。编译器通常可推断类型，但存在歧义时必须手动标注（如 let x: u32 = \"42\".parse().unwrap();）。",
                "来源：TRPL §3.2。与其他静态类型语言不同，Rust 的类型推断能力很强，多数情况不需要显式标注。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "static-typing", "type-inference", "qa"],
        ),
        # ── RQ31 · 四种标量 ──
        note(
            model,
            [
                "RQ31",
                "qa",
                "[Rust 类型系统] Rust 有哪四种基本的标量（scalar）类型？",
                "",
                "整型、浮点型、布尔型（bool）、字符型（char）。",
                "来源：TRPL §3.2。标量 = 单个值。复合类型（元组、数组）= 多个值组合。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "scalar", "types", "qa"],
        ),
        # ── RF35 · 整型表 ──
        note(
            model,
            [
                "RF35",
                "fill",
                trusted_html("[Rust 类型系统] 整数类型表格：<br>8-bit: {{c1::i8}}/{{c2::u8}} &nbsp; 16-bit: {{c3::i16}}/{{c4::u16}} &nbsp; 32-bit: {{c5::i32}}/{{c6::u32}}<br>64-bit: {{c7::i64}}/{{c8::u64}} &nbsp; 128-bit: {{c9::i128}}/{{c10::u128}} &nbsp; 架构相关: {{c11::isize}}/{{c12::usize}}"),
                "",
                "i8||u8||i16||u16||i32||u32||i64||u64||i128||u128||isize||usize",
                "来源：TRPL §3.2 表格 3-1。默认整型是 i32。isize/usize 位数随 CPU 架构（32/64 位）。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "integer", "types", "fill", "multi-cloze"],
        ),
        # ── RQ32 · 有符号 vs 无符号 ──
        note(
            model,
            [
                "RQ32",
                "qa",
                "[Rust 类型系统] i8 和 u8 的取值范围各是多少？i 和 u 分别代表什么？",
                "",
                'i8: -128 ~ 127   u8: 0 ~ 255\ni = signed（有符号，可表示负数）；u = unsigned（无符号，只能非负）。',
                "来源：TRPL §3.2。有符号用二进制补码。n 位有符号范围：-(2^(n-1)) ~ 2^(n-1)-1。n 位无符号范围：0 ~ 2^n-1。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "signed", "unsigned", "integer", "qa"],
        ),
        # ── RQ33a · 整型溢出定义 ──
        note(
            model,
            [
                "RQ33a",
                "qa",
                "[Rust 类型系统] 什么是整型溢出（integer overflow）？举一个具体例子。",
                "",
                "值超出类型能表示的范围。例如 let x: u8 = 256; ——u8 只能存 0~255，256 超出范围，发生溢出。",
                "来源：TRPL §3.2「整型溢出」。溢出的后果取决于编译模式（debug/release）。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "overflow", "integer", "qa"],
        ),
        # ── RQ33b · 溢出 debug 行为 ──
        note(
            model,
            [
                "RQ33b",
                "qa",
                "[Rust 类型系统] debug 模式下发生整型溢出（如 let x: u8 = 256;），Rust 会怎样？",
                "",
                "程序 panic（崩溃退出）。Rust 在 debug 构建中加入溢出检查，帮助开发者尽早发现溢出 bug。",
                "来源：TRPL §3.2。debug = 开发模式，安全优先。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "overflow", "debug", "panic", "qa"],
        ),
        # ── RQ33c · 溢出 release 行为 ──
        note(
            model,
            [
                "RQ33c",
                "qa",
                "[Rust 类型系统] release 模式下发生整型溢出，Rust 会怎样？u8 的 256 会变成什么？",
                "",
                "不 panic，执行回绕（wrapping）：值超过最大值后从最小值重新开始。256 回绕为 0，257 回绕为 1。",
                "来源：TRPL §3.2。release = 性能优先，不检查溢出。需要显式处理用 wrapping_*/checked_*/overflowing_*/saturating_* 方法。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "overflow", "release", "wrapping", "qa"],
        ),
        # ── RF36 · 溢出处理方法 ──
        note(
            model,
            [
                "RF36",
                "fill",
                trusted_html("[Rust 类型系统] 标准库显式溢出处理方法：<br>wrapping: {{c1::wrapping_*}} &nbsp; 返回 None: {{c2::checked_*}}<br>返回结果+溢出标志: {{c3::overflowing_*}} &nbsp; 边界饱和: {{c4::saturating_*}}"),
                "",
                "wrapping_*||checked_*||overflowing_*||saturating_*",
                "来源：TRPL §3.2。wrapping（密码学/哈希）、checked（安全优先，返回 Option）、overflowing（需要标志位）、saturating（信号处理/音频，停在边界值）。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "overflow", "methods", "fill", "multi-cloze"],
        ),
        # ── RF37 · 整型字面值 ──
        note(
            model,
            [
                "RF37",
                "fill",
                trusted_html("[Rust 类型系统] 整数字面值写法：<br>十进制: 98_222（_ 是{{c1::视觉分隔符}}）<br>十六进制: {{c2::0xff}} &nbsp; 八进制: {{c3::0o77}}<br>二进制: {{c4::0b1111_0000}} &nbsp; 字节字面值(仅 u8): {{c5::b'A'}}"),
                "",
                "视觉分隔符||0xff||0o77||0b1111_0000||b'A'",
                "来源：TRPL §3.2 表格 3-2。_ 不影响数值只提高可读性。b'A' 等价于 65u8（ASCII 码）。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "literals", "integer", "fill", "multi-cloze"],
        ),
        # ── RQ34 · 浮点型 ──
        note(
            model,
            [
                "RQ34",
                "qa",
                "[Rust 类型系统] Rust 的两种浮点类型是什么？默认哪个？为什么？",
                "",
                "f32（32 位）和 f64（64 位）。默认 f64——在现代 CPU 上速度与 f32 几乎一样，但精度更高。都遵循 IEEE-754 标准。",
                "来源：TRPL §3.2「浮点型」。所有浮点型都是有符号的。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "float", "f32", "f64", "qa"],
        ),
        # ── RQ35 · char 类型 ──
        note(
            model,
            [
                "RQ35",
                "qa",
                "[Rust 类型系统] Rust 的 char 类型占几个字节？能表示什么范围？",
                "",
                "占 4 个字节（32 位）。表示 Unicode 标量值（Unicode Scalar Value），范围 U+0000~U+D7FF 和 U+E000~U+10FFFF。涵盖 ASCII、中文、emoji。",
                "来源：TRPL §3.2「字符类型」。char 不是 1 字节！用单引号声明：let c = '中';",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "char", "unicode", "qa"],
        ),
        # ── RQ36 · 两种复合类型 ──
        note(
            model,
            [
                "RQ36",
                "qa",
                "[Rust 类型系统] Rust 的两种原生复合类型是什么？核心区别？",
                "",
                '元组（tuple）：固定长度，元素可以不同类型。\n数组（array）：固定长度，所有元素必须相同类型。',
                "来源：TRPL §3.2「复合类型」。两者都是固定长度、栈上分配。动态长度用 Vec（第八章）。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "compound-types", "tuple", "array", "qa"],
        ),
        # ── RF38 · 元组解构与索引 ──
        note(
            model,
            [
                "RF38",
                "fill",
                trusted_html("[Rust 类型系统] 元组的两种取值方式：<br><pre>let tup: (i32, f64, u8) = (500, 6.4, 1);\n// 方式一：解构\nlet (x, y, z) = {{c1::tup}};\n// 方式二：点索引（从 0 开始）\nlet five_hundred = tup.{{c2::0}};</pre>"),
                "",
                "tup||0",
                "来源：TRPL §3.2。解构 = 一次性拆给多个变量。点索引 = 单独访问（如 tup.0, tup.1, tup.2）。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "tuple", "destructuring", "fill", "multi-cloze"],
        ),
        # ── RQ37 · 单元类型 () ──
        note(
            model,
            [
                "RQ37",
                "qa",
                "[Rust 类型系统] Rust 的单元（unit）类型写作什么？什么时候出现？",
                "",
                "写作 ()。是空元组。不返回任何值的表达式隐式返回 ()。没有显式返回值的函数也返回 ()。",
                "来源：TRPL §3.2。() 既是类型也是值，类似于 C 的 void，但 () 可以作为值传递和绑定。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "unit", "()", "qa"],
        ),
        # ── RF39 · 数组类型标注与初始化 ──
        note(
            model,
            [
                "RF39",
                "fill",
                trusted_html("[Rust 类型系统] 数组的两种创建方式：<br><pre>// 显式类型标注：[类型; 长度]\nlet a: [{{c1::i32}}; 5] = [1, 2, 3, 4, 5];\n// 重复值初始化\nlet b = [{{c2::3}}; 5];  // 等价于 [3, 3, 3, 3, 3]</pre>"),
                "",
                "i32||3",
                "来源：TRPL §3.2。数组长度是类型的一部分：let a: [i32; 5] 和 let a: [i32; 10] 是不同类型。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "array", "syntax", "fill", "multi-cloze"],
        ),
        # ── RQ38 · 数组越界检查 ──
        note(
            model,
            [
                "RQ38",
                "qa",
                "[Rust 类型系统] 访问数组 a[10] 但 a 只有 5 个元素，Rust 会怎样？",
                "",
                "运行时 panic（索引越界检查）。Rust 每次索引访问都检查 索引 < 数组长度。这是 Rust 内存安全保证的一部分——许多底层语言不检查，可能访问无效内存。",
                "来源：TRPL §3.2「无效的数组元素访问」。编译器无法预知运行时用户输入的索引值，所以在运行时检查。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "array", "bounds-check", "panic", "safety", "qa"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §3.3 函数
        # ═══════════════════════════════════════════════════════════

        # ── RQ39 · 语句 vs 表达式 ──
        note(
            model,
            [
                "RQ39",
                "qa",
                "[Rust 语法] 语句（statement）和表达式（expression）在 Rust 中的区别是什么？",
                "",
                '语句：执行操作，不返回值（如 let y = 6;、函数定义）。\n表达式：计算并产生一个值（如 5 + 6、函数调用、宏调用、代码块 { ... }）。',
                "来源：TRPL §3.3「语句和表达式」。这是 Rust 最核心的语法概念之一：分号将表达式转为语句（吃掉返回值）；代码块的值是最后一个表达式的值。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "statement", "expression", "syntax", "qa"],
        ),
        # ── RQ40 · 分号吞返回值 ──
        note(
            model,
            [
                "RQ40",
                "qa",
                "[Rust 语法] 在表达式末尾加分号 ; 会发生什么？",
                "",
                "表达式变成语句，丢弃其返回值，返回单元类型 ()。这就是函数最后一行不能加分号的原因——加了就不返回那个值了。",
                "来源：TRPL §3.3。let x = (let y = 6); 会编译错误，因为 let y = 6 是语句，不返回值。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "semicolon", "expression", "statement", "qa"],
        ),
        # ── RQ41 · 代码块是表达式 ──
        note(
            model,
            [
                "RQ41",
                "qa",
                "[Rust 语法] Rust 中花括号 { } 创建的代码块是什么？它的值怎么确定？",
                "",
                "代码块是表达式。整个块的值 = 块中最后一个表达式的值（不加分号的那行）。例如 { let x = 3; x + 1 } 的值是 4。",
                "来源：TRPL §3.3。这也是 if 表达式能用在 let 右侧的根本原因。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "block", "expression", "qa"],
        ),
        # ── RF40 · 函数返回值语法 ──
        note(
            model,
            [
                "RF40",
                "fill",
                trusted_html("[Rust 函数] 定义返回 i32 的函数 five（无参数，返回 5）：<br><pre>fn five() {{c1::-> i32}} {\n    {{c2::5}}\n}</pre>"),
                "",
                "-> i32||5",
                "来源：TRPL §3.3。-> 声明返回类型。最后一个表达式不加分号 = 隐式返回。return 用于提前返回。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "function", "return", "syntax", "fill", "multi-cloze"],
        ),
        # ── RQ42 · 函数参数必须标注类型 ──
        note(
            model,
            [
                "RQ42",
                "qa",
                "[Rust 函数] Rust 函数定义中，每个参数必须做什么？为什么？",
                "",
                "每个参数必须显式标注类型（如 fn foo(x: i32, y: char)）。不能写 fn foo(x, y)。这让编译器不需要从调用处反向推断，也能给出更清晰的错误信息和更好的文档。",
                "来源：TRPL §3.3「参数」。函数签名是 API 边界，显式类型 = 合约。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "function", "parameter", "type-annotation", "qa"],
        ),
        # ── RQ43 · return 关键字 ──
        note(
            model,
            [
                "RQ43",
                "qa",
                "[Rust 函数] Rust 中 return 关键字和隐式返回的区别是什么？",
                "",
                "隐式返回：函数最后一个表达式（无分号）= 返回值（Rust 惯用风格）。return：提前从函数中返回一个值，用于条件分支等需要提前退出的场景。",
                "来源：TRPL §3.3。大多数 Rust 函数用隐式返回。return 只在需要提前退出时使用。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "return", "implicit-return", "function", "qa"],
        ),

        # ═══════════════════════════════════════════════════════════
        # §3.5 控制流
        # ═══════════════════════════════════════════════════════════

        # ── RQ44 · if 条件必须是 bool ──
        note(
            model,
            [
                "RQ44",
                "qa",
                "[Rust 控制流] Rust 中 if 的条件必须是哪种类型？if 3 { } 会怎样？",
                "",
                "条件必须是 bool 类型（true 或 false）。if 3 { } 编译错误——Rust 不会自动把整数转为布尔值（无 truthy/falsy 概念）。必须显式写 if x != 0。",
                "来源：TRPL §3.5「if 表达式」。不同于 Ruby/JavaScript 的隐式转换。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "if", "bool", "type-check", "qa"],
        ),
        # ── RQ45 · if 是表达式 ──
        note(
            model,
            [
                "RQ45",
                "qa",
                "[Rust 控制流] Rust 中 if 可以作为表达式用在 let 右侧。使用这个特性有什么关键约束？",
                "",
                "所有分支必须返回相同类型。let x = if cond { 5 } else { \"six\" }; 编译错误——分支返回 i32 和 &str，类型不匹配。编译时必须确定变量的唯一类型。",
                "来源：TRPL §3.5「在 let 语句中使用 if」。这是因为 Rust 静态类型——变量类型必须在编译时确定。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "if-expression", "let", "type-consistency", "qa"],
        ),
        # ── RQ46 · 三种循环 ──
        note(
            model,
            [
                "RQ46",
                "qa",
                "[Rust 控制流] Rust 的三种循环结构是什么？各适合什么场景？",
                "",
                "loop：无限循环，手动 break 退出（适合\"一直尝试直到成功\"）。while：条件循环（适合\"满足条件才继续\"）。for：遍历迭代器/集合（最常用、最安全、推荐首选）。",
                "来源：TRPL §3.5「使用循环重复执行」。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "loop", "while", "for", "qa"],
        ),
        # ── RQ47 · break 带返回值 ──
        note(
            model,
            [
                "RQ47",
                "qa",
                "[Rust 控制流] loop 循环中，break 能做什么 while 和 for 中做不到的事？",
                "",
                "break 后面可以跟一个表达式，将该值作为整个 loop 表达式的返回值。let result = loop { ... break counter * 2; }; ——result 得到 break 后面的值。",
                "来源：TRPL §3.5「从循环返回值」。loop 本身是表达式，这是它独有的能力。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "loop", "break", "return-value", "qa"],
        ),
        # ── RQ48 · 循环标签 ──
        note(
            model,
            [
                "RQ48",
                "qa",
                "[Rust 控制流] 嵌套循环中，break 默认作用于哪一层？如何作用于外层？",
                "",
                "默认作用于最内层。要让 break/continue 作用于外层，给外层加循环标签：\n'label: loop { ... break 'label; }",
                "来源：TRPL §3.5「循环标签：在多个循环之间消除歧义」。标签以单引号 ' 开头。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "loop", "label", "break", "nested", "qa"],
        ),
        # ── RF41 · for + Range 倒计时 ──
        note(
            model,
            [
                "RF41",
                "fill",
                trusted_html("[Rust 控制流] 用 for 循环倒计时（输出 3, 2, 1）：<br><pre>for number in ({{c1::1}}..{{c2::4}}).rev() {\n    println!(\"{number}!\");\n}</pre>"),
                "",
                "1||4",
                "来源：TRPL §3.5。1..4 半开区间生成 1,2,3。.rev() 反转。for 遍历 Range 无越界风险，推荐优先使用。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "for", "range", "rev", "fill", "multi-cloze"],
        ),
        # ── RC12 · for 遍历 vs while 遍历 ──
        note(
            model,
            [
                "RC12",
                "choice",
                "[Rust 控制流] 遍历数组时，为什么推荐 for element in &array 而非 while index < array.len()？",
                "for 有编译器优化，更快||for 不手动管理索引，无越界风险，修改数组长度后不会忘记更新条件，代码更简洁安全||while 在 Rust 中已被标记为 deprecated||for 可以修改数组元素，while 不能",
                "2",
                "来源：TRPL §3.5。for 由编译器保证安全，是 Rust 的首选循环方式。while+索引容易写出越界 panic 或遗漏元素。",
                "",
                "",
                "",
            ],
            ["ch3", "rust", "for", "while", "array", "iteration", "choice"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "Rust TRPL · 第三章：常见编程概念", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
