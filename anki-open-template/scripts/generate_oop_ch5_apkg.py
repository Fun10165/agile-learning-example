from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400515
OUTPUT = ROOT / "anki-第五章-设计模式导论.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════ 七条设计原则（考试重点）═══════════
        # ═══ C01 · SRP · 单选 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "单一职责原则（SRP）的核心含义是什么？",
                "一个类应该实现尽可能多的功能||一个类应该仅有一个引起它变化的原因||一个类应该只有一个方法||一个类只能有一个字段",
                "2",
                "SRP：就一个类而言，应该仅有一个引起它变化的原因。如果将不同变化原因的职责放在一起，一个职责的变化可能削弱或抑制该类完成其他职责的能力。判定标准：如果多于一个动机去改变一个类，该类就具有多个职责，应考虑职责分离。如 Hero 类同时负责移动和分数存储——修改分数存储方式不该影响 Hero 类。",
                "",
                "",
                "",
            ],
            ["ch5", "SRP", "principle", "choice"],
        ),
        # ═══ C02 · OCP · 单选 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "开闭原则（OCP）的含义是什么？Java 中如何实现？",
                "对修改开放，对扩展关闭——通过反射实现||对扩展开放，对修改关闭——通过抽象类和接口实现||所有类都必须是 public 的||禁止使用 private 修饰符",
                "2",
                "OCP：在不修改已有代码的前提下，通过扩展来增加新功能。Java 实现机制：用抽象类/接口定义稳定的抽象层（不修改），通过新增子类来改变行为（扩展）。反例：每加一种敌机就要改 createEnemy() 的 if-else——违反 OCP。正例：用工厂方法模式，加新敌机 = 建新子类，已有代码不动。",
                "",
                "",
                "",
            ],
            ["ch5", "OCP", "principle", "choice"],
        ),
        # ═══ C03 · LSP · 单选 ═══
        note(
            model,
            [
                "C03",
                "choice",
                "里氏代换原则（LSP）要求子类满足什么条件？",
                "子类的方法必须比父类的方法更长||子类的方法必须与父类有完全相同的代码||所有引用基类的地方，必须能透明地使用其子类对象||子类必须覆盖父类的所有方法",
                "3",
                "LSP 的精确含义：如果 T2 是 T1 的子类型，那么以 T1 定义的所有程序 P 在所有 T1 对象都代换为 T2 对象时，P 的行为没有变化。子类不能破坏父类的契约。反例：InvincibleEnemy 覆盖 takeDamage() 为「什么都不做」——破坏了「受伤害会扣血到死」的隐性契约。子类只能「强化」契约（前置条件不加强、后置条件不减弱），不能「弱化」。",
                "",
                "",
                "",
            ],
            ["ch5", "LSP", "principle", "choice"],
        ),
        # ═══ C04 · DIP · 单选 ═══
        note(
            model,
            [
                "C04",
                "choice",
                "依赖倒转原则（DIP）中「倒转」的是什么？",
                "倒转了代码的执行顺序||倒转了依赖关系——高层模块和低层模块都依赖抽象，而不是高层依赖低层||倒转了类的继承层次||倒转了内存分配的方向",
                "2",
                "DIP：① 高层模块不应该依赖低层模块，两者都应该依赖抽象。② 要针对接口编程，不要针对实现编程。传统结构化设计中，高层的 GameLoop 依赖具体的 NormalEnemy→ 倒转后两者都依赖抽象的 Enemy。实现方式：使用接口/抽象类进行变量类型声明、参数类型声明和返回类型说明。",
                "",
                "",
                "",
            ],
            ["ch5", "DIP", "principle", "choice"],
        ),
        # ═══ C05 · CARP · 单选 ═══
        note(
            model,
            [
                "C05",
                "choice",
                "合成复用原则（CARP）为什么建议「优先使用组合而非继承」？",
                "因为继承的语法更复杂||因为组合是黑箱复用（只知道接口），耦合更低；继承是白箱复用（知道内部实现），耦合更高||因为组合运行速度更快||因为继承在 Java 中已被废弃",
                "2",
                "继承是白箱复用——子类知道父类内部细节，父类修改可能破坏子类。组合是黑箱复用——只依赖被组合对象的公开接口，内部实现变化不影响使用方。优先顺序：合成/聚合 > 继承。使用继承时须严格遵循 LSP。BossEnemy 通过组合同时拥有 MoveStrategy 和 FireStrategy，用继承无法同时获得两种行为。",
                "",
                "",
                "",
            ],
            ["ch5", "CARP", "principle", "choice"],
        ),
        # ═══ C06 · ISP · 单选 ═══
        note(
            model,
            [
                "C06",
                "choice",
                "接口隔离原则（ISP）反对什么？",
                "反对使用任何接口||反对使用抽象类||反对「胖接口」——客户端不应该依赖它不需要的接口||反对接口中有多个方法",
                "3",
                "ISP：客户端不应该依赖它不需要的接口。一旦接口太大（胖接口），应分割成更细小的接口。使用多个专门的接口比使用单一总接口好。反例：GameObject 接口包含 move/fire/draw/heal/explode——NormalEnemy 被迫实现 heal()（空实现）。正例：拆为 Movable、Shootable、Damagable 三个小接口，每个类只实现自己需要的。",
                "",
                "",
                "",
            ],
            ["ch5", "ISP", "principle", "choice"],
        ),
        # ═══ C07 · LoD · 单选 ═══
        note(
            model,
            [
                "C07",
                "choice",
                "迪米特法则（LoD / 最少知识原则）要求什么？",
                "每个类都要尽可能多地了解其他类||一个对象应该对其它对象有尽可能少的了解，只和直接朋友通信||类之间不应该有任何交互||所有方法都必须是 private 的",
                "2",
                "LoD：一个软件实体应尽可能少地与其他实体发生相互作用。具体规则——对象的方法只能调用：自身、方法参数、自身创建的对象、自身持有的组件对象。不要和「朋友的朋友」通信。反例：GamePanel 调用 hero.getGun().getBullets()——和 Gun（Hero 的朋友）直接交互。正例：Hero 封装 anyBulletHits(Enemy)，GamePanel 只调用 Hero 的方法。",
                "",
                "",
                "",
            ],
            ["ch5", "LoD", "principle", "choice"],
        ),
        # ═══ C08 · 七原则综合 · 多选 ═══
        note(
            model,
            [
                "C08",
                "choice",
                "以下哪些是面向对象设计的核心原则？（多选）",
                "单一职责原则（SRP）||开闭原则（OCP）||里氏代换原则（LSP）||依赖注入原则（DIP-另一种）||接口实现原则（IIP）||迪米特法则（LoD）||合成复用原则（CARP）||接口隔离原则（ISP）",
                "1||2||3||6||7||8",
                "正确的七大原则：SRP、OCP、LSP、DIP（依赖倒转原则）、CARP、ISP、LoD。选项 4「依赖注入」是 Spring 框架的实现技术，不是七大设计原则之一。选项 5 不存在。DIP 的 D 是 Dependency Inversion（依赖倒转），不是 Dependency Injection（依赖注入）。",
                "",
                "",
                "",
            ],
            ["ch5", "principles", "all", "choice", "multi"],
        ),
        # ═══ C09 · 道与术 · 单选 ═══
        note(
            model,
            [
                "C09",
                "choice",
                "面向对象设计中「道与术」分别指什么？",
                "道 = 设计模式，术 = 编程语言||道 = 设计原则（抽象/封装/继承/多态等指导思想），术 = 设计模式（解决具体问题的具象化方法）||道 = 单例模式，术 = 工厂模式||道 = Java 语法，术 = 代码实现",
                "2",
                "道 = 面向对象的核心思想和方法论（七大设计原则 + 封装/继承/多态），是所有模式的指导性原则。术 = 具体的设计模式（单例、工厂、策略、观察者等），是「道」在解决不同具体问题时的具象化方法。只知道模式怎么写（术）不懂为什么这么写（道），换个场景就不会用了。",
                "",
                "",
                "",
            ],
            ["ch5", "tao-shu", "choice"],
        ),

        # ═══════════ 设计模式概念 ═══════════
        # ═══ C10 · 四要素 · 单选 ═══
        note(
            model,
            [
                "C10",
                "choice",
                "设计模式的四个基本要素是什么？",
                "类名、方法名、字段名、包名||模式名、问题、解决方案、效果||创建型、结构型、行为型、范围||封装、继承、多态、抽象",
                "2",
                "四要素：① 模式名（Pattern Name）——助记词，用于交流；② 问题（Problem）——何时使用、解决什么问题；③ 解决方案（Solution）——组成成分、关系和协作方式（不是具体代码，是抽象描述）；④ 效果（Consequence）——优缺点、时空权衡、对灵活性/扩展性/可移植性的影响。所有 GoF 23 种模式都按这四要素描述。",
                "",
                "",
                "",
            ],
            ["ch5", "pattern", "elements", "choice"],
        ),
        # ═══ C11 · GoF 分类 · 单选 ═══
        note(
            model,
            [
                "C11",
                "choice",
                "GoF 23 种设计模式按目的分为哪三类？",
                "创建型、修改型、删除型||创建型、结构型、行为型||类模式、对象模式、接口模式||单例型、工厂型、策略型",
                "2",
                "按目的分：① 创建型（Creational）——将对象的创建与使用分离（单例、工厂方法、抽象工厂、建造者、原型）；② 结构型（Structural）——将类或对象组合成更大的结构（适配器、装饰器、代理、组合、桥接、外观、享元）；③ 行为型（Behavioral）——类或对象间的协作和职责分配（策略、观察者、模板方法、命令、迭代器等）。按范围分：类模式（编译时，基于继承）和对象模式（运行时，基于组合/聚合）。",
                "",
                "",
                "",
            ],
            ["ch5", "gof", "classification", "choice"],
        ),
        # ═══ C12 · 范围分类 · 单选 ═══
        note(
            model,
            [
                "C12",
                "choice",
                "设计模式按范围分，类模式和对象模式的关键区别是什么？",
                "类模式处理对象间关系（动态），对象模式处理类间关系（静态）||类模式处理类与子类的关系（通过继承，编译时确定），对象模式处理对象间关系（通过组合/聚合，运行时可变）||类模式只能用于 Java，对象模式可用于所有语言||没有区别，只是名称不同",
                "2",
                "类模式：处理类与子类之间的关系，通过继承建立，编译时确定——静态。代表：工厂方法、适配器（类）、模板方法、解释器。对象模式：处理对象之间的关系，通过组合/聚合实现，运行时可变——动态。代表：单例、抽象工厂、策略、观察者、装饰器、代理等绝大多数模式。",
                "",
                "",
                "",
            ],
            ["ch5", "scope", "class-vs-object", "choice"],
        ),

        # ═══════════ 单例模式 ═══════════
        # ═══ C13 · 单例三要素 · 单选 ═══
        note(
            model,
            [
                "C13",
                "choice",
                "单例模式（Singleton）保证唯一实例的三个关键机制是什么？",
                "public 字段记录实例、public 构造方法、实例方法获取对象||private 静态字段持有唯一实例、private 构造方法、public 静态方法 getInstance()||synchronized 字段、final 构造方法、static 代码块||volatile 变量、protected 构造、synchronized getter",
                "2",
                "单例三要素：① private 构造方法——外部无法 new；② private static 字段——持有唯一实例的引用；③ public static 工厂方法（通常 getInstance()）——返回唯一实例。UML 类图：Singleton 类中 -instance: Singleton（私有静态字段），-Singleton()（私有构造），+getInstance(): Singleton（公有静态方法）。",
                "",
                "",
                "",
            ],
            ["ch5", "singleton", "structure", "choice"],
        ),
        # ═══ C14 · 饿汉 vs 懒汉 · 单选 ═══
        note(
            model,
            [
                "C14",
                "choice",
                "饿汉式和懒汉式单例的核心区别是什么？各自的优缺点？",
                "饿汉式线程不安全，懒汉式线程安全||饿汉式在类加载时立即创建实例（线程安全但可能浪费），懒汉式在第一次调用 getInstance() 时创建（延迟初始化但需处理线程安全）||饿汉式需要 synchronized，懒汉式不需要||两者完全一样，只是命名不同",
                "2",
                "饿汉式：类加载时立即实例化——JVM 类加载机制天然保证线程安全，调用效率高（无需同步），但不用也会创建实例（浪费）。懒汉式：第一次调用 getInstance() 时才实例化——延迟初始化，但多线程下需 synchronized 保证线程安全，同步带来性能开销。课外拓展：双重检查锁定（DCL）用 volatile + synchronized 块实现线程安全且高并发的懒汉式。",
                "",
                "",
                "",
            ],
            ["ch5", "singleton", "eager-vs-lazy", "choice"],
        ),

        # ═══════════ 工厂模式 ═══════════
        # ═══ C15 · 简单工厂 · 单选 ═══
        note(
            model,
            [
                "C15",
                "choice",
                "简单工厂模式（Simple Factory）为什么「不是真正的设计模式」？",
                "因为 Java 不支持||因为它的工厂方法是静态的||因为它不是 GoF 23 种之一，且违反开闭原则——每加一种产品就要修改工厂类的创建逻辑||因为工厂类不能被实例化",
                "3",
                "简单工厂将对象创建集中到一个工厂类的静态方法中，实现了创建与使用的分离。但致命缺陷：加新产品 → 改 createProduct() 里的 if-else/switch → 违反 OCP。产品类型多时工厂逻辑越来越复杂，且工厂类集中了所有创建逻辑——工厂挂了整个系统瘫痪。简单工厂是工厂方法模式的前身和基础，常作为编码技巧使用而非独立的设计模式。",
                "",
                "",
                "",
            ],
            ["ch5", "simple-factory", "limitation", "choice"],
        ),
        # ═══ C16 · 工厂方法 · 单选 ═══
        note(
            model,
            [
                "C16",
                "choice",
                "工厂方法模式（Factory Method）中，「工厂方法」指的是什么？",
                "工厂类中的一个静态方法||抽象类（Creator）中声明的抽象 factoryMethod()，由子类实现，返回一个 Product 对象||客户端代码中的 main 方法||产品的构造方法",
                "2",
                "结构：Creator 抽象类实现所有操作产品的方法（如 orderPizza()），但将 factoryMethod() 声明为抽象——「创建产品的具体工作交给子类」。ConcreteCreator 子类覆盖 factoryMethod() 返回具体产品。核心思想：将对象的实例化延迟到子类。orderPizza() 不知道具体是什么披萨——它只调用抽象 factoryMethod() 拿到 Product，然后调用通用流程（prepare/bake/cut/box）。符合 OCP。",
                "",
                "",
                "",
            ],
            ["ch5", "factory-method", "definition", "choice"],
        ),
        # ═══ C17 · 抽象工厂 · 单选 ═══
        note(
            model,
            [
                "C17",
                "choice",
                "抽象工厂模式中「产品族」和「产品等级」分别指什么？",
                "产品族 = 同一品牌的所有产品，产品等级 = 同一类产品不同品牌||产品族 = 所有工厂，产品等级 = 所有产品||产品族 = 手机，产品等级 = 电脑||两者是同一概念的不同翻译",
                "1",
                "产品族（Product Family）= 同一品牌下的所有产品——如华为（手机+路由+电脑）。产品等级（Product Type）= 同一类产品不同品牌——如手机（华为手机、小米手机）。抽象工厂的好处：新增品牌容易（建新工厂子类，符合 OCP）；坏处：新增产品类型极难（要改工厂接口和所有实现类）。设计时需权衡产品族和产品等级哪个变化更频繁。",
                "",
                "",
                "",
            ],
            ["ch5", "abstract-factory", "family-vs-type", "choice"],
        ),
        # ═══ C18 · 三种工厂对比 · 单选 ═══
        note(
            model,
            [
                "C18",
                "choice",
                "简单工厂、工厂方法、抽象工厂三者的递进关系是什么？",
                "三者是并列的，没有递进关系||简单工厂（一个工厂创建所有产品，违反 OCP）→ 工厂方法（每个具体产品一个具体工厂，符合 OCP）→ 抽象工厂（一个工厂创建一组相关产品，即产品族）||简单工厂是最复杂的，抽象工厂是最简单的||工厂方法包含简单工厂，抽象工厂包含工厂方法",
                "2",
                "递进关系：简单工厂——一个工厂类集中所有创建逻辑，加新产品要改工厂（违反 OCP）。工厂方法——将工厂抽象化，每个具体产品对应一个具体工厂子类，加新产品 = 新建子类（符合 OCP）。抽象工厂——创建的不只是一个产品，而是一整个产品族（一组配套产品），保证同一品牌产品的一致性。从「创建一个」到「创建一组」，从「中心化工厂」到「分布式工厂」。",
                "",
                "",
                "",
            ],
            ["ch5", "factory", "comparison", "choice"],
        ),

        # ═══ F01 · 七原则速记 · 填空 ═══
        note(
            model,
            [
                "F01",
                "fill",
                "七大设计原则：{{c1::单一职责原则}}(SRP)——一个类仅有一个变化原因；{{c2::开闭原则}}(OCP)——对扩展开放、对修改关闭；{{c3::里氏代换原则}}(LSP)——子类必须能透明替代父类；{{c4::依赖倒转原则}}(DIP)——依赖抽象而非具体；{{c5::合成复用原则}}(CARP)——优先组合而非继承；{{c6::接口隔离原则}}(ISP)——客户端不依赖不需要的接口；{{c7::迪米特法则}}(LoD)——只和直接朋友通信。",
                "",
                "单一职责原则||开闭原则||里氏代换原则||依赖倒转原则||合成复用原则||接口隔离原则||迪米特法则",
                "口诀速记：S(ingle Responsibility) O(pen-Closed) L(iskov) I(nterface Segregation) D(ependency Inversion) + CARP + LoD = SOLID + 两条。SOLID 是前五条首字母的经典记忆法。",
                "",
                "",
                "",
            ],
            ["ch5", "principles", "seven", "fill", "multi-cloze"],
        ),
        # ═══ F02 · 设计模式四要素 · 填空 ═══
        note(
            model,
            [
                "F02",
                "fill",
                "设计模式四要素：{{c1::模式名}}(Pattern Name)——助记词，便于交流；{{c2::问题}}(Problem)——何时使用该模式，描述应用环境和先决条件；{{c3::解决方案}}(Solution)——设计的组成成分、它们的关系及协作方式（是抽象描述而非具体代码）；{{c4::效果}}(Consequence)——模式的优缺点、时空权衡及对系统灵活性/扩展性/可移植性的影响。",
                "",
                "模式名||问题||解决方案||效果",
                "解决方案不描述具体实现——如单例的解决方案是「私有构造+静态唯一实例+静态访问方法」，但具体用饿汉式还是懒汉式是实现的自由。效果包括：对时间/空间的衡量，对灵活性/扩充性/可移植性的影响。",
                "",
                "",
                "",
            ],
            ["ch5", "pattern", "elements", "fill", "multi-cloze"],
        ),
        # ═══ F03 · GoF 分类 · 填空 ═══
        note(
            model,
            [
                "F03",
                "fill",
                "GoF 23 种模式按目的分三类：{{c1::创建型}}（将对象创建与使用分离，如单例、工厂方法、抽象工厂）、{{c2::结构型}}（将类或对象组合成更大结构，如适配器、装饰器、代理）、{{c3::行为型}}（类或对象间协作和职责分配，如策略、观察者、模板方法）。按范围分：{{c4::类}}模式（基于继承，编译时确定）和{{c5::对象}}模式（基于组合/聚合，运行时可变）。",
                "",
                "创建型||结构型||行为型||类||对象",
                "创建型 5 种：单例、工厂方法、抽象工厂、建造者、原型。结构型 7 种：适配器、桥接、组合、装饰、外观、享元、代理。行为型 11 种：职责链、命令、解释器、迭代器、中介者、备忘录、观察者、状态、策略、模板方法、访问者。5+7+11=23。",
                "",
                "",
                "",
            ],
            ["ch5", "gof", "classification", "fill", "multi-cloze"],
        ),
        # ═══ F04 · 单例三要素 · 填空 ═══
        note(
            model,
            [
                "F04",
                "fill",
                "单例模式三要素：① {{c1::private}}构造方法——外部无法 new；② {{c2::private static}}字段——持有唯一实例的引用；③ {{c3::public static}}方法（通常 getInstance()）——返回唯一实例。饿汉式：类加载时立即创建——线程{{c4::安全}}但可能浪费资源。懒汉式：首次调用时创建——延迟初始化但需要{{c5::synchronized}}保证线程安全。",
                "",
                "private||private static||public static||安全||synchronized",
                "UML 类图要点：-instance: Singleton（私有静态字段）、-Singleton()（私有构造）、+getInstance(): Singleton（公有静态方法）。饿汉式代码：private static final Singleton INSTANCE = new Singleton();。返回字段即可，无需判空。",
                "",
                "",
                "",
            ],
            ["ch5", "singleton", "elements", "fill", "multi-cloze"],
        ),
        # ═══ F05 · 工厂方法结构 · 填空 ═══
        note(
            model,
            [
                "F05",
                "fill",
                "工厂方法模式结构：{{c1::Creator}}抽象类实现所有操作产品的方法（如 orderPizza()），但声明抽象的{{c2::factoryMethod()}}——创建产品的具体工作交给子类。{{c3::ConcreteCreator}}子类覆盖 factoryMethod() 返回{{c4::具体产品}}。核心思想：将对象的{{c5::实例化延迟到子类}}。符合{{c6::开闭原则}}（OCP）。",
                "",
                "Creator||factoryMethod()||ConcreteCreator||具体产品||实例化延迟到子类||开闭原则",
                "对比：简单工厂中 createPizza() 是具体方法（含 if-else）——违反 OCP。工厂方法中 factoryMethod() 是抽象方法——子类各自实现，符合 OCP。orderPizza() 不知道具体是哪种产品，它只知道拿到的是 Product（依赖抽象）。",
                "",
                "",
                "",
            ],
            ["ch5", "factory-method", "structure", "fill", "multi-cloze"],
        ),
        # ═══ F06 · 抽象工厂概念 · 填空 ═══
        note(
            model,
            [
                "F06",
                "fill",
                "抽象工厂模式核心概念：{{c1::产品族}}(Product Family) = 同一品牌下的所有产品（如华为：手机+路由+电脑）；{{c2::产品等级}}(Product Type) = 同一类产品不同品牌（如手机：华为手机+小米手机）。优点：新增{{c3::品牌（产品族）}}容易（新建工厂子类，符合 OCP）；缺点：新增{{c4::产品类型}}极难（要改工厂接口和所有实现类）。保证{{c5::同一产品族内对象配套}}。",
                "",
                "产品族||产品等级||品牌（产品族）||产品类型||同一产品族内对象配套",
                "设计决策：考虑产品族和产品等级哪个变化更频繁。如果经常加新品牌（新厂商）——抽象工厂适合。如果经常加新类型（新品类）——抽象工厂不适用，应考虑工厂方法或其他方案。",
                "",
                "",
                "",
            ],
            ["ch5", "abstract-factory", "concepts", "fill", "multi-cloze"],
        ),

        # ═══ Q01 · 原则综合诊断 · 问答 ═══
        note(
            model,
            [
                "Q01",
                "qa",
                "分析以下飞机大战代码违反了哪些设计原则，并逐一说明原因和改进方案。\nclass GameLoop {\n    NormalEnemy[] enemies;\n    void update() {\n        for (NormalEnemy e : enemies) {\n            e.y += e.speed;\n            if (e.hp <= 0) { score += e.getValue(); }\n        }\n    }\n}",
                "",
                "违反的原则：① DIP——GameLoop 依赖具体类 NormalEnemy 而非抽象 Enemy，无法处理其他敌机类型。改进：改为 Enemy[] 数组，所有敌机类型都继承 Enemy。② 直接访问 e.y、e.hp、e.speed——违反封装。改进：调用 e.move() 和 e.isDead()。③ OCP——加新敌机类型需修改 GameLoop。改进：改用抽象 Enemy + 多态的 move()。④ 直接在 GameLoop 中修改 score——违反 SRP（GameLoop 该管游戏循环而非分数）。改进：分数交给 ScoreManager。改进后代码：class GameLoop { Enemy[] enemies; ScoreManager scoreMgr; void update() { for (Enemy e : enemies) { e.move(); if (e.isDead()) scoreMgr.add(e.getScore()); } } }",
                "这道题综合考察了 SRP/OCP/DIP/封装——一道题同时违反多个原则是考试中的典型模式。关键思维：看到具体类名出现在方法体/字段声明中 → 违反 DIP；看到字段直接访问 → 违反封装；看到 if-else 按类型分派 → 可能违反 OCP。",
                "",
                "",
                "",
            ],
            ["ch5", "principles", "diagnosis", "qa"],
        ),
        # ═══ Q02 · LSP 反例 · 问答 ═══
        note(
            model,
            [
                "Q02",
                "qa",
                "为什么说「子类覆盖父类方法时抛出 UnsupportedOperationException」违反了里氏代换原则（LSP）？给出飞机大战中的例子。",
                "",
                "因为父类的契约是「所有 Enemy 都可以 move()」。如果子类写了 throw new UnsupportedOperationException(\"这种敌机不会移动\")，那么任何使用 Enemy 引用调用 move() 的代码都可能突然遇到运行时异常——这破坏了「子类可以透明替代父类」的保证。LSP 要求子类的方法不能弱化父类契约——前置条件不能加强（不能多要求参数条件），后置条件不能减弱（不能少做保证结果）。正确的做法：如果某种敌机真的不移动，应该在 move() 中留空方法体（什么都不做也是合法实现，行为可预期），而不是抛异常让调用方崩溃。或者重新审视类层次设计——这种敌机真的 is-a Enemy 吗？",
                "核心测试：如果某个子类让你在使用父类引用时不得不写 instanceof 检查，那么它很可能违反了 LSP。",
                "",
                "",
                "",
            ],
            ["ch5", "LSP", "counter-example", "qa"],
        ),
        # ═══ Q03 · 披萨店工厂方法 · 问答 ═══
        note(
            model,
            [
                "Q03",
                "qa",
                "写出披萨店案例中工厂方法模式的完整代码结构：PizzaStore（抽象 Creator）、NYPizzaStore（ConcreteCreator）、Pizza（抽象 Product）、NYStyleCheesePizza（ConcreteProduct）。说明 orderPizza() 为什么不需要知道具体是哪种披萨。",
                "",
                "public abstract class PizzaStore {\n    public Pizza orderPizza(String type) {\n        Pizza pizza = createPizza(type);  // 工厂方法\n        pizza.prepare(); pizza.bake(); pizza.cut(); pizza.box();\n        return pizza;\n    }\n    protected abstract Pizza createPizza(String type);  // 工厂方法\n}\n\npublic class NYPizzaStore extends PizzaStore {\n    @Override protected Pizza createPizza(String type) {\n        switch(type) {\n            case \"cheese\": return new NYStyleCheesePizza();\n            case \"veggie\": return new NYStyleVeggiePizza();\n            default: return null;\n        }\n    }\n}\n\norderPizza() 不需要知道具体类型，因为它只与抽象 Product（Pizza）交互——prepare/bake/cut/box 是所有披萨的通用流程。具体是纽约芝士还是芝加哥素食，由 createPizza() 的运行时多态决定。这就是「依赖抽象而非具体」——orderPizza() 依赖抽象的 createPizza() 和抽象的 Pizza，不依赖任何具体子类。",
                "工厂方法的精妙之处：超类的 orderPizza() 是稳定的框架代码（不变），子类的 createPizza() 是变化点（可变）。框架调用变化点——这是模板方法模式（Template Method）的雏形，后面章节会讲。",
                "",
                "",
                "",
            ],
            ["ch5", "factory-method", "pizza", "qa"],
        ),
        # ═══ Q04 · 工厂三兄弟对比 · 问答 ═══
        note(
            model,
            [
                "Q04",
                "qa",
                "从创建目标的粒度、OCP 符合程度、使用场景三个维度，对比简单工厂、工厂方法和抽象工厂。",
                "",
                "① 创建目标粒度：简单工厂——一个工厂创建所有类型的一种产品。工厂方法——每个具体工厂创建一个具体产品，一个工厂体系只创建一种产品（如只创建 Pizza）。抽象工厂——一个工厂创建一整个产品族（如同时创建 Phone + Router + Laptop）。② OCP 符合程度：简单工厂——不符合（加产品需改工厂的 if-else）。工厂方法——符合（加产品 = 新建 ConcreteCreator + ConcreteProduct）。抽象工厂——新增品牌符合（新建工厂子类），新增产品类型不符合（需改接口和所有实现）。③ 使用场景：简单工厂——产品种类少且稳定。工厂方法——产品种类会不断增加，但每次只创建「一种」产品。抽象工厂——需要保证创建的一组产品配套使用（如 UI 组件库：Windows 工厂创建 Windows 风格的按钮+文本框+下拉框，Mac 工厂创建 Mac 风格的）。",
                "三者可以组合——抽象工厂内部可以用工厂方法来实现每种具体产品的创建。",
                "",
                "",
                "",
            ],
            ["ch5", "factory", "comparison", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 第五章 设计模式导论", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
