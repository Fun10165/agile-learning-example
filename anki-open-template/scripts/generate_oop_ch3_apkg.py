from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400513
OUTPUT = ROOT / "anki-第三章-类和对象.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════ UML 类图（考试重点）═══════════
        # ═══ C01 · 类图三格 · 单选 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "UML 类图中，一个类的标准表示由几部分组成？分别是什么？",
                "两部分：类名 + 方法||三部分：类名 + 属性 + 操作（方法）||四部分：类名 + 属性 + 方法 + 构造器||一部分：只有类名",
                "2",
                "标准类图 = 三格矩形：第一格——类名（必须，抽象类用斜体或 «abstract» 标注）；第二格——属性（格式：可见性 名称: 类型，如 -hp: int）；第三格——操作/方法（格式：可见性 名称(参数: 类型): 返回类型，如 +getHp(): int）。后两格可选——简单场景可能省略属性和方法只留类名。",
                "",
                "",
                "",
            ],
            ["ch3", "uml", "class-diagram", "choice"],
        ),
        # ═══ C02 · 可见性标记 · 单选 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "UML 类图中，符号「+」「-」「#」「~」分别对应 Java 的什么访问修饰符？",
                "public / private / protected / default||private / public / protected / default||public / protected / private / default||public / private / default / protected",
                "1",
                "UML 可见性标记与 Java 的精确对应：+ = public（全局访问）、- = private（仅本类）、# = protected（本类+同包+子类）、~ = default/package-private（本类+同包）。口诀：+ 对所有人开放，- 对自己私密，# 对家人（子类）开放，~ 对邻居（同包）开放。",
                "",
                "",
                "",
            ],
            ["ch3", "uml", "visibility", "choice"],
        ),
        # ═══ C03 · 泛化关系 · 单选 ═══
        note(
            model,
            [
                "C03",
                "choice",
                "UML 中表示继承（泛化 Generalization）关系用哪种线和箭头？",
                "实线 + 普通箭头||实线 + 空心三角箭头（指向父类）||虚线 + 空心三角箭头||实线 + 实心菱形",
                "2",
                "泛化 = 空心三角箭头 + 实线，箭头指向父类。Java 对应 extends。注意箭头方向：箭头指向父类，不是指向子类——因为子类指向父类表示「is-a」。例：NormalEnemy ——▷ Enemy。",
                "",
                "",
                "",
            ],
            ["ch3", "uml", "generalization", "choice"],
        ),
        # ═══ C04 · 聚合 vs 组合 · 单选 ═══
        note(
            model,
            [
                "C04",
                "choice",
                "UML 中聚合（Aggregation）和组合（Composition）的核心区别是什么？用什么符号表示？",
                "没有区别，只是画法不同||聚合是弱拥有（空心菱形◇），部分可独立存在；组合是强拥有（实心菱形◆），部分随整体生死||聚合是强拥有，组合是弱拥有||聚合用实线，组合用虚线",
                "2",
                "聚合（Aggregation）= 空心菱形 ◇ + 实线，菱形在整体端。整体包含部分，但部分可以脱离整体独立存在。例：GamePanel ◇—— Enemy（敌机没有游戏面板也可以存在）。组合（Composition）= 实心菱形 ◆ + 实线。部分生命周期绑定整体——整体销毁则部分销毁。例：Hero ◆—— Weapon（武器离开英雄机无意义）。判断标准：部分能否脱离整体独立存在。",
                "",
                "",
                "",
            ],
            ["ch3", "uml", "aggregation", "composition", "choice"],
        ),
        # ═══ C05 · 六种关系归类 · 单选 ═══
        note(
            model,
            [
                "C05",
                "choice",
                "UML 中哪种关系使用虚线表示？",
                "泛化（Generalization）||关联（Association）||依赖（Dependency）和实现（Realization）||聚合（Aggregation）",
                "3",
                "UML 中只有两种关系用虚线：① 依赖（Dependency）——虚线 + 普通箭头，表示临时使用（方法参数/局部变量）；② 实现（Realization）——虚线 + 空心三角箭头，表示接口实现（下章讲）。其他四种都用实线。口诀：依赖和实现是「虚」的——一个是临时关系，一个是接口约定。",
                "",
                "",
                "",
            ],
            ["ch3", "uml", "dependency", "realization", "choice"],
        ),
        # ═══ C06 · 关系与代码对应 · 多选 ═══
        note(
            model,
            [
                "C06",
                "choice",
                "以下关于 UML 类间关系与 Java 代码的对应，哪些是正确的？（多选）",
                "泛化（空心△实线）= extends||实现（空心△虚线）= implements||关联（实线）= 一个类持有另一个类的字段||依赖（虚线箭头）= 方法参数或局部变量中使用||聚合（空心◇）= 部分生命周期绑定整体||组合（实心◆）= 部分不可脱离整体独立存在",
                "1||2||3||4||6",
                "注意 5 是错的——聚合是弱拥有，部分可以独立存在（如课程和学生：学生不上这门课也存在）。6 是正确的——组合是强拥有，部分随整体创建和销毁。关联 vs 依赖的关键区别：关联是持久持有（字段），依赖是临时使用（方法参数）。",
                "",
                "",
                "",
            ],
            ["ch3", "uml", "relationships", "code", "choice", "multi"],
        ),
        # ═══ F01 · 可见性符号 · 填空 ═══
        note(
            model,
            [
                "F01",
                "fill",
                "UML 可见性标记与 Java 修饰符对应：{{c1::+}} = public（全局访问），{{c2::-}} = private（仅本类），{{c3::#}} = protected（本类+同包+子类），{{c4::~}} = default（本类+同包）。类图中属性格式为 {{c5::可见性 名称: 类型}}，方法格式为 {{c6::可见性 名称(参数: 类型): 返回类型}}。",
                "",
                "+||-||#||~||可见性 名称: 类型||可见性 名称(参数: 类型): 返回类型",
                "可见性标记是考试常客——四个符号必须能默写。属性/方法里类型写在冒号后面，不是前面（与 Java 声明顺序相反）。",
                "",
                "",
                "",
            ],
            ["ch3", "uml", "visibility", "fill", "multi-cloze"],
        ),
        # ═══ F02 · 六种关系速记 · 填空 ═══
        note(
            model,
            [
                "F02",
                "fill",
                "UML 六种类间关系：{{c1::泛化}}(Generalization，空心△实线，extends)、{{c2::实现}}(Realization，空心△虚线，implements)、{{c3::关联}}(Association，实线，字段持有)、{{c4::聚合}}(Aggregation，空心◇实线，弱拥有)、{{c5::组合}}(Composition，实心◆实线，强拥有)、{{c6::依赖}}(Dependency，虚线箭头，临时使用)。用虚线的是{{c7::依赖}}和{{c8::实现}}；用菱形的是{{c9::聚合}}和{{c10::组合}}。",
                "",
                "泛化||实现||关联||聚合||组合||依赖||依赖||实现||聚合||组合",
                "从强到弱的关系强度：泛化/实现 > 组合 > 聚合 > 关联 > 依赖。泛化/实现是编译期确定的类型关系，组合/聚合/关联是运行时对象间的关系，依赖是最弱的临时关系。",
                "",
                "",
                "",
            ],
            ["ch3", "uml", "relationships", "fill", "multi-cloze"],
        ),
        # ═══ Q01 · 完整 UML 类图分析 · 问答 ═══
        note(
            model,
            [
                "Q01",
                "qa",
                "画出飞机大战中 Hero、Enemy、Bullet 三个类的 UML 类图，标明可见性标记、属性类型、方法签名，以及三者之间的关系（用正确的 UML 箭头）。",
                "",
                "Hero 类：-x: int, -y: int, -hp: int, -weapon: Weapon（组合◆——Hero 销毁 Weapon 也销毁）, -bullets: Bullet[]（关联——Hero 持有子弹引用）。+fire(): void, +move(dx:int): void, +takeDamage(d:int): void。Enemy 类：-x: int, -y: int, -hp: int, -speed: int。+move(): void, +takeDamage(d:int): void, +isDead(): boolean。关系：Hero —— Enemy（关联——Hero 可能持有对当前锁定敌机的引用，或在碰撞检测时作为参数传入），二者的碰撞检测在 GamePanel 中进行。Bullet 类：-x: int, -y: int, -speed: int。+move(): void, +isOffScreen(): boolean。Hero —— Bullet（关联——Hero 持有 Bullet[] 字段）。Hero 的 fire() 方法依赖（虚线）GameConfig.getBulletSpeed()——这是临时调用，不持有引用。",
                "UML 考试常见丢分点：① 箭头方向画反（泛化/实现箭头指向父类/接口，不是子类）；② 菱形方向画反（菱形在整体端）；③ 组合 vs 聚合混用（判断标准是「部分能否独立存在」）；④ 依赖用实线画（依赖必须虚线）。",
                "",
                "",
                "",
            ],
            ["ch3", "uml", "class-diagram", "full", "qa"],
        ),

        # ═══════════ 对象与类 ═══════════
        # ═══ C07 · 对象定义 · 单选 ═══
        note(
            model,
            [
                "C07",
                "choice",
                "面向对象中，对象（Object）的三个核心特征是什么？",
                "类名、构造方法、析构方法||标识符、属性（状态）、操作（行为）||封装、继承、多态||字段、方法、内部类",
                "2",
                "对象三特征：① 标识符（identity）——唯一区别其他对象（即使两个对象所有属性相等，标识符也不同，如两个 Enemy 的堆地址不同）；② 属性/状态——描述对象静态特征的数据，即成员变量；③ 操作/行为——描述对象动态特征的功能，即成员方法。封装/继承/多态是 OOP 三大特性（类的层面），不是对象的特征。",
                "",
                "",
                "",
            ],
            ["ch3", "object", "definition", "choice"],
        ),
        # ═══ C08 · 类 vs 对象 · 单选 ═══
        note(
            model,
            [
                "C08",
                "choice",
                "关于类和对象的关系，以下哪项描述是错误的？",
                "类是对象的模板/蓝图||对象是类的实例||类是动态的，在运行时创建；对象是静态的，在编译期确定||一个类可以创建多个对象",
                "3",
                "正确关系：类是静态的——编译期就已定义，类的关系和语义在程序设计时确定。对象是动态的——运行时通过 new 创建、被修改、被 GC 回收。类与对象的对照：同一类的不同对象有不同的标识符和属性值，但共享相同的类定义。",
                "",
                "",
                "",
            ],
            ["ch3", "class", "vs-object", "choice"],
        ),

        # ═══════════ 封装 ═══════════
        # ═══ C09 · 封装目的 · 单选 ═══
        note(
            model,
            [
                "C09",
                "choice",
                "封装（Encapsulation）使用 private 字段 + public getter/setter 模式，其最核心的设计目的是什么？",
                "让代码看起来更专业||保护对象内部状态的不变式（invariant），控制数据访问权限||提高程序运行速度||让外部调用者不能看到任何数据",
                "2",
                "封装的核心目的：保护不变式——类自身保证内部状态始终合法。如 age 字段为 private，setAge 中校验 0~150，外部无法绕过直接设 age=-30。其他价值：① 隔离变化——内部实现可改而不影响调用方；② 控制访问粒度——可以只提供 getter（只读）或只提供 setter（只写）。封装 ≠ 完全隐藏——是「有控制的暴露」。",
                "",
                "",
                "",
            ],
            ["ch3", "encapsulation", "purpose", "choice"],
        ),

        # ═══════════ 构造方法与 this ═══════════
        # ═══ C10 · 默认构造 · 单选 ═══
        note(
            model,
            [
                "C10",
                "choice",
                "关于 Java 构造方法（Constructor），以下哪项是正确的？",
                "构造方法与类同名，但可以声明返回类型为 void||如果没写任何构造方法，编译器自动生成无参默认构造方法||一个类只能有一个构造方法||构造方法可以用 return 语句返回值",
                "2",
                "构造方法规则：① 与类同名，不写返回类型（包括 void）；② new 时自动调用，负责初始化字段；③ 可重载（overload）——一个类可以有多个构造方法；④ 不能有 return 语句返回值（可以有单独的 return; 提前退出，极罕见）；⑤ 默认构造方法——在你没有定义任何构造方法时编译器自动添加无参 public 构造。一旦你定义了任何构造方法，默认构造就不再生成了。",
                "",
                "",
                "",
            ],
            ["ch3", "constructor", "default", "choice"],
        ),
        # ═══ C11 · this 用途 · 多选 ═══
        note(
            model,
            [
                "C11",
                "choice",
                "Java 中 this 关键字有哪些合法用途？（多选）",
                "在成员方法中区分同名的成员变量和局部变量||在构造方法中调用本类的另一个构造方法（this(...)）||在静态方法中引用当前对象||调用本类的其他成员方法（this.method()）||获取当前对象的哈希码",
                "1||2||4",
                "this 三大用途：① 区分成员变量和同名参数（this.x = x）；② 构造方法中调用其他构造方法 this(...)——必须是第一条语句，必须至少有一个构造方法不用 this 作为出口；③ 调用本类其他方法 this.method()。3 是错的——静态方法中没有 this（静态方法调用时可能不存在任何对象）。5 是错的——获取哈希码用 hashCode()，与 this 无关。",
                "",
                "",
                "",
            ],
            ["ch3", "this", "usage", "choice", "multi"],
        ),

        # ═══════════ 访问控制 ═══════════
        # ═══ C12 · 四档访问权限 · 单选 ═══
        note(
            model,
            [
                "C12",
                "choice",
                "Java 中 default（不写修饰符）的访问权限范围是什么？",
                "只有本类内部||本类 + 同一个包中的所有类||本类 + 同包 + 所有子类||任何类都可以访问",
                "2",
                "四档访问权限范围：private = 仅本类；default（不写）= 本类 + 同包；protected = 本类 + 同包 + 子类（包括跨包子类）；public = 所有类。default 的关键限制：跨包子类不能访问父类的 default 成员——这是 default 和 protected 的核心区别。",
                "",
                "",
                "",
            ],
            ["ch3", "access", "default", "choice"],
        ),
        # ═══ C13 · 跨包继承访问 · 单选 ═══
        note(
            model,
            [
                "C13",
                "choice",
                "在包 p1 中定义 class A { protected int x; }，在包 p2 中定义 class B extends A。B 能访问 x 吗？p2 中的其他类 C（非 A 子类）能通过 B 的实例访问 x 吗？",
                "B 能访问，C 也能通过 B 访问||B 不能访问，C 也不能||B 能访问（作为子类继承），C 不能（不是子类）||B 不能访问，但 C 能通过 B 访问",
                "3",
                "protected 对于跨包子类：子类自身可以访问从父类继承的 protected 成员（通过 this 直接使用）。但非子类不能通过子类实例访问——这是 protected 的精妙之处：它不是说「任何类都可以通过子类对象访问」，而是「子类自身可以使用继承来的 protected 成员」。",
                "",
                "",
                "",
            ],
            ["ch3", "access", "protected", "cross-package", "choice"],
        ),

        # ═══════════ static ═══════════
        # ═══ C14 · static 内存 · 单选 ═══
        note(
            model,
            [
                "C14",
                "choice",
                "关于 Java 的 static 修饰符，以下哪项描述是错误的？",
                "静态字段在类加载时初始化，先于任何对象存在||静态方法可以访问实例字段||所有对象共享同一份静态字段||静态块（static{}）在类加载时执行且仅执行一次",
                "2",
                "static 三大铁律：① 静态方法不能访问实例成员（字段/方法）——因为静态方法通过类名调用时可能没有对象存在；② 实例方法可以访问静态成员——因为类加载时静态成员已在内存中；③ 静态字段在方法区只有一份副本，所有对象共享。静态块的执行：类加载时按书写顺序执行，无论创建多少对象只执行一次。",
                "",
                "",
                "",
            ],
            ["ch3", "static", "rules", "choice"],
        ),
        # ═══ C15 · static 破坏 OOP · 单选 ═══
        note(
            model,
            [
                "C15",
                "choice",
                "static 成员是否破坏了面向对象的「封装」特性？为什么？",
                "是，因为 static 是全局变量，任何类都能直接访问||是，因为 static 方法不需要对象就能调用，违背了「一切皆对象」||否，static 只是说明成员属于类而非实例，访问控制（private static）仍然生效||否，因为 Java 中 static 很少使用",
                "3",
                "static 不破坏封装。封装的核心是访问控制——限制谁能读/写数据。private static 字段仍然只能在本类内部访问，外部无法直接修改。static 解决的是「ownership」问题（属于类还是实例），而非「visibility」问题（谁能看到）。两者正交：可以 private static（只有类自己能修改的共享数据）、public static（对外公开的类常量）、public 实例字段（Bad Practice）。",
                "",
                "",
                "",
            ],
            ["ch3", "static", "encapsulation", "choice"],
        ),

        # ═══════════ 对象数组 ═══════════
        # ═══ C16 · 对象数组本质 · 单选 ═══
        note(
            model,
            [
                "C16",
                "choice",
                "执行 Enemy[] enemies = new Enemy[5]; 后，enemies[0] 的值是什么？",
                "一个新的 Enemy 对象，所有字段为默认值||null||0||编译错误",
                "2",
                "new Enemy[5] 只分配了 5 个引用槽，没有创建任何 Enemy 对象——每个槽初始值为 null。必须逐个 new Enemy(...) 填入：enemies[0] = new Enemy(100, 0, 3)。这与 C 中 int* arr = malloc(5 * sizeof(int*)) 后每个槽是未初始化指针不同——Java 保证引用数组初始化为 null，基本类型数组初始化为 0/false。",
                "",
                "",
                "",
            ],
            ["ch3", "array", "object", "null", "choice"],
        ),
        # ═══ C17 · 二维不规则数组 · 单选 ═══
        note(
            model,
            [
                "C17",
                "choice",
                "int[][] arr = new int[3][]; 这行代码执行后，arr[0] 的值是什么？能否直接写 arr[0][0] = 1？",
                "arr[0] 是长度为 0 的数组，可以写||arr[0] 是 null，不能写——必须先 arr[0] = new int[...]||arr[0] 是 new int[3]，可以写||编译错误：第二维长度不能省略",
                "2",
                "new int[3][] 只创建了外层数组（3 个引用槽），每个槽初始为 null。第二维的每个子数组需要单独 new：arr[0] = new int[5]; arr[1] = new int[3]; arr[2] = new int[7]。这正是 Java 支持「不规则矩阵」的方式——每行长度可以不同。Java 不允许写 new int[][3]（第二维长度不能先于第一维指定）。",
                "",
                "",
                "",
            ],
            ["ch3", "array", "2d", "irregular", "choice"],
        ),

        # ═══ F03 · 构造方法语法 · 填空 ═══
        note(
            model,
            [
                "F03",
                "fill",
                "构造方法的语法规则：与{{c1::类名同名}}，{{c2::不写返回类型}}（包括 void），使用{{c3::new}}关键字调用。如果类中没有定义任何构造方法，编译器自动生成{{c4::无参默认构造方法}}。一旦定义了任何构造方法，默认构造{{c5::不再自动生成}}。在构造方法中用{{c6::this(参数)}}调用本类的另一个构造方法，该语句必须是{{c7::第一条语句}}。",
                "",
                "类名同名||不写返回类型||new||无参默认构造方法||不再自动生成||this(参数)||第一条语句",
                "构造方法可以重载（overload）——多个构造方法用不同参数列表区分。this(...) 调用链不能形成循环——必须至少有一个不用 this 的构造方法作为终点。",
                "",
                "",
                "",
            ],
            ["ch3", "constructor", "syntax", "fill", "multi-cloze"],
        ),
        # ═══ F04 · 访问权限四档 · 填空 ═══
        note(
            model,
            [
                "F04",
                "fill",
                "Java 四种访问修饰符的可见范围：{{c1::private}} = 仅本类；{{c2::default}}(不写) = 本类+同包；{{c3::protected}} = 本类+同包+子类（包括跨包）；{{c4::public}} = 所有类。字段默认应使用{{c5::private}}，通过{{c6::getter/setter}}方法暴露。",
                "",
                "private||default||protected||public||private||getter/setter",
                "区别 protected 和 default 的关键场景：跨包子类。在包 p1 的 A 中定义 protected int x，包 p2 的 B extends A——B 内部可以访问 x；如果 x 是 default，B 不能访问（default 不跨包）。",
                "",
                "",
                "",
            ],
            ["ch3", "access", "modifiers", "fill", "multi-cloze"],
        ),
        # ═══ F05 · static 三种用法 · 填空 ═══
        note(
            model,
            [
                "F05",
                "fill",
                "static 的三种用法：① {{c1::静态字段}}——属于类，所有对象共享唯一副本，在类加载时分配在{{c2::方法区}}；② {{c3::静态方法}}——通过{{c4::类名}}调用，不能访问{{c5::实例成员}}（字段/方法）；③ {{c6::静态块}}——类加载时执行且仅执行{{c7::一次}}，按书写顺序执行，用于初始化静态成员。",
                "",
                "静态字段||方法区||静态方法||类名||实例成员||静态块||一次",
                "严格区分：实例字段 → 每个对象一份（堆）；静态字段 → 整个类一份（方法区）。静态方法中不能用 this/super。静态块不在任何方法内——直接写在类体中。",
                "",
                "",
                "",
            ],
            ["ch3", "static", "three-uses", "fill", "multi-cloze"],
        ),
        # ═══ F06 · 对象数组 · 填空 ═══
        note(
            model,
            [
                "F06",
                "fill",
                "对象数组：声明 {{c1::Enemy[] enemies;}}，动态初始化 {{c2::new Enemy[5];}} 只分配引用槽，每个槽初始化为{{c3::null}}。必须手动创建对象：{{c4::enemies[0] = new Enemy(100, 0, 3);}}。静态初始化可直接写 {{c5::{new Enemy(...), new Enemy(...)}}}。访问未初始化的槽（null）调用方法会抛出{{c6::NullPointerException}}。",
                "",
                "Enemy[] enemies;||new Enemy[5];||null||enemies[0] = new Enemy(100, 0, 3);||{new Enemy(...), new Enemy(...)}||NullPointerException",
                "对象数组存的是引用（地址），不是对象本身的数据。Rust 对比：Vec<Enemy> 存的是对象本身（栈上或堆上连续排列），Java 的 Enemy[] 存的是指向堆上各处对象的指针数组——类似 Rust 的 Vec<Box<Enemy>>。",
                "",
                "",
                "",
            ],
            ["ch3", "array", "object", "fill", "multi-cloze"],
        ),

        # ═══ Q02 · 封装完整示例 · 问答 ═══
        note(
            model,
            [
                "Q02",
                "qa",
                "写出一个完整的 Java 类 Enemy，体现封装（private 字段 + getter/setter）、构造方法重载、this 的用法。",
                "",
                "public class Enemy {\n    private int x, y, hp, speed;\n    private static int totalCount = 0;  // 静态字段：统计所有敌机数量\n\n    // 完整构造\n    public Enemy(int x, int y, int hp, int speed) {\n        this.x = x; this.y = y;\n        this.hp = hp; this.speed = speed;\n        totalCount++;\n    }\n    // 简化构造：默认 hp=50\n    public Enemy(int x, int y, int speed) {\n        this(x, y, 50, speed);  // 调用完整构造\n    }\n    // getter（只读）\n    public int getX() { return x; }\n    public int getY() { return y; }\n    public int getHp() { return hp; }\n    // setter 带校验\n    public void takeDamage(int dmg) {\n        hp = Math.max(0, hp - dmg);\n        if (hp == 0) destroy();\n    }\n    private void destroy() { totalCount--; }\n    public boolean isDead() { return hp <= 0; }\n    public static int getTotalCount() { return totalCount; }\n}",
                "关键考察点：① private 字段 + public getter/setter；② this 区分字段和参数；③ this(x,y,50,speed) 构造方法链——必须在第一行；④ static totalCount 所有对象共享——在构造方法中++，在 destroy() 中--；⑤ destroy() 是 private——外部不能直接销毁敌机，只能通过 takeDamage 触发。",
                "",
                "",
                "",
            ],
            ["ch3", "encapsulation", "example", "qa"],
        ),
        # ═══ Q03 · static 调用限制 · 问答 ═══
        note(
            model,
            [
                "Q03",
                "qa",
                "解释为什么静态方法不能访问实例字段，而实例方法可以访问静态字段。从类加载和对象创建的时间线说明。",
                "",
                "时间线：① JVM 启动 → 加载类 → 静态成员分配内存（方法区）→ 执行静态块。此时还没有任何对象存在。② 代码执行到 new Enemy() → 堆上分配对象内存 → 调用构造方法初始化实例字段 → 返回引用。静态方法在阶段①结束后就可以通过类名调用了——此时实例字段还不存在，所以静态方法不能访问实例成员。实例方法在阶段②通过对象调用——此时静态字段早已存在，所以实例方法可以访问静态成员。根本原因：静态成员与类同生命周期，实例成员与对象同生命周期，类的生命周期覆盖了对象。",
                "反证法：如果静态方法可以访问实例字段 x，那么 Enemy.printX() 调用时 JVM 应该取哪个对象的 x？没有任何对象存在，访问无意义——编译器直接禁止。",
                "",
                "",
                "",
            ],
            ["ch3", "static", "lifecycle", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 第三章 类和对象", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
