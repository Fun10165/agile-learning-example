from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400514
OUTPUT = ROOT / "anki-第四章-继承与接口.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════ 继承 ═══════════
        # ═══ C01 · extends 语义 · 单选 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "关于 Java 继承（extends），以下哪项描述是正确的？",
                "子类继承父类的所有成员，包括 private 字段和方法||子类可以直接访问父类的 private 字段||子类继承父类所有非 private 成员，但不继承构造方法||子类可以同时 extends 多个父类",
                "3",
                "子类继承父类的所有非 private 字段和方法。private 成员在子类中存在但不直接可见——子类只能通过父类的 public/protected getter/setter 间接访问。构造方法不被继承——子类必须通过 super(...) 调用父类构造。Java 类只允许单继承（extends 一个类）。",
                "",
                "",
                "",
            ],
            ["ch4", "inheritance", "extends", "choice"],
        ),
        # ═══ C02 · super 构造第一行 · 单选 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "为什么 super(...) 必须是子类构造方法的第一条语句？",
                "这是 Java 语法规定的惯例，没有技术原因||因为子类字段初始化可能用到父类字段，父类必须已初始化完毕||因为 JVM 把父类和子类的构造方法编译为同一个方法体||为了让代码好看",
                "2",
                "JVM 在堆上分配对象时，父类字段在子类字段之下的内存区域。如果子类构造方法体在 super(...) 之前执行了代码，这时代码可能访问到未初始化的父类字段（如调用一个继承来的方法读到 hp=0）。super(...) 第一行的强制规定从语法层面杜绝了这一问题——确保在执行子类任何代码之前，父类已经处于合法状态。",
                "",
                "",
                "",
            ],
            ["ch4", "super", "constructor", "choice"],
        ),
        # ═══ C03 · super() 自动插入 · 单选 ═══
        note(
            model,
            [
                "C03",
                "choice",
                "以下代码为什么会编译错误？\nclass Enemy { public Enemy(int hp) {} }\nclass BossEnemy extends Enemy { }",
                "BossEnemy 没有写 extends Enemy 的完整语法||Enemy 没有无参构造，编译器自动插入的 super() 找不到匹配的父类构造||BossEnemy 不能继承 Enemy 的构造方法||父类 Enemy 的构造方法是 public 导致子类无法访问",
                "2",
                "BossEnemy 没写构造方法 → 编译器自动生成无参构造 public BossEnemy() { super(); }。但 Enemy 只有 Enemy(int hp)，没有 Enemy() → super() 找不到匹配的父类构造 → 编译错误。解决方案：在 BossEnemy 中显式写构造方法，第一行用 super(hp值) 调用父类有参构造。",
                "",
                "",
                "",
            ],
            ["ch4", "super", "auto-insert", "choice"],
        ),
        # ═══ C04 · super 三用途 · 多选 ═══
        note(
            model,
            [
                "C04",
                "choice",
                "Java 中 super 关键字有哪些合法用途？（多选）",
                "super(参数) —— 在子类构造方法中调用父类构造方法||super.field —— 访问父类中被同名字段隐藏的字段||super.method() —— 调用父类中被覆盖的方法||在静态方法中使用 super 调用父类的静态方法||super.new() —— 创建父类的新实例",
                "1||2||3",
                "super 三用途与 this 对应：① super(参数) 调用父类构造——必须是第一行；② super.field 访问被隐藏的父类字段（父类字段不能是 private）；③ super.method() 调用被覆盖的父类方法——静态绑定，不查 vtable。4 错在静态方法中没有 super（静态方法没有当前对象，自然没有父对象）。5 纯属虚构。",
                "",
                "",
                "",
            ],
            ["ch4", "super", "three-uses", "choice", "multi"],
        ),
        # ═══ C05 · 继承优缺点 · 多选 ═══
        note(
            model,
            [
                "C05",
                "choice",
                "关于继承的优缺点，以下哪些是正确的？（多选）",
                "提高代码复用性——子类无需重复写父类已有的方法||提高程序扩展性——加新子类不需改动已有代码||是多态的基础——父类引用可指向子类对象||降低类的耦合性——父类的改变不影响子类||子类可以同时继承多个父类的方法，具有高度灵活性",
                "1||2||3",
                "继承优点：代码复用、扩展性、多态基础。缺点：增强耦合——父类改变会影响所有子类（因此 4 错）。Java 类只允许单继承（因此 5 错）。设计原则：优先使用组合（composition）而非继承（inheritance）来达到复用目的——这是 GoF 设计模式的核心建议之一。",
                "",
                "",
                "",
            ],
            ["ch4", "inheritance", "pros-cons", "choice", "multi"],
        ),

        # ═══════════ 抽象类 ═══════════
        # ═══ C06 · 抽象类规则 · 单选 ═══
        note(
            model,
            [
                "C06",
                "choice",
                "关于抽象类（abstract class），以下哪项描述是错误的？",
                "抽象类用 abstract 关键字修饰||抽象类不能实例化（new）||抽象类可以有构造方法||抽象类中的所有方法都必须是抽象方法",
                "4",
                "抽象类三条铁律：① 不能实例化；② 可以有构造方法（供子类 super() 调用）；③ 可以混合包含抽象方法和具体方法——具体方法被子类继承复用，抽象方法强制子类实现。错误项 4：抽象类中完全可以有已经实现的普通方法，如 Enemy 的 takeDamage()，所有敌机扣血逻辑相同，写死在抽象类中。",
                "",
                "",
                "",
            ],
            ["ch4", "abstract", "rules", "choice"],
        ),
        # ═══ C07 · 抽象类 vs 接口 · 单选 ═══
        note(
            model,
            [
                "C07",
                "choice",
                "抽象类和接口的关键区别是什么？",
                "抽象类可以有构造方法，接口没有||抽象类中的方法全部抽象，接口可以有具体方法||抽象类可以被继承，接口不能||抽象类支持多继承，接口不支持",
                "1",
                "核心区别表：① 抽象类可以有字段和构造方法，接口无（只有 static final 常量）；② 抽象类可以有具体方法和抽象方法混合，接口方法默认都是 public abstract；③ 类只能 extends 一个抽象类，但可以 implements 多个接口；④ 语义不同——抽象类是「is-a」关系（定义了骨架），接口是「can-do」能力契约。注意选项 2 反过来才对。",
                "",
                "",
                "",
            ],
            ["ch4", "abstract", "vs-interface", "choice"],
        ),

        # ═══════════ 接口 ═══════════
        # ═══ C08 · interface 定义 · 单选 ═══
        note(
            model,
            [
                "C08",
                "choice",
                "关于 Java 接口（interface），以下哪项是正确的？",
                "接口中的方法可以有方法体||接口中的方法默认是 public abstract||接口中可以有 private 字段||一个类只能实现一个接口",
                "2",
                "接口规则：① 方法默认 public abstract——不写修饰符也一样；② 无字段（实例变量）——只有 static final 常量；③ 无构造方法——接口不能 new；④ 类可以 implements 多个接口，接口可以 extends 多个接口。接口是纯粹的「能力契约」——定义能做什么，不关心怎么做。",
                "",
                "",
                "",
            ],
            ["ch4", "interface", "definition", "choice"],
        ),

        # ═══════════ 多态 ═══════════
        # ═══ C09 · 多态三条件 · 多选 ═══
        note(
            model,
            [
                "C09",
                "choice",
                "Java 中实现多态的三个必要条件是什么？（多选）",
                "继承（extends）或实现（implements）||重写（@Override）——子类覆盖父类方法||父类/接口引用指向子类对象||父类必须是抽象类||子类必须用 super 调用父类方法",
                "1||2||3",
                "三必要条件：① 继承/实现——子类获得父类的类型身份；② 重写——子类提供与父类签名相同但行为不同的方法；③ 父类引用指向子类对象——如 Enemy e = new BossEnemy()。缺少任何一个都无法形成多态调用。注意 4 不对——普通类和接口一样可以实现多态。注意 5 不对——不调用 super 照样多态。",
                "",
                "",
                "",
            ],
            ["ch4", "polymorphism", "conditions", "choice", "multi"],
        ),
        # ═══ C10 · 多态三种实现 · 单选 ═══
        note(
            model,
            [
                "C10",
                "choice",
                "Java 中多态的三种实现方式分别是什么？它们的递进关系是什么？",
                "重载、重写、覆盖——并列关系||重写、抽象类、接口——从同族内差异化到跨继承树的共同能力||继承、封装、多态——三大特性||父类、子类、孙类——继承层次",
                "2",
                "三种实现方式递进：① 重写（@Override）——同一父类下不同子类的方法差异化，调用者知道是 Enemy 族系；② 抽象类——父类定义了「所有子类必须能做什么」的规范，调用者只知道父类规范；③ 接口——定义跨继承树的纯粹能力契约，调用者完全不关心对象的类是什么，只关心「能 fire 吗」。递进方向：耦合越来越低，抽象程度越来越高。",
                "",
                "",
                "",
            ],
            ["ch4", "polymorphism", "three-ways", "choice"],
        ),

        # ═══════════ 多继承问题 ═══════════
        # ═══ C11 · 菱形问题 · 单选 ═══
        note(
            model,
            [
                "C11",
                "choice",
                "Java 为什么禁止类的多继承（菱形问题 / Diamond Problem）？",
                "因为多继承会让编译速度变慢||因为 JVM 不支持多个父类的内存布局||因为如果多个父类有同名方法/字段，子类调用时产生歧义||因为 Java 历史原因，没有技术难度只是没实现",
                "3",
                "菱形问题：B 和 C 都继承 A，D 同时继承 B 和 C。如果 B 和 C 都覆盖了 A 的 method()，D 调用 method() 时 JVM 无法确定执行哪个。C++ 允许但需要虚继承机制解决，规则复杂。Java 选择禁止类多继承，同时让接口支持多继承——因为接口无字段、无方法体，即使两个父接口有同名方法签名，实现类只用一个实现同时满足两者，不产生歧义。",
                "",
                "",
                "",
            ],
            ["ch4", "diamond", "multiple-inheritance", "choice"],
        ),
        # ═══ C12 · 接口多继承 · 单选 ═══
        note(
            model,
            [
                "C12",
                "choice",
                "Daughter extends Father, Mother（Father 和 Mother 都是接口）。如果两者都有 void smile()，Daughter 的实现类 Girl 需要写几个 smile()？",
                "两个——分别实现 Father.smile() 和 Mother.smile()||一个——一个实现同时满足两个父接口||零个——接口多继承会自动合并相同方法||编译错误——两个接口有同名方法会导致冲突",
                "2",
                "因为接口方法没有方法体，两个 smile() 只是「签名契约」。Girl 写一个 smile() 就同时满足 Father 和 Mother 的要求。这与类的多继承有本质区别——类的多继承中，两个父类各自的 smile() 可能有不同的实现，JVM 无法确定用哪个。接口多继承不会冲突的根本原因就在于「只有签名没有实现」。",
                "",
                "",
                "",
            ],
            ["ch4", "interface", "multi-extends", "choice"],
        ),
        # ═══ C13 · 内部类多继承 · 单选 ═══
        note(
            model,
            [
                "C13",
                "choice",
                "用内部类实现多继承效果的原理是什么？它是一种真正的多继承吗？",
                "内部类直接继承了多个父类，是真正的多继承||内部类各自继承不同父类，外部类通过组合获得多个父类的功能——本质是组合而非继承||内部类只能继承一个父类，不能用来模拟多继承||内部类通过反射绕过单继承限制",
                "2",
                "内部类方案的本质：在 Son 中定义 Father_Inner extends Father 和 Mother_Inner extends Mother，Son 通过 new Father_Inner().strong() 和 new Mother_Inner().smart() 调用——这是组合（Composition），不是多继承。Son 本身并没有继承 Father 或 Mother。优点：灵活性高，可选择性暴露父类方法；缺点：代码冗长，不建立类型关系（Son 不是 Father 也不是 Mother）。",
                "",
                "",
                "",
            ],
            ["ch4", "inner-class", "multi-inheritance", "choice"],
        ),

        # ═══════════ Object 超类 ═══════════
        # ═══ C14 · Object 根类 · 单选 ═══
        note(
            model,
            [
                "C14",
                "choice",
                "关于 java.lang.Object 类，以下哪项描述是错误的？",
                "Object 是所有 Java 类的最终祖先||如果一个类没有显式 extends，编译器自动让它 extends Object||Object 类位于 java.lang 包，自动导入||Object 是一个抽象类，不能直接用 new Object() 创建实例",
                "4",
                "Object 是普通具体类，可以 new Object()。它是所有类的根——每个类都直接或间接继承 Object，因此每个 Java 对象都拥有 Object 的方法（toString、equals、hashCode、getClass 等）。Object 类型的变量可以引用任何对象（泛型容器用途），但要调用具体类型的方法需要强制转型。",
                "",
                "",
                "",
            ],
            ["ch4", "object", "root", "choice"],
        ),
        # ═══ C15 · equals 默认行为 · 单选 ═══
        note(
            model,
            [
                "C15",
                "choice",
                "Object 的默认 equals() 方法比较的是什么？为什么通常需要覆盖它？",
                "比较两个对象的内容（字段值）是否相等||比较两个对象的 hashCode 是否相等||比较两个引用是否指向同一个堆地址（== 语义）||比较两个对象是否是同一个类的实例",
                "3",
                "Object.equals() 的默认实现就是 this == obj——只判断引用地址是否相同。这意味着 new Enemy(100,0,50,3).equals(new Enemy(100,0,50,3)) 返回 false，虽然内容完全一样但它们是两个不同对象。如果你需要按内容比较（如分数排行榜中判断是否是同一玩家），必须 @Override equals()。覆盖 equals 时必须同时覆盖 hashCode()——这是 Java 的硬契约：相等对象必须有相同的 hashCode。",
                "",
                "",
                "",
            ],
            ["ch4", "object", "equals", "choice"],
        ),

        # ═══════════ 异常继承框架 ═══════════
        # ═══ C16 · Throwable 体系 · 单选 ═══
        note(
            model,
            [
                "C16",
                "choice",
                "Java 异常体系中，Error 和 Exception 的最大区别是什么？",
                "Error 是受检异常，Exception 是非受检异常||Error 表示严重系统错误（如 OOM），程序一般无法处理；Exception 表示可被捕获处理的程序级错误||Error 是 Exception 的子类||Error 需要 try-catch，Exception 不需要",
                "2",
                "Throwable 体系：Error（如 OutOfMemoryError、StackOverflowError）——严重系统级错误，程序无法也不应该尝试恢复。Exception 分为 RuntimeException（非受检，编译器不强制处理）和受检异常（如 IOException、SQLException，编译器强制 try-catch 或 throws）。Error 既不是受检也不是非受检——它不在 exception handling 的通常框架中讨论。",
                "",
                "",
                "",
            ],
            ["ch4", "exception", "throwable", "choice"],
        ),
        # ═══ C17 · 自定义异常 · 单选 ═══
        note(
            model,
            [
                "C17",
                "choice",
                "如果要定义一个受检异常（Checked Exception），应该继承哪个类？",
                "Throwable||Error||Exception（非 RuntimeException）||RuntimeException",
                "3",
                "继承规则：继承 Exception（但非 RuntimeException）→ 受检异常——编译器强制调用者处理。继承 RuntimeException → 非受检异常——编译器不强制。继承 Error → 不推荐（Error 用于 JVM 级错误）。自定义异常通常提供两个构造方法：无参构造（super()）和带消息的构造（super(str)），消息可通过 getMessage() 获取。",
                "",
                "",
                "",
            ],
            ["ch4", "exception", "custom", "choice"],
        ),

        # ═══ F01 · extends 语法 · 填空 ═══
        note(
            model,
            [
                "F01",
                "fill",
                "Java 中继承使用{{c1::extends}}关键字。子类构造方法通过{{c2::super(参数)}}调用父类构造，该语句必须是{{c3::第一条语句}}。如果子类构造未显式写 super，编译器自动插入{{c4::super();}}——若父类没有无参构造则{{c5::编译错误}}。子类覆盖父类方法时使用{{c6::@Override}}注解让编译器检查签名正确性。",
                "",
                "extends||super(参数)||第一条语句||super();||编译错误||@Override",
                "继承的优点：代码复用、扩展性、多态基础。缺点：增强耦合——父类改变影响所有子类。设计建议：优先组合（has-a）而非继承（is-a）。",
                "",
                "",
                "",
            ],
            ["ch4", "extends", "syntax", "fill", "multi-cloze"],
        ),
        # ═══ F02 · 抽象类与接口对比 · 填空 ═══
        note(
            model,
            [
                "F02",
                "fill",
                "抽象类 vs 接口：抽象类用{{c1::abstract class}}声明，{{c2::可以}}(可以/不可以)有实例字段和构造方法；接口用{{c3::interface}}声明，{{c4::不可以}}(可以/不可以)有实例字段和构造方法。类只能{{c5::extends}}一个抽象类，但可以{{c6::implements}}多个接口。抽象类是{{c7::is-a}}关系，接口是{{c8::can-do}}能力契约。",
                "",
                "abstract class||可以||interface||不可以||extends||implements||is-a||can-do",
                "为什么需要接口？抽象类解决不了多继承——BossEnemy 既是一种 Enemy（is-a），又是 Drawable（可绘制）和 Damagable（可受伤），后两者只能用接口表示。",
                "",
                "",
                "",
            ],
            ["ch4", "abstract", "interface", "comparison", "fill", "multi-cloze"],
        ),
        # ═══ F03 · 异常继承体系 · 填空 ═══
        note(
            model,
            [
                "F03",
                "fill",
                "Java 异常根类是{{c1::Throwable}}，下分两大分支：{{c2::Error}}（严重系统错误，如 OOM）和{{c3::Exception}}（可被捕获处理的异常）。Exception 分为：{{c4::RuntimeException}}及其子类（非受检，编译器不强制处理）和{{c5::其他 Exception}}子类（受检，编译器强制 try-catch 或 throws）。自定义受检异常继承{{c6::Exception}}，自定义非受检异常继承{{c7::RuntimeException}}。",
                "",
                "Throwable||Error||Exception||RuntimeException||其他 Exception||Exception||RuntimeException",
                "受检异常的设计哲学：文件可能不存在、网络可能断开——程序员无法控制但可以预期。编译器强制处理迫使程序员提前考虑这些场景，避免运行时崩溃。",
                "",
                "",
                "",
            ],
            ["ch4", "exception", "hierarchy", "fill", "multi-cloze"],
        ),
        # ═══ F04 · super 三用途 · 填空 ═══
        note(
            model,
            [
                "F04",
                "fill",
                "super 三用途：① {{c1::super(参数)}}——子类构造调用父类构造，必须是第一条语句；② {{c2::super.field}}——访问父类中被同名字段隐藏的字段（父类字段不能是 private）；③ {{c3::super.method()}}——调用父类中被覆盖的方法，使用静态绑定（不查 vtable）。编译器的自动插入规则：子类构造首行无 super/this → 自动加{{c4::super();}}。super(...) 和 this(...) {{c5::不能}}(能/不能)同时出现。",
                "",
                "super(参数)||super.field||super.method()||super();||不能",
                "super.method() 的典型场景：子类想「扩展」父类方法而非完全替换——子类先做自己的逻辑，再调用 super.method() 复用父类的处理。",
                "",
                "",
                "",
            ],
            ["ch4", "super", "syntax", "fill", "multi-cloze"],
        ),
        # ═══ F05 · Object 三个核心方法 · 填空 ═══
        note(
            model,
            [
                "F05",
                "fill",
                "Object 类三个最常被覆盖的方法：① {{c1::toString()}}——默认返回 类名@十六进制哈希，覆盖后返回可读描述；② {{c2::equals(Object)}}——默认实现是 {{c3::==}} （比较引用地址），覆盖后按内容比较；③ {{c4::hashCode()}}——返回对象的哈希码。铁规则：覆盖 equals 必须覆盖 hashCode——{{c5::相等对象必须有相同 hashCode}}（反之不必然）。",
                "",
                "toString()||equals(Object)||==||hashCode()||相等对象必须有相同 hashCode",
                "Object 是所有类的根——即使你没有写 extends，编译器自动让类继承 Object。Object 类型的变量可以引用任何对象（泛型容器），但要调用具体方法需要强制转型：(TargetType) obj。",
                "",
                "",
                "",
            ],
            ["ch4", "object", "methods", "fill", "multi-cloze"],
        ),

        # ═══ Q01 · 继承完整示例 · 问答 ═══
        note(
            model,
            [
                "Q01",
                "qa",
                "写出飞机大战中 Enemy（抽象类）、NormalEnemy、BossEnemy 三个类的完整继承关系代码，要求体现：extends、super(参数)、@Override、抽象方法。",
                "",
                "public abstract class Enemy {\n    protected int x, y, hp, speed;\n    public Enemy(int x, int y, int hp, int speed) {\n        this.x = x; this.y = y;\n        this.hp = hp; this.speed = speed;\n    }\n    public abstract void move();    // 抽象方法\n    public abstract int getScore();\n    public void takeDamage(int dmg) { hp = Math.max(0, hp - dmg); }\n    public boolean isDead() { return hp <= 0; }\n}\n\npublic class NormalEnemy extends Enemy {\n    public NormalEnemy(int x, int y) {\n        super(x, y, 50, 3);\n    }\n    @Override public void move() { y += speed; }\n    @Override public int getScore() { return 100; }\n}\n\npublic class BossEnemy extends Enemy {\n    private int phase;\n    public BossEnemy(int x, int y) {\n        super(x, y, 500, 2);\n        this.phase = 1;\n    }\n    @Override public void move() {\n        y += speed;\n        x += (int)(20 * Math.sin(y * 0.02));\n    }\n    @Override public int getScore() { return 2000; }\n}",
                "关键考察点：① Enemy 用 abstract class 声明——不能 new Enemy()；② Enemy 定义了两个抽象方法 move() 和 getScore()——子类必须实现；③ Enemy 也有具体方法 takeDamage()——所有子类共享；④ NormalEnemy 的构造用 super(x,y,50,3) 传递默认 hp 和 speed；⑤ BossEnemy 有自己的字段 phase；⑥ @Override 确保方法签名正确。",
                "",
                "",
                "",
            ],
            ["ch4", "inheritance", "example", "qa"],
        ),
        # ═══ Q02 · 接口与多继承 · 问答 ═══
        note(
            model,
            [
                "Q02",
                "qa",
                "用飞机大战的例子，说明接口如何解决 Java 单继承限制。BossEnemy 既是一种 Enemy，又是可射击的（Shootable）和可绘制的（Drawable）。写出完整的接口定义和类实现。",
                "",
                "public interface Drawable { void draw(); }\npublic interface Shootable { void fire(); }\n\npublic class BossEnemy extends Enemy implements Drawable, Shootable {\n    public BossEnemy(int x, int y) { super(x, y, 500, 2); }\n    @Override public void move() { ... }\n    @Override public int getScore() { return 2000; }\n    @Override public void draw() { /* 画 BOSS 像素 */ }\n    @Override public void fire() { /* BOSS 发射弹幕 */ }\n}\n\n// 多态使用\nDrawable d = new BossEnemy(400, 0);\nd.draw();           // ✅ Drawable 有 draw()\n// d.fire();        // ❌ Drawable 没有 fire()\nShootable s = new BossEnemy(400, 0);\ns.fire();           // ✅ Shootable 有 fire()\n// s.draw();        // ❌ Shootable 没有 draw()\nEnemy e = new BossEnemy(400, 0);\ne.move();           // ✅ Enemy 有 move()\n// e.fire();        // ❌ Enemy 没有 fire()",
                "关键点：BossEnemy 同时 extends Enemy 和 implements Drawable, Shootable——这是 Java 合法的方式。三个引用类型（Drawable/Shootable/Enemy）各自只能调用自己类型中声明的方法——编译器只看声明类型。接口是纯粹的「能力标签」：BossEnemy 同时是 Enemy（类型身份）+ Drawable（可画）+ Shootable（可射击），后两个标签与 Enemy 继承树完全无关。",
                "",
                "",
                "",
            ],
            ["ch4", "interface", "multi-inheritance", "example", "qa"],
        ),
        # ═══ Q03 · equals 覆盖 · 问答 ═══
        note(
            model,
            [
                "Q03",
                "qa",
                "为 Enemy 类覆盖 equals() 方法，使得两个 Enemy 对象当且仅当 x、y、hp、speed 全部相等时被视为相等。说明覆盖 equals 为什么必须同时覆盖 hashCode。",
                "",
                "@Override\npublic boolean equals(Object obj) {\n    if (this == obj) return true;         // 同一引用\n    if (!(obj instanceof Enemy)) return false; // 类型不符\n    Enemy other = (Enemy) obj;\n    return this.x == other.x && this.y == other.y\n        && this.hp == other.hp && this.speed == other.speed;\n}\n\n@Override\npublic int hashCode() {\n    return Objects.hash(x, y, hp, speed);\n}",
                "为什么必须同时覆盖 hashCode：Java 契约规定——如果 a.equals(b)，则 a.hashCode() == b.hashCode()。如果你只覆盖 equals 不覆盖 hashCode，两个 equals 为 true 的对象可能返回不同 hashCode，导致它们在 HashMap/HashSet 中行为异常——放进 HashSet 的同一个「相等」对象可能出现两份或者找不到。Objects.hash(...) 是 JDK 7 提供的便捷方法。",
                "",
                "",
                "",
            ],
            ["ch4", "object", "equals", "hashcode", "qa"],
        ),
        # ═══ Q04 · 静态类型限制 · 问答 ═══
        note(
            model,
            [
                "Q04",
                "qa",
                "Shootable s = new Hero(); 后为什么 s.fire() 可以但 s.moveUp() 不行？这和 Enemy e = new BossEnemy(); 后 e.getScore() 可以但 e.getPhase() 不行是同一条规则吗？解释原理。",
                "",
                "是同一条规则——静态类型决定可调用方法集合，与用 extends 还是 implements 无关。编译器只认声明类型：s 的类型是 Shootable，编译器只允许调用 Shootable 中声明的方法（fire），不允许 moveUp（Hero 的方法但不在 Shootable 中）。e 的类型是 Enemy，只允许调用 Enemy 的方法（getScore），不允许 getPhase（BossEnemy 的方法但不在 Enemy 中）。运行时 JVM 通过 vtable 正确分派到实际类型的实现，但编译期已过滤掉签名之外的方法。要调用静态类型之外的方法，必须强制转型：((Hero) s).moveUp() 或 ((BossEnemy) e).getPhase()。",
                "这条规则正是多态的设计精髓——调用方只需要知道接口/父类的契约，不关心具体实现类型。契约约束了调用方能做什么，但也隔离了具体实现的变化。",
                "",
                "",
                "",
            ],
            ["ch4", "static-type", "polymorphism", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 第四章 继承与接口", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
