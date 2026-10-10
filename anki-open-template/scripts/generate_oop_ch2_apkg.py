from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400512
OUTPUT = ROOT / "anki-第二章-Java语言基础.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══ C01 · 标识符规则 · 单选 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "以下哪个在 Java 中是合法的标识符？",
                "2player||_player||class||player-name",
                "2",
                "Java 标识符规则：由字母、数字、下划线、$ 组成，不能以数字开头，不能是关键字。A 以数字开头非法；C 是关键字；D 含连字符 - 非法。只有 B（下划线开头）合法。",
                "",
                "",
                "",
            ],
            ["ch2", "identifier", "choice"],
        ),
        # ═══ C02 · 命名约定 · 单选 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "以下哪个最符合 Java 命名约定？",
                "int player_score;||int PlayerScore;||int playerScore;||int playerscore;",
                "3",
                "变量名/方法名用 camelCase：首单词全小写，后续单词首字母大写。A 是 C 风格的下划线命名；B 是 PascalCase（用于类名）；D 缺少单词边界。",
                "",
                "",
                "",
            ],
            ["ch2", "naming", "convention", "choice"],
        ),
        # ═══ C03 · 关键字 · 单选 ═══
        note(
            model,
            [
                "C03",
                "choice",
                "以下哪一个是 Java 的保留关键字但实际未被使用？",
                "static||volatile||goto||synchronized",
                "3",
                "Java 有 50 个关键字，其中 goto 和 const 是保留字——保留但无实现。goto 在 JVM 层面存在（goto 字节码指令），但 Java 语法中不可用。static、volatile、synchronized 都是正常使用的关键字。",
                "",
                "",
                "",
            ],
            ["ch2", "keyword", "reserved", "choice"],
        ),
        # ═══ C04 · 注释类型 · 单选 ═══
        note(
            model,
            [
                "C04",
                "choice",
                "以下哪种注释可以通过 javadoc 命令自动生成 API 文档？",
                "// 行注释||/* 块注释 */||/** 文档注释 */||# 单行注释",
                "3",
                "只有 /** ... */ 格式的文档注释能被 javadoc 工具提取生成 HTML API 文档。// 和 /* */ 是普通注释，编译时被丢弃。# 不是 Java 的注释符号（那是 Python/bash 的）。",
                "",
                "",
                "",
            ],
            ["ch2", "comment", "javadoc", "choice"],
        ),
        # ═══ C05 · 基本数据类型大小 · 单选 ═══
        note(
            model,
            [
                "C05",
                "choice",
                "Java 中 int 类型占几个字节？",
                "与操作系统有关，32 位系统 2 字节，64 位系统 4 字节||固定 2 字节||固定 4 字节||固定 8 字节",
                "3",
                "Java 的 int 永远是 4 字节（32 bit），表数范围 -2³¹ ~ 2³¹-1，不受操作系统或 CPU 架构影响。这与 C 不同——C 的 int 大小是实现定义的。这正是 Java「一次编译，到处运行」在类型系统上的体现。",
                "",
                "",
                "",
            ],
            ["ch2", "datatype", "int", "choice"],
        ),
        # ═══ C06 · boolean 独立类型 · 单选 ═══
        note(
            model,
            [
                "C06",
                "choice",
                "以下哪些代码在 Java 中能通过编译？",
                "if (1) { }||int flag = 1; if (flag) { }||boolean b = true; if (b) { }||if (x = 5) { }",
                "3",
                "Java 的 boolean 是独立的类型，与整数不兼容。if 的条件必须是 boolean 或 Boolean 类型。A 中整数不能当布尔值；B 中 int 变量不能直接做条件；D 是赋值表达式 x=5 返回 int，不能做条件（这与 C 的重大差异——杜绝 if(x=5) 语义错误）。C 是唯一合法的。",
                "",
                "",
                "",
            ],
            ["ch2", "boolean", "type-safety", "choice"],
        ),
        # ═══ C07 · char 编码 · 单选 ═══
        note(
            model,
            [
                "C07",
                "choice",
                "Java 的 char 类型使用什么编码，占多少字节？",
                "ASCII，1 字节||UTF-8，可变长度 1-4 字节||UTF-16 code unit，2 字节||Unicode 码点，4 字节",
                "3",
                "Java 的 char 是 UTF-16 的 code unit，固定 2 字节（16 bit）。这与 C 的 char（1 字节，通常 ASCII）不同。注意：一个 char 不一定能表示一个完整的 Unicode 字符——补充平面的字符（如某些 emoji）需要两个 char（代理对，surrogate pair）表示。",
                "",
                "",
                "",
            ],
            ["ch2", "char", "utf16", "choice"],
        ),
        # ═══ C08 · 浮点默认类型 · 单选 ═══
        note(
            model,
            [
                "C08",
                "choice",
                "以下哪行代码会导致编译错误？",
                "double d = 3.14;||float f = 3.14f;||float f = 3.14;||float f = (float) 3.14;",
                "3",
                "Java 的浮点字面量（如 3.14）默认为 double 类型。double 不能自动降级赋给 float——必须显式转型或加 f/F 后缀。A 中 double 赋给 double 没问题；B 用 f 后缀明确是 float；D 用强制转型也可以。C 没有后缀也没有转型，编译报错。",
                "",
                "",
                "",
            ],
            ["ch2", "float", "literal", "choice"],
        ),
        # ═══ C09 · 类型转换 · 单选 ═══
        note(
            model,
            [
                "C09",
                "choice",
                "以下哪个类型转换在 Java 中必须显式强转（可能丢失数据）？",
                "byte → int||int → long||long → double||double → int",
                "4",
                "自动类型转换（widening）从低精度到高精度：byte→short→int→long→float→double 自动完成。反向（narrowing）必须显式强制转型：(int) 3.99 结果为 3——直接截断小数部分，不是四舍五入。",
                "",
                "",
                "",
            ],
            ["ch2", "casting", "narrowing", "choice"],
        ),
        # ═══ C10 · 数组本质 · 单选 ═══
        note(
            model,
            [
                "C10",
                "choice",
                "关于 Java 数组，以下哪项描述是错误的？",
                "数组是对象，有 .length 属性||访问越界会抛出 ArrayIndexOutOfBoundsException||数组创建后长度不可改变||数组的 length 是一个方法，需要加括号调用",
                "4",
                "Java 数组是 JVM 自动生成的特殊对象，.length 是属性不是方法——a.length 而非 a.length()。数组创建后长度固定，越界访问必抛异常（不像 C 的未定义行为）。JVM 内部用 [I、[C 等命名规则标识数组类型。",
                "",
                "",
                "",
            ],
            ["ch2", "array", "properties", "choice"],
        ),
        # ═══ C11 · 数组声明 · 单选 ═══
        note(
            model,
            [
                "C11",
                "choice",
                "int[] a, b; 声明后，a 和 b 的类型分别是什么？",
                "a 是 int，b 是 int[]||a 是 int[]，b 是 int||a 和 b 都是 int[]||编译错误",
                "3",
                "Java 推荐风格 int[] a, b 中，int[] 是完整类型，a 和 b 都是 int[]。对比 C 风格 int a[], b 中 a 是 int[] 但 b 只是 int——这正是推荐第一种写法的原因。",
                "",
                "",
                "",
            ],
            ["ch2", "array", "declaration", "choice"],
        ),
        # ═══ C12 · break 多层 · 单选 ═══
        note(
            model,
            [
                "C12",
                "choice",
                "带标签的 break outer 在字节码层面如何实现？",
                "JVM 解释器查找标签名字后跳转||编译为 goto 指令直接跳到标签后的字节码偏移||运行时异常处理机制||调用标签对象的 break 方法",
                "2",
                "带标签 break 是纯粹的编译期特性：javac 将 break outer 直接编译为 goto 指令，目标偏移是标签所在循环后的第一条指令。标签名字只存在于源码中，字节码中没有标签名字的运行时查找——零开销。JVM 的 goto 指令本身是存在的，但 Java 语法中 goto 被保留而不允许使用。",
                "",
                "",
                "",
            ],
            ["ch2", "break", "labeled", "choice"],
        ),
        # ═══ C13 · throw vs throws · 单选 ═══
        note(
            model,
            [
                "C13",
                "choice",
                "关于 throw 和 throws，以下哪项是正确的？",
                "两者都必须在方法签名中声明||throw 后面跟异常类型，throws 后面跟异常对象||throws 声明在方法签名上，throw 在方法体内抛异常对象||throws 用于捕获异常，throw 用于声明异常",
                "3",
                "throw 是语句，在方法体内执行，后面跟异常对象（如 new IOException()）；throws 是方法签名声明，后面跟异常类型（如 IOException, Exception），向编译器和调用者宣告本方法可能抛出这些异常。受检异常必须用 throws 声明或 try-catch 处理，非受检异常不做强制要求。",
                "",
                "",
                "",
            ],
            ["ch2", "exception", "throw-throws", "choice"],
        ),
        # ═══ C14 · 受检异常 · 单选 ═══
        note(
            model,
            [
                "C14",
                "choice",
                "以下哪种异常是受检异常（Checked Exception），调用者必须处理或声明？",
                "NullPointerException||ArrayIndexOutOfBoundsException||IOException||IllegalArgumentException",
                "3",
                "IOException 及其子类（如 FileNotFoundException）是受检异常——编译器强制要求调用者 try-catch 或用 throws 声明。其他三个都是 RuntimeException 的子类（非受检异常），编译器不强制处理。设计哲学：IO 错误不可控但可预期（文件可能不在、网络可能断开），所以强制要求处理。",
                "",
                "",
                "",
            ],
            ["ch2", "exception", "checked", "choice"],
        ),
        # ═══ C15 · GC 回收对象 · 单选 ═══
        note(
            model,
            [
                "C15",
                "choice",
                "Java 垃圾回收器（GC）回收对象的标准是什么？",
                "对象的引用计数降为零||对象从 GC Root 出发不可达||程序显式调用 System.gc() 后立即回收||对象创建超过指定时间",
                "2",
                "Java GC 基于可达性分析：从 GC Root（栈上局部变量、静态字段、活跃线程等）出发，沿引用链能到达的对象存活，到达不了的就是垃圾。Java 不使用引用计数（无法处理循环引用）。System.gc() 只是建议 JVM 执行 GC，不保证立即回收，也不应依赖它。",
                "",
                "",
                "",
            ],
            ["ch2", "gc", "reachability", "choice"],
        ),
        # ═══ C16 · 堆内存分区 · 单选 ═══
        note(
            model,
            [
                "C16",
                "choice",
                "JVM 堆内存中，新创建的对象首先分配到哪个区域？",
                "老年代（Old Generation）||元空间（Metaspace）||新生代（Young Generation）||永久代（PermGen）",
                "3",
                "新对象分配在新生代（Young Gen）。存活足够多次 Minor GC 的对象晋升到老年代（Old Gen）。元空间（Metaspace，JDK 8+ 替代永久代）存类元数据而非对象实例。分代收集的设计基于「大多数对象朝生暮死」的经验假设。",
                "",
                "",
                "",
            ],
            ["ch2", "gc", "generations", "choice"],
        ),
        # ═══ C17 · JVM/JRE/JDK · 单选 ═══
        note(
            model,
            [
                "C17",
                "choice",
                "以下关于 JVM/JRE/JDK 的关系，哪个描述正确？",
                "JRE 包含 JDK||JDK 包含 JRE，JRE 包含 JVM||JVM 包含 JRE||三者是并列关系",
                "2",
                "包含关系：JDK（开发工具包）= 开发工具（javac、jar 等）+ JRE；JRE（运行环境）= JVM + 核心类库；JVM（虚拟机）= 类加载器 + 运行时数据区 + 执行引擎（含 GC）+ 本地接口。用户只运行程序只需 JRE，开发需 JDK。",
                "",
                "",
                "",
            ],
            ["ch2", "jvm", "jre", "jdk", "choice"],
        ),
        # ═══ F01 · 标识符规则 · 填空 ═══
        note(
            model,
            [
                "F01",
                "fill",
                "Java 标识符由{{c1::字母}}、{{c2::数字}}、{{c3::下划线（_）}}、{{c4::美元符号（$）}}组成，不能以{{c5::数字}}开头，区分{{c6::大小写}}。关键字{{c7::不能}}（能/不能）用作标识符。",
                "",
                "字母||数字||下划线（_）||美元符号（$）||数字||大小写||不能",
                "标识符命名约定：类名 PascalCase（HelloWorld），方法名/变量名 camelCase（playerScore），常量全大写下划线分隔（MAX_ENTRIES），包名全小写（com.hitsz）。",
                "",
                "",
                "",
            ],
            ["ch2", "identifier", "rules", "fill", "multi-cloze"],
        ),
        # ═══ F02 · 注释三种 · 填空 ═══
        note(
            model,
            [
                "F02",
                "fill",
                "Java 三种注释：{{c1:://}} 用于单行注释，{{c2::/* */}} 用于块注释（不能嵌套），{{c3::/** */}} 用于文档注释——可通过{{c4::javadoc}}命令生成 API 文档。",
                "",
                "//||/* */||/** */||javadoc",
                "文档注释内可使用 @param、@return、@throws 等 Javadoc 标签，描述方法的参数、返回值和可能抛出的异常。",
                "",
                "",
                "",
            ],
            ["ch2", "comment", "types", "fill", "multi-cloze"],
        ),
        # ═══ F03 · 8种基本类型 · 填空 ═══
        note(
            model,
            [
                "F03",
                "fill",
                "Java 的 8 种基本数据类型：整数型——{{c1::byte}}(1字节)、{{c2::short}}(2字节)、{{c3::int}}(4字节)、{{c4::long}}(8字节)；浮点型——{{c5::float}}(4字节，IEEE)、{{c6::double}}(8字节)；字符型——{{c7::char}}(2字节，UTF-16 code unit)；布尔型——{{c8::boolean}}(取值为 true/false)。整数默认类型是{{c9::int}}，浮点默认是{{c10::double}}。",
                "",
                "byte||short||int||long||float||double||char||boolean||int||double",
                "Java 各类型表数范围固定，不随 OS/CPU 变化。long 常量加 L 后缀（如 100L），float 常量加 f/F 后缀（如 3.14f）。",
                "",
                "",
                "",
            ],
            ["ch2", "datatype", "primitive", "fill", "multi-cloze"],
        ),
        # ═══ F04 · 类型转换阶梯 · 填空 ═══
        note(
            model,
            [
                "F04",
                "fill",
                "Java 自动类型转换（widening）的精度阶梯：{{c1::byte}} → {{c2::short}} → {{c3::int}} → {{c4::long}} → {{c5::float}} → {{c6::double}}。反向转换（narrowing）必须使用强制转型语法 {{c7::(目标类型) 值}}，可能{{c8::丢失精度}}。",
                "",
                "byte||short||int||long||float||double||(目标类型) 值||丢失精度",
                "注意：long（64位整数）自动转 float（32位浮点）虽合法，但有效精度从 64 位降到约 23 位。char 类型可以自动转为 int、long、float、double，但不能与 short 互转（两者都是 16 位）。",
                "",
                "",
                "",
            ],
            ["ch2", "casting", "promotion", "fill", "multi-cloze"],
        ),
        # ═══ F05 · 数组声明创建 · 填空 ═══
        note(
            model,
            [
                "F05",
                "fill",
                "Java 数组声明推荐使用{{c1::int[] a}}而非 C 风格的 int a[]。创建数组：① 指定长度——{{c2::new int[5]}}，元素自动初始化为默认值；② 直接初始化——{{c3::new int[]{1, 2, 3}}}或简写{{c4::{1, 2, 3}}}。数组长度通过{{c5::.length}}属性获取（非方法）。数组创建后长度{{c6::不可改变}}，越界访问抛出{{c7::ArrayIndexOutOfBoundsException}}。",
                "",
                "int[] a||new int[5]||new int[]{1, 2, 3}||{1, 2, 3}||.length||不可改变||ArrayIndexOutOfBoundsException",
                "JVM 内部数组类型命名：[I 表示 int[]，[C 表示 char[]，[Ljava.lang.String; 表示 String[]，[[I 表示 int[][]。",
                "",
                "",
                "",
            ],
            ["ch2", "array", "syntax", "fill", "multi-cloze"],
        ),
        # ═══ F06 · 异常关键字 · 填空 ═══
        note(
            model,
            [
                "F06",
                "fill",
                "Java 异常处理五大关键字：{{c1::try}}包裹可能异常的代码、{{c2::catch}}捕获并处理特定异常、{{c3::finally}}执行必定运行的清理代码、{{c4::throw}}在方法体内抛出异常对象、{{c5::throws}}在方法签名上声明本方法可能抛出的异常类型。受检异常必须被{{c6::try-catch}}处理或在方法签名上用{{c7::throws}}声明。",
                "",
                "try||catch||finally||throw||throws||try-catch||throws",
                "异常体系根类：Throwable → Error（严重系统错误）/Exception。Exception 下分 RuntimeException（非受检，如 NPE）和受检异常（如 IOException）。三种捕获形式：try-catch、try-catch-finally、try-finally。",
                "",
                "",
                "",
            ],
            ["ch2", "exception", "keywords", "fill", "multi-cloze"],
        ),
        # ═══ F07 · 堆内存三代 · 填空 ═══
        note(
            model,
            [
                "F07",
                "fill",
                "JVM 堆内存逻辑上分为三区：{{c1::新生代}}（新对象和短命对象）、{{c2::老年代}}（多次 GC 仍存活的长命对象）、{{c3::元空间}}（JDK 8+ 存储类元数据，使用本地内存）。对象晋升条件：每活过一次{{c4::Minor GC}}年龄+1，达到{{c5::MaxTenuringThreshold}}（默认 15）移到老年代。",
                "",
                "新生代||老年代||元空间||Minor GC||MaxTenuringThreshold",
                "分代设计原理：绝大多数对象朝生暮死（循环临时变量），新生代用高频小范围 GC；少量长寿对象（缓存、单例）最终进入老年代，用低频全范围 GC。元空间在 JDK 8 前叫永久代（PermGen），占用 JVM 内存；JDK 8 起用本地内存，避免永久代 OOM。",
                "",
                "",
                "",
            ],
            ["ch2", "gc", "heap", "fill", "multi-cloze"],
        ),
        # ═══ F08 · final · 填空 ═══
        note(
            model,
            [
                "F08",
                "fill",
                "Java 中用{{c1::final}}关键字声明常量（C 中 const 被保留但不实现）。符号常量声明示例：{{c2::public static final double PI = 3.14159;}}。final 修饰基本类型时{{c3::值不可改}}，修饰引用类型时{{c4::引用不可改（不可指向新对象）}}但对象内部状态可改。",
                "",
                "final||public static final double PI = 3.14159;||值不可改||引用不可改（不可指向新对象）",
                "常量三种作用域：静态常量（static final，类级别共享）、成员常量（实例级别）、局部常量（方法内）。final 修饰方法表示该方法不能被子类覆盖（override），修饰类表示该类不能被继承。",
                "",
                "",
                "",
            ],
            ["ch2", "constant", "final", "fill", "multi-cloze"],
        ),
        # ═══ Q01 · 标识符与命名规范 · 问答 ═══
        note(
            model,
            [
                "Q01",
                "qa",
                "分别举例说明 Java 标识符的「语法规则」和「命名约定」有什么区别。为什么约定也很重要？",
                "",
                "语法规则是编译器的硬性规定：由字母、数字、_、$ 组成，不以数字开头，不能是关键字。违反即编译错误。命名约定是社区规范，不报错但被视为不合格代码：类名 PascalCase（ScoreBoard），方法/变量 camelCase（playerScore），常量 UPPER_SNAKE_CASE（MAX_ENTRIES），包名全小写。约定重要因为软件构造第一目标是「可理解性」——六个月后的自己或同事需要一眼看懂代码中每个名字的角色。",
                "约定 vs 规则的类比：规则是「不能穿拖鞋进考场」（硬性），约定是「穿正装面试」（软性）。规则保下限，约定提上限。",
                "",
                "",
                "",
            ],
            ["ch2", "identifier", "convention", "qa"],
        ),
        # ═══ Q02 · Java vs C 类型三大差异 · 问答 ═══
        note(
            model,
            [
                "Q02",
                "qa",
                "从语言设计角度，详细说明 Java 基本数据类型与 C 的三大根本差异及其设计动机。",
                "",
                "差异 1——固定宽度 vs 实现定义：Java 的 int 永远是 4 字节，C 的 int 随平台而变。动机：Java 追求移植性（一次编译到处运行），C 追求接近硬件（跟 CPU 字长走）。差异 2——boolean 独立类型 vs 整数：Java 的 boolean 只能取 true/false，不能与整数互转。动机：类型安全——从编译期消灭 if(x=5) 将赋值当条件的经典 bug。差异 3——char 是 UTF-16(2字节) vs ASCII(1字节)：动机：Java 设计于国际化时代，char 必须能表示 Unicode 基本多文种平面字符。C 的 char 继承自早期计算机的 7 位 ASCII。",
                "补充：Java 没有 unsigned 整数类型——所有整型都是有符号的。Java 设计者认为 unsigned 引入的复杂性（混合运算的类型提升规则）大于其收益，且大多数场景用更大一级有符号类型即可容纳。",
                "",
                "",
                "",
            ],
            ["ch2", "java-vs-c", "types", "qa"],
        ),
        # ═══ Q03 · switch(String) 内部实现 · 问答 ═══
        note(
            model,
            [
                "Q03",
                "qa",
                "Java 的 switch 支持 String 类型（JDK 7 起），请描述编译器在字节码层面是如何实现的。为什么不能只用 hashCode？",
                "",
                "编译器将 switch(String) 编译为两步判定。第一步：计算字符串 s.hashCode()，用 lookupswitch 指令按 int 分支配对。第二步：跳到目标 case 后，必须执行 s.equals(\"case字符串\") 二次确认。这是因为不同字符串的 hashCode 可能碰撞——hashCode() 的契约是 a.equals(b) ⇒ a.hashCode()==b.hashCode()，但反过来不成立。如果只用 hashCode，碰撞会导致执行错误的 case 分支（正确性 bug）。字节码层面是普通的 lookupswitch + equals 调用组合，JVM 没有特殊的「字符串 switch」指令。",
                "hashCode 公式：s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1]。虽然碰撞概率极低，但编译器不能赌概率——必须保证语义正确。另外，重复的 case 标签在语义分析阶段就被 javac 直接报错。",
                "",
                "",
                "",
            ],
            ["ch2", "switch", "string", "implementation", "qa"],
        ),
        # ═══ Q04 · Garbage Collection · 问答 ═══
        note(
            model,
            [
                "Q04",
                "qa",
                "Java GC 的可达性分析是如何工作的？与传统引用计数相比有何优劣？为什么 GC 不能完全消除内存泄漏？",
                "",
                "可达性分析：从 GC Root 集合（栈上局部变量、静态字段、JNI 引用、活跃线程等）出发，沿引用链遍历对象图。被遍历到的对象标记为「存活」，未遍历到的即为垃圾，将在 GC 时回收。对比引用计数：引用计数无法处理循环引用（A↔B 互相引用但外部不可达），每次引用变更都要更新计数有额外开销。但引用计数是即时回收（计数归零立即释放），GC 是延迟批量回收——触发时机不确定。GC 不能消除内存泄漏：如果代码将对象放入静态集合后忘记移除，对象始终从 GC Root 可达，GC 无法回收——这是「逻辑泄漏」而非「物理泄漏」。",
                "Rust 对比：编译期所有权+借用检查杜绝了所有内存安全问题（包括逻辑泄漏的特定形式如 use-after-free），零运行时 GC 开销。代价是程序员必须理解所有权模型。Java 的 GC 换取了更简单的编程模型，代价是运行时开销和回收时机不可控。",
                "",
                "",
                "",
            ],
            ["ch2", "gc", "reachability", "qa"],
        ),
        # ═══ Q05 · try-finally 设计 · 问答 ═══
        note(
            model,
            [
                "Q05",
                "qa",
                "为什么 Java 需要 finally 块？什么场景下 finally 是唯一正确的做法（try-catch 无法替代）？",
                "",
                "finally 块的语义：无论 try 块是正常结束、抛出异常、还是执行了 return，finally 中的代码一定会执行。不可替代的场景：① 锁释放——lock.unlock() 必须放在 finally 中，否则异常会导致锁永不释放，其他线程永久阻塞；② 资源关闭——文件流、数据库连接如果在 try 中关闭，一旦前面代码抛异常，close() 永远执行不到。try-catch 无法替代因为：catch 只在异常发生时执行（正常返回时不执行），而 finally 无论正常还是异常都执行。try-finally 的形式（无 catch）用于「当前方法不处理异常，但必须释放资源」的场景。",
                "JDK 7 引入 try-with-resources 语法简化了场景②：try (FileReader fr = new FileReader(path)) { ... } 自动在末尾调用 fr.close()，编译器生成的字节码等价于 try-finally。",
                "",
                "",
                "",
            ],
            ["ch2", "finally", "resource", "qa"],
        ),
        # ═══ Q06 · continue 死循环 · 问答 ═══
        note(
            model,
            [
                "Q06",
                "qa",
                "分析以下代码为何会死循环，并说明 continue 在 while 和 for 中的行为差异。\nint i = 0;\nwhile (i < 10) {\n    if (i % 2 == 0) { continue; }\n    System.out.println(i);\n    i++;\n}",
                "",
                "初始 i=0，0%2==0 → continue，跳过 i++。下一次循环 i 仍然是 0 → 再次 continue → 无限循环。根因：while 循环中，循环变量的更新语句在循环体内，continue 跳过了它。对比 for 循环：for(int i=0; i<10; i++) { if(i%2==0) continue; ... } 不会死循环——因为 i++ 在循环头的表达式中，continue 不跳过它。原理：continue 跳过的是「循环体内 continue 之后的所有语句」，while 循环的条件判断和 for 循环头的表达式 3（i++）不在这个范围内。简言之：continue 不跳过循环头，只跳过循环体剩余部分。",
                "Java 字节码层面：continue 编译为 goto，目标偏移指向循环的条件判断指令（while 的 i<10 判断 / for 的 i++ 后 i<10 判断），而非循环体顶部。",
                "",
                "",
                "",
            ],
            ["ch2", "continue", "infinite-loop", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 第二章 Java语言基础", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
