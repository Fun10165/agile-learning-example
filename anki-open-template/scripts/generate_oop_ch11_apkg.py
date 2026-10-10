from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400521
OUTPUT = ROOT / "anki-第十一章-泛型与反射.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════ 泛型基础 ═══════════
        # ═══ C01 · 为什么泛型 · 单选 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "Java 引入泛型（Generic）解决的核心问题是什么？",
                "让代码运行更快||提供编译期类型安全检查——将类型错误从运行时提前到编译时，消除强制类型转换，让程序员编写更安全的集合代码||让 ArrayList 支持更多方法||替代 Object 类型",
                "2",
                "Java 5 之前 ArrayList 存 Object——任何类型都可放入，取出需强转。三个问题：① 无编译期类型检查（list.add(100) 不报错）；② 取出需强转（样板代码）；③ 错误延迟到运行时（ClassCastException）。泛型 = 参数化类型——类型作为参数传入，编译器自动检查。如 ArrayList<String>：add(100) 编译错误，get(0) 直接返回 String 不需强转。",
                "",
                "",
                "",
            ],
            ["ch11", "generic", "why", "choice"],
        ),
        # ═══ C02 · 泛型类 · 单选 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "关于泛型类，以下哪项是正确的？",
                "泛型类只能有一个类型参数||泛型类的类型参数不能用基本类型——Box<int> 非法，必须 Box<Integer>||泛型类中所有方法都是泛型方法||泛型类的类型参数必须在构造方法中指定",
                "2",
                "泛型类规则：① 声明语法 class Box<T> { }，在类名后尖括号中声明类型参数；② 可以有多个 T,E,K,V 等约定字母；③ 不能使用基本类型——必须用包装类，因为泛型在编译时类型擦除后所有类型参数替换为 Object；④ 泛型类中使用 T 的普通方法不算泛型方法——只有方法自己声明 <T> 的才是泛型方法；⑤ 静态方法不能使用泛型类的类型参数——必须独立声明。",
                "",
                "",
                "",
            ],
            ["ch11", "generic", "class", "choice"],
        ),
        # ═══ C03 · 泛型方法 · 单选 ═══
        note(
            model,
            [
                "C03",
                "choice",
                "以下哪个才是真正的泛型方法？为什么静态方法不能直接使用类的类型参数？",
                "class Box<T> { public void put(T t) {} }——这是泛型方法||class Util { public static <T> T getFirst(List<T> l) {} }——泛型方法在返回类型前独立声明 <T>。静态方法不能用类的 T 因为调用时可能尚未实例化该类，而 T 的类型在实例化时才确定||两者都是泛型方法||两者都不是泛型方法",
                "2",
                "区分标准：泛型方法 = 方法自己独立声明了类型参数 `<T>`（写在返回类型前面）。class Box<T> 中的 void put(T t) 只是使用了类声明的 T——不是泛型方法。静态方法限制原因：静态方法通过类名调用，不需要对象。但泛型类的类型参数 T 是在 new Box<String>() 创建对象时才确定的——没有对象就没有确定的 T，静态方法自然不能引用它。解决方案：静态方法独立声明自己的 <T>：public static <T> Box<T> create(T t)。",
                "",
                "",
                "",
            ],
            ["ch11", "generic", "method", "choice"],
        ),
        # ═══ C04 · 泛型接口 · 单选 ═══
        note(
            model,
            [
                "C04",
                "choice",
                "泛型接口的两种实现方式是什么？",
                "只有一种——实现时确定类型||① 实现时确定类型——class ScoreRepo implements Repository<ScoreEntry>；② 实现类也保持泛型——class GenericRepo<T> implements Repository<T>||必须用抽象类实现||必须用 Lambda 实现",
                "2",
                "两种实现：① 非泛型实现——实现类确定接口的泛型类型，此后接口方法返回具体类型不需强转。② 泛型实现——实现类也声明相同的类型参数，保持泛型特性，实例化时才确定类型。选择取决于业务需要——如果 Repository 专门存 ScoreEntry，方式①更简单；如果 Repository 是通用框架，方式②提供灵活性。",
                "",
                "",
                "",
            ],
            ["ch11", "generic", "interface", "choice"],
        ),

        # ═══════════ 通配符 ═══════════
        # ═══ C05 · 无协变 · 单选 ═══
        note(
            model,
            [
                "C05",
                "choice",
                "为什么 List<String> 不是 List<Object> 的子类型？这和数组有什么不同？",
                "这是 Java 的 bug||为了类型安全——如果 List<String> 能当 List<Object> 用，就可以往里面放 Integer，破坏 String 列表的类型安全。数组为了兼容旧代码允许 String[] 当 Object[] 用，但运行时写入非 String 会抛 ArrayStoreException||两者是父子关系——编译器有 bug||泛型不支持继承",
                "2",
                "Java 数组是协变的：String[] 是 Object[] 的子类型——存非 String 入 Object[] 引用的数组 → 运行时 ArrayStoreException（错误推迟到运行时）。泛型设计者选择不变（invariant）：List<String> 和 List<Object> 无父子关系——编译期就能杜绝错误。这是「类型安全前移」理念的体现。通配符 ? 就是来弥补泛型不变带来的灵活性损失的。",
                "",
                "",
                "",
            ],
            ["ch11", "wildcard", "invariance", "choice"],
        ),
        # ═══ C06 · 三种通配符 · 单选 ═══
        note(
            model,
            [
                "C06",
                "choice",
                "<?>、<? extends T>、<? super T> 三种通配符各自的语义和读写能力是什么？",
                "三者完全相同||<?> = 元素类型未知，只能读（返回 Object）不能写；<? extends T> = 元素是 T 或 T 子类，只能读不能写（PECS 的 Producer）；<? super T> = 元素是 T 或 T 超类，可以写 T 类型，读返回 Object（PECS 的 Consumer）||<? extends T> 可以写，<? super T> 只能读||<?> 可以读写任何类型",
                "2",
                "PECS 口诀：Producer Extends（产生数据的用 extends，只读），Consumer Super（消费数据的用 super，只写）。List<? extends Number>——可以从列表中取 Number，但 list.add(?) 非法。List<? super Integer>——可以 list.add(42)，但取出的只能是 Object。上界保类型安全（知道「至少是这个类型」），下界保写入安全（知道「至少能存这个类型」）。",
                "",
                "",
                "",
            ],
            ["ch11", "wildcard", "pecs", "choice"],
        ),
        # ═══ C07 · T vs ? · 单选 ═══
        note(
            model,
            [
                "C07",
                "choice",
                "类型参数 T 和通配符 ? 的精确区别是什么？什么时候必须用 T？",
                "没有区别||T 是确定的类型（虽然编译时不知道具体值，但同一段代码中 T 是固定的），用于定义泛型类/方法；? 是不确定的类型，只能用于形参/变量声明，不能用于定义。需要多次引用同一类型时（如方法返回类型与参数类型一致）必须用 T||T 只能用一次，? 可重复使用||T 用于接口，? 用于类",
                "2",
                "T vs ? 对照：① 定义能力——T 可声明泛型类 class Box<T> 和泛型方法 <T> void f()；? 不能——? a = ... 非法。② 代码引用——T 是一个可以在方法体内使用的类型名（T t）；? 是匿名类型，不能声明变量。③ 使用场景——T 用于「类型需要被多次引用」的情况（如参数与返回值同类型 public T get(T t)）；? 用于「类型只出现一次不关心具体值」的情况（如遍历打印 List<?> list）。",
                "",
                "",
                "",
            ],
            ["ch11", "generic", "T-vs-wildcard", "choice"],
        ),

        # ═══════════ 模板方法模式 ═══════════
        # ═══ C08 · 模板方法结构 · 单选 ═══
        note(
            model,
            [
                "C08",
                "choice",
                "模板方法模式中，模板方法 templateMethod() 应该用什么修饰？为什么？抽象方法和钩子方法的区别？",
                "public——让子类覆盖||模板方法用 public final——定义算法骨架，不允许子类覆盖（骨架是固定的）。抽象方法用 protected abstract——子类必须实现。钩子方法用 protected（非 abstract）——提供默认空实现，子类可选覆盖||模板方法必须是 abstract 的||钩子方法必须是 final 的",
                "2",
                "三种方法角色：① 模板方法（public final）——算法骨架，调用各个步骤。final 确保骨架不被子类篡改。② 抽象方法（protected abstract）——子类必须实现的可变步骤。③ 钩子方法（protected，有方法体）——子类可选覆盖的扩展点，默认实现可能是空操作或默认值。好莱坞法则：父类调用子类的方法——「别找我们，我们找你」。反向控制——控制流在父类中，细节留给子类。",
                "",
                "",
                "",
            ],
            ["ch11", "template-method", "structure", "choice"],
        ),
        # ═══ C09 · 模板方法 vs 策略 · 单选 ═══
        note(
            model,
            [
                "C09",
                "choice",
                "模板方法模式和策略模式都用于「算法的不同实现」。它们的根本区别是什么？",
                "没有区别——可以互换||模板方法用继承（子类覆盖），编译期确定，适合算法骨架固定、个别步骤变化的场景；策略模式用组合（注入策略对象），运行时可切换，适合整个算法可替换的场景||模板方法用组合，策略用继承||模板方法只用于集合框架",
                "2",
                "核心区分：① 复用机制——模板方法 = 继承（白箱复用，子类知道父类细节），策略 = 组合（黑箱复用，只依赖接口）。② 变化粒度——模板方法变的是「算法中的某些步骤」，策略变的是「整个算法」。③ 运行时灵活性——模板方法在编译时就确定了子类（静态），策略可在运行时替换（动态）。④ 选择——算法整体要替换 → 策略；算法骨架不变、只需定制某几步 → 模板方法。",
                "",
                "",
                "",
            ],
            ["ch11", "template", "vs-strategy", "choice"],
        ),

        # ═══════════ 反射 ═══════════
        # ═══ C10 · Class 对象 · 单选 ═══
        note(
            model,
            [
                "C10",
                "choice",
                "获取 Java 类的 Class 对象有哪三种方式？一个类在 JVM 中有几个 Class 对象？",
                "一种——new Class()||① obj.getClass()、② 类名.class、③ Class.forName(\"全限定类名\")。一个类在 JVM 中只有一个 Class 对象——c1 == c2 == c3||三种——编译期、运行期、链接期||每个实例有一个 Class 对象",
                "2",
                "三种方式：① getClass()——从已有对象获取，继承了 Object；② 类名.class——最安全高效，编译期检查，不需要对象；③ Class.forName(className)——动态加载，类名字符串可来自配置/输入，适合插件系统。一个 Class 对象存储类的完整结构信息（包名/类名/字段/方法/构造器等），JVM 用它选择要执行的方法。唯一性：同一个类的 Class 对象在 JVM 中全局唯一——所有获取方式返回同一对象。",
                "",
                "",
                "",
            ],
            ["ch11", "reflection", "class-object", "choice"],
        ),
        # ═══ C11 · 反射构造 · 单选 ═══
        note(
            model,
            [
                "C11",
                "choice",
                "Class.newInstance() 和 Constructor.newInstance() 的区别是什么？getConstructor 和 getDeclaredConstructor 的区别？",
                "没有区别||Class.newInstance() 只能调用无参公开构造——如果类没有无参构造或构造是 private 就抛异常。Constructor.newInstance() 可指定参数类型调用任意构造。getConstructor 只获取「公开的」指定参数构造；getDeclaredConstructor 获取「任意访问权限」的指定参数构造——私有的需 setAccessible(true) 后调用||Class.newInstance() 已废弃||getConstructor 获取所有构造，getDeclaredConstructor 获取一个",
                "2",
                "获取构造：getConstructors() = 所有公有构造。getDeclaredConstructors() = 所有构造（含私有）。getConstructor(int.class, String.class) = 指定参数类型的公有构造。Constructor 对象调用 newInstance(实参) 创建对象——支持有参构造。setAccessible(true) 突破 Java 访问控制——是反射破坏封装的入口，也用于防御（在构造中检测并抛异常）。",
                "",
                "",
                "",
            ],
            ["ch11", "reflection", "constructor", "choice"],
        ),
        # ═══ C12 · 反射字段与方法 · 单选 ═══
        note(
            model,
            [
                "C12",
                "choice",
                "通过反射获取字段和方法时，getFields() 和 getDeclaredFields() 的区别？Method.invoke() 的两个参数是什么？",
                "没有区别||getFields() = 获取所有公有字段（含继承的）；getDeclaredFields() = 获取本类声明的所有字段（含私有的，不含继承的）。Method.invoke(obj, args)——obj 是调用方法的对象（静态方法传 null），args 是参数||getFields() 获取私有字段||invoke 只需要方法名",
                "2",
                "字段相关：getField(name) / getFields()——公有字段。getDeclaredField(name) / getDeclaredFields()——本类所有字段（private 也能拿，需 setAccessible）。get(Object obj) 读取字段值，set(Object obj, Object value) 修改字段值。方法相关：getMethod(name, paramTypes) / getDeclaredMethod(name, paramTypes)。invoke(obj, args)——第一个参数是调用目标对象，之后是实参，返回 Object。反射缺点：性能瓶颈（解释执行而非直接调用）、破坏封装、丢失编译期检查。",
                "",
                "",
                "",
            ],
            ["ch11", "reflection", "field-method", "choice"],
        ),
        # ═══ C13 · 反射破坏单例 · 单选 ═══
        note(
            model,
            [
                "C13",
                "choice",
                "如何使用反射破坏饿汉式单例？如何在构造方法中防御反射攻击？",
                "反射无法破坏单例||攻击：constructor = Singleton.class.getDeclaredConstructor(); constructor.setAccessible(true); Singleton evil = constructor.newInstance()。防御：在私有构造中检查——if (singleton != null) throw new RuntimeException()。原理：饿汉式在类加载时就创建了唯一实例，攻击代码通过反射调用私有构造时，静态字段 instance 已经非 null——抛异常阻止创建第二个实例||用 getConstructor 获取||用 Class.newInstance()",
                "2",
                "攻击流程：① 获取 Singleton.class → ② getDeclaredConstructor() 拿到私有构造 → ③ setAccessible(true) 突破访问控制 → ④ newInstance() 创建第二个实例。防御原理：私有构造执行时检查静态字段是否已非 null——如果是则说明实例已存在（无论是正常调用还是反射），抛异常阻止。注意：此防御无法阻止通过序列化反序列化创建第二个实例——需额外实现 readResolve() 方法防御。",
                "",
                "",
                "",
            ],
            ["ch11", "reflection", "singleton", "choice"],
        ),

        # ═══ F01 · 泛型通配符 · 填空 ═══
        note(
            model,
            [
                "F01",
                "fill",
                "三种通配符：① {{c1::<?>}}(无限定)——元素类型未知，只能{{c2::读}}(读/写)，取出的只能是 Object，不能 add。② {{c3::<? extends T>}}(上界)——T 及 T 子类，只能{{c4::读}}(读/写)，遵循 PECS 的 Producer 角色。③ {{c5::<? super T>}}(下界)——T 及 T 超类，可以{{c6::写}}(读/写) T 类型，读回 Object，遵循 PECS 的 Consumer 角色。List<String>{{c7::不是}}(是/不是) List<Object> 的子类型。",
                "",
                "<?>||读||<? extends T>||读||<? super T>||写||不是",
                "PECS：Producer Extends（产出数据用 extends——只取不存）、Consumer Super（消费数据用 super——只存不取适用于 copy）。这来自 Josh Bloch《Effective Java》。",
                "",
                "",
                "",
            ],
            ["ch11", "wildcard", "all", "fill", "multi-cloze"],
        ),
        # ═══ F02 · 模板方法 · 填空 ═══
        note(
            model,
            [
                "F02",
                "fill",
                "模板方法模式：抽象类中定义{{c1::模板方法}}(public final)——算法骨架，调用{{c2::抽象方法}}(protected abstract)——子类必须实现，和{{c3::钩子方法}}(protected 有体)——子类可选覆盖。好莱坞法则：{{c4::父类调用子类}}——「别找我们，我们找你」。与策略模式区别：模板方法用{{c5::继承}}(继承/组合)（编译时），策略用{{c6::组合}}(继承/组合)（运行时切换）。",
                "",
                "模板方法||抽象方法||钩子方法||父类调用子类||继承||组合",
                "模板方法优势：一次实现算法不变部分，可变部分留给子类；提取公共行为到父类避免代码重复；控制子类扩展——只允许在特定点（hook）扩展。应用场景：Swing 的 paintComponent 就是模板方法的钩子操作。",
                "",
                "",
                "",
            ],
            ["ch11", "template-method", "fill", "multi-cloze"],
        ),
        # ═══ F03 · 反射 API · 填空 ═══
        note(
            model,
            [
                "F03",
                "fill",
                "反射核心 API：获取 Class 对象三种方式——{{c1::obj.getClass()}}、{{c2::类名.class}}、{{c3::Class.forName(\"全限定名\")}}。获取构造——getConstructor(参数类型)（公有）/{{c4::getDeclaredConstructor(参数类型)}}（私有需 setAccessible）。获取字段——getField / getDeclaredField，读写用{{c5::get(obj) / set(obj, val)}}。获取方法——getMethod(name, paramTypes) / getDeclaredMethod，调用用{{c6::invoke(obj, args)}}。静态方法 invoke 第一个参数传{{c7::null}}。",
                "",
                "obj.getClass()||类名.class||Class.forName(\"全限定名\")||getDeclaredConstructor(参数类型)||get(obj) / set(obj, val)||invoke(obj, args)||null",
                "反射缺点：性能瓶颈（解释执行 JVM 要额外查 metadata）、破坏封装（可访问私有成员）、失去编译期类型检查。适用场景：IDE 的代码补全、Spring 的依赖注入(@Autowired)、JUnit 的测试发现、序列化框架。",
                "",
                "",
                "",
            ],
            ["ch11", "reflection", "api", "fill", "multi-cloze"],
        ),

        # ═══ Q01 · 泛型通配符综合 · 问答 ═══
        note(
            model,
            [
                "Q01",
                "qa",
                "飞机大战中，排行榜需要支持多种类型：ScoreEntry、KillRecord、ItemCollection。① 写出泛型接口 RankBoard<T>（方法：add(T item)、List<T> topN(int n)、T getBest()）；② 写出 printBoard 方法能打印任何排行榜（用通配符）；③ 说明为什么用 <?> 而非 <Object>。",
                "",
                "public interface RankBoard<T extends Comparable<T>> {\n    void add(T item);\n    List<T> topN(int n);\n    T getBest();\n}\n\n// 打印任意排行榜——用通配符\npublic static void printBoard(RankBoard<?> board, int n) {\n    for (Object item : board.topN(n)) {\n        System.out.println(item.toString());\n    }\n}\n\n// 为什么用 <?> 而非 <Object>：\n// RankBoard<ScoreEntry> 不是 RankBoard<Object> 的子类型——\n// printBoard(RankBoard<Object>) 无法接收 RankBoard<ScoreEntry>。\n// <?> 表示「任意类型的排行榜」——解决了泛型的不变性。\n// T extends Comparable<T> 确保排行榜能排序。",
                "考察：① 泛型接口声明 + 上界约束；② 通配符 <?> 的应用场景——方法只读不写；③ 泛型不变性的理解——RankBoard<A> 和 RankBoard<B> 无继承关系；④ T extends Comparable<T> 表示类型参数必须可比较自身——这是排行榜排序的前提。",
                "",
                "",
                "",
            ],
            ["ch11", "generic", "wildcard", "qa"],
        ),
        # ═══ Q02 · 模板方法飞机大战 · 问答 ═══
        note(
            model,
            [
                "Q02",
                "qa",
                "写出飞机大战中「敌机波次生成器」的模板方法模式完整代码。抽象类 EnemyWaveGenerator 定义 spawnWave() 模板方法（final），抽象方法 getFormation() / createEnemy(int idx) 由子类实现，钩子方法 onWaveStart() 可选的 BOSS 出场动画。给出一个具体子类 BossWaveGenerator。",
                "",
                "public abstract class EnemyWaveGenerator {\n    public final void spawnWave() {      // final：骨架不可覆盖\n        onWaveStart();                   // 钩子——可选覆盖\n        Enemy[] formation = getFormation();  // 抽象——子类决定阵型\n        for (int i = 0; i < formation.length; i++) {\n            Enemy e = createEnemy(i);    // 抽象——子类决定敌机\n            addToScreen(e, formation[i]);\n        }\n        onWaveComplete();                // 钩子\n    }\n    protected abstract Enemy[] getFormation();\n    protected abstract Enemy createEnemy(int index);\n    protected void onWaveStart() {}     // 钩子默认空\n    protected void onWaveComplete() { System.out.println(\"波次完成\"); }\n}\n\npublic class BossWaveGenerator extends EnemyWaveGenerator {\n    @Override protected Enemy[] getFormation() {\n        return new Enemy[]{position(200,0)};  // BOSS 在屏幕中间\n    }\n    @Override protected Enemy createEnemy(int i) {\n        return new BossEnemy(200, 0);\n    }\n    @Override protected void onWaveStart() {\n        System.out.println(\"!!! WARNING: BOSS APPROACHING !!!\");\n    }\n}",
                "考察：① 模板方法 final 修饰——防止子类篡改算法骨架；② 抽象方法 protected abstract——子类必须实现但外部不可见；③ 钩子方法 protected 非 abstract——有默认实现，子类按需覆盖；④ 好莱坞法则——spawnWave() 调用子类的 getFormation()/createEnemy()/onWaveStart()，控制反转。",
                "",
                "",
                "",
            ],
            ["ch11", "template-method", "example", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 第十一章 泛型与反射", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
