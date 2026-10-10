from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400517
OUTPUT = ROOT / "anki-第七章-集合与策略迭代器模式.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════ 集合框架 ═══════════
        # ═══ C01 · 集合体系 · 单选 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "以下关于 Java 集合框架的层次关系，哪项是正确的？",
                "Map 继承自 Collection 接口||List 和 Set 实现了 Collection 接口，Map 是独立体系||ArrayList 是 LinkedList 的子类||HashSet 继承自 ArrayList",
                "2",
                "核心层次：Collection 接口 → List（有序可重复）和 Set（无序不重复）→ ArrayList/LinkedList（List 实现）、HashSet/TreeSet（Set 实现）。Map（键值对）是独立体系，不继承 Collection——HashMap 和 TreeMap 直接实现 Map 接口。所有集合类在 java.util 包中。",
                "",
                "",
                "",
            ],
            ["ch7", "collection", "hierarchy", "choice"],
        ),
        # ═══ C02 · 集合 vs 数组 · 单选 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "Java 集合与数组的核心区别是什么？",
                "集合只能存基本类型，数组只能存对象||数组长度固定，集合长度可变||集合比数组运行慢得多，不推荐使用||两者完全相同，只是名字不同",
                "2",
                "关键区别：① 数组长度创建后不可变（a.length 固定），集合容量随元素增减自动调整；② 数组可以存基本类型（int[]），集合只能存引用类型（ArrayList<Integer>——需自动装箱）；③ 集合提供丰富的增删查改 API（add/remove/contains/size），数组只有 length 和下标。飞机大战用 Enemy[] 要手动处理空洞（null）和扩容；用 ArrayList<Enemy> 则 add/remove 自动处理。",
                "",
                "",
                "",
            ],
            ["ch7", "collection", "vs-array", "choice"],
        ),

        # ═══════════ ArrayList ═══════════
        # ═══ C03 · ArrayList 底层 · 单选 ═══
        note(
            model,
            [
                "C03",
                "choice",
                "ArrayList 的底层数据结构是什么？泛型参数 <E> 有什么限制？",
                "链表——不能存 null||数组——E 不能是基本类型，必须是引用类型（如 Integer 而非 int）||哈希表——没有限制||二叉树——只能存 Comparable 类型",
                "2",
                "ArrayList 底层是 Object[] 数组。泛型 E 必须是引用类型——不能写 ArrayList<int>，应写 ArrayList<Integer>（利用自动装箱/拆箱）。扩容机制：当容量不足时，分配一个更大的数组（通常原容量的 1.5 倍），拷贝旧数据过去。类比 C 的 realloc，但 Java 自动完成且旧数组由 GC 回收。",
                "",
                "",
                "",
            ],
            ["ch7", "arraylist", "generic", "choice"],
        ),
        # ═══ C04 · ArrayList 操作 · 单选 ═══
        note(
            model,
            [
                "C04",
                "choice",
                "在 ArrayList 中，add(index, element) 和 set(index, element) 的区别是什么？",
                "没有区别——两者都是修改指定位置的元素||add 是插入——原位置及之后元素后移；set 是替换——修改指定位置的元素值||add 只能在末尾添加，set 可以在任意位置修改||add 返回 void，set 返回 boolean",
                "2",
                "add(index, element)：在指定索引插入新元素，原位置及之后所有元素后移一位，ArrayList 长度 +1。set(index, element)：用新值替换指定索引的现有元素，长度不变，返回被替换的旧值。get(index) 获取但不修改。remove(index) 删除并返回被删元素，后续元素前移。size() 返回当前元素数量。",
                "",
                "",
                "",
            ],
            ["ch7", "arraylist", "operations", "choice"],
        ),
        # ═══════════ LinkedList ═══════════
        # ═══ C05 · LinkedList vs ArrayList 性能 · 单选 ═══
        note(
            model,
            [
                "C05",
                "choice",
                "关于 ArrayList 和 LinkedList 的性能，以下哪项描述是正确的？",
                "LinkedList 在任意位置的插入和删除都比 ArrayList 快||ArrayList 的随机访问（get）是 O(1)，LinkedList 是 O(n)；LinkedList 的头部增删是 O(1)，ArrayList 是 O(n)||两者完全等价，性能相同||ArrayList 在任何操作上都比 LinkedList 快",
                "2",
                "精确对比：① 随机访问——ArrayList O(1)（数组直接下标），LinkedList O(n)（链表需逐个遍历）；② 头部增删——LinkedList O(1)（改指针），ArrayList O(n)（所有元素后移）；③ 中间增删——两者都是 O(n)——ArrayList 费在移动元素，LinkedList 费在移动到目标位置（从头部逐节点走到索引位置）。④ 尾部增删——两者都是 O(1)。结论：频繁随机访问用 ArrayList，频繁头尾增删用 LinkedList。",
                "",
                "",
                "",
            ],
            ["ch7", "arraylist", "linkedlist", "performance", "choice"],
        ),
        # ═══ C06 · LinkedList 中间插入 · 单选 ═══
        note(
            model,
            [
                "C06",
                "choice",
                "LinkedList 在中间位置插入元素是否总是比 ArrayList 快？为什么？",
                "是，因为链表插入只需改指针（O(1)），数组需要移动元素（O(n)）||不一定——虽然改指针是 O(1)，但找到插入位置需要从头部逐节点移动到目标索引，这本身是 O(n)，当目标位置很远时总体与 ArrayList 相差不大||LinkedList 不能中间插入||LinkedList 在任何情况下都比 ArrayList 慢",
                "2",
                "这是讲义中的经典陷阱。LinkedList 的 add(index, e) 需要：① 从头部（或尾部，取较近者）逐节点遍历到 index 位置 → O(n)；② 修改前后节点的指针完成插入 → O(1)。所以总体 O(n)。ArrayList 的 add(index, e)：① 直接计算下标到达位置 → O(1)；② 移动后续所有元素 → O(n)。两者总体都是 O(n)，但常数因子不同——插入位置越靠近头部，LinkedList 越有利；越靠近尾部找特定索引，ArrayList 可能反而更快（免去遍历）。",
                "",
                "",
                "",
            ],
            ["ch7", "linkedlist", "middle-insert", "choice"],
        ),

        # ═══════════ HashSet ═══════════
        # ═══ C07 · HashSet 特性 · 单选 ═══
        note(
            model,
            [
                "C07",
                "choice",
                "关于 HashSet，以下哪项描述是错误的？",
                "HashSet 中的元素是无序的||HashSet 中不能有重复元素||HashSet 通过 hashCode() 和 equals() 共同判定元素是否重复||HashSet 中的元素按插入顺序排列",
                "4",
                "HashSet 特性：① 无序——不记录插入顺序，输出顺序不可预测；② 无重复——相同元素只存一份，重复 add 不生效也不报错；③ 判定重复用 hashCode()+equals()——先比较 hashCode，碰撞时再 equals 二次确认；④ 支持 add/remove/contains/size/clear + for-each 遍历。如需保持插入顺序，用 LinkedHashSet；如需排序，用 TreeSet。",
                "",
                "",
                "",
            ],
            ["ch7", "hashset", "characteristics", "choice"],
        ),
        # ═══════════ HashMap ═══════════
        # ═══ C08 · HashMap 特性 · 单选 ═══
        note(
            model,
            [
                "C08",
                "choice",
                "关于 HashMap，以下哪项描述是正确的？",
                "HashMap 保证按插入顺序输出||HashMap 的 key 可以重复||HashMap 根据 key 的 hashCode 存储数据，无序，最多允许一条 key 为 null||HashMap 继承自 Collection 接口",
                "3",
                "HashMap 特性：① 键值对存储——put(key, value)/get(key)/remove(key)；② key 不可重复，value 可重复；③ 无序——不保证顺序；④ 基于 hashCode 散列——存取 O(1)；⑤ 最多一条 null key；⑥ 遍历用 keySet()/values()/entrySet()。与 HashSet 的关系：HashSet 内部就是用一个 HashMap 实现的——元素作为 key，value 统一用一个占位对象。",
                "",
                "",
                "",
            ],
            ["ch7", "hashmap", "characteristics", "choice"],
        ),

        # ═══════════ 策略模式 ═══════════
        # ═══ C09 · 策略模式三角色 · 单选 ═══
        note(
            model,
            [
                "C09",
                "choice",
                "策略模式（Strategy Pattern）的三个角色分别是什么？各自对应哪部分代码？",
                "Provider/Consumer/Client||抽象策略（Strategy，接口/抽象类定义算法接口）、具体策略（ConcreteStrategy，封装具体算法）、环境（Context，持有 Strategy 引用并调用其方法）||Factory/Product/Creator||Observable/Observer/Event",
                "2",
                "三角色：① 抽象策略（Strategy）——接口或抽象类，定义所有策略的统一接口（如 calcPrice(double)）；② 具体策略（ConcreteStrategy）——实现/继承 Strategy，包装具体算法（如 8折/9折/原价）；③ 环境（Context）——持有一个 Strategy 对象的引用，对外暴露调用接口（如 Network.quote() 内部调用 strategy.calcPrice()）。客户端创建具体策略传给 Context，并决定使用哪个策略。",
                "",
                "",
                "",
            ],
            ["ch7", "strategy", "roles", "choice"],
        ),
        # ═══ C10 · 策略模式核心洞察 · 多选 ═══
        note(
            model,
            [
                "C10",
                "choice",
                "关于策略模式，以下哪些描述是正确的？（多选）",
                "策略模式的重心是组织/调用算法，而非实现算法本身||所有策略算法地位平等，可以相互替换||运行期间同一时刻只能使用一个具体策略||策略模式自动决策何时切换策略||策略类是独立的，相互之间无依赖",
                "1||2||3||5",
                "核心洞察：① 重心是组织调用而非实现——让程序结构更灵活；② 算法平等性——所有具体策略地位相同，这是可替换性的基础；③ 运行时唯一性——同一时刻只有一个策略生效（可动态切换）；④ 策略模式不决定何时换——切换决策交客户端；⑤ 策略独立——相互无依赖。缺点：客户端必须知道所有策略类并自行选择；策略多时类数量会增多。",
                "",
                "",
                "",
            ],
            ["ch7", "strategy", "insights", "choice", "multi"],
        ),
        # ═══ C11 · 策略模式优缺点 · 选错项 · 单选 ═══
        note(
            model,
            [
                "C11",
                "choice",
                "以下哪项不是策略模式的优点？",
                "提供替代继承的方法，比继承更灵活（算法独立可扩展）||将算法选择逻辑与算法本身分离，避免多重 if-else||遵守大部分设计原则，高内聚低耦合||策略模式会自动选择最优算法",
                "4",
                "优点：① 替代继承——算法封装为独立类，可自由组合替换；② 消除 if-else/switch——每个分支变成一个策略类；③ 高内聚低耦合——每个策略类高度内聚，策略间低耦合。缺点：① 客户端必须知道所有策略并自选——客户端需理解算法区别；② 策略类数量增多——每个算法一个类。选项 4 是错误的——策略模式不自动决策，决策责任在客户端。",
                "",
                "",
                "",
            ],
            ["ch7", "strategy", "pros-cons", "choice"],
        ),

        # ═══════════ 迭代器模式 ═══════════
        # ═══ C12 · Iterator 接口 · 单选 ═══
        note(
            model,
            [
                "C12",
                "choice",
                "Java Iterator 接口的三个核心方法是什么？各自的功能？",
                "add()/get()/remove()||next()/hasNext()/remove()||push()/pop()/peek()||first()/last()/size()",
                "2",
                "Iterator 三核心方法：① hasNext()——判断集合中是否还有下一个元素，返回 boolean；② next()——返回下一个元素并使迭代器前进一位；③ remove()——删除 next() 刚返回的元素。调用顺序必须是 hasNext()→next()→(可选)remove()。直接调用 remove() 而不先调用 next() 会抛出 IllegalStateException。获取迭代器：collection.iterator()。",
                "",
                "",
                "",
            ],
            ["ch7", "iterator", "methods", "choice"],
        ),
        # ═══ C13 · Iterator vs for · 单选 ═══
        note(
            model,
            [
                "C13",
                "choice",
                "与 for-i 循环相比，使用 Iterator 遍历的核心优势是什么？以及 Iterator 独有的能力？",
                "Iterator 比 for 运行更快||Iterator 将遍历行为与底层集合结构解耦——换集合类型（List→Set）遍历代码不变；且 Iterator 支持在遍历中安全删除元素（for 和 for-each 不行）||Iterator 可以反向遍历||Iterator 支持多线程并发遍历",
                "2",
                "核心优势：① 解耦——遍历代码只依赖 Iterator 接口（hasNext/next），不依赖底层是 ArrayList 还是 HashSet。如果后续把 List 改成 Set，for-i 遍历全部要改（Set 没有 get(i)），Iterator 一行不动。② 安全删除——Iterator.remove() 在遍历中删除元素不会破坏迭代状态，for 和 for-each 在遍历时直接调用集合的 remove() 会抛出 ConcurrentModificationException。缺点：简单遍历（数组/有序列表）用 for-each 更简洁。",
                "",
                "",
                "",
            ],
            ["ch7", "iterator", "vs-for", "choice"],
        ),
        # ═══ C14 · 迭代器模式本质 · 单选 ═══
        note(
            model,
            [
                "C14",
                "choice",
                "迭代器模式（Iterator Pattern）的本质是什么？它体现了哪些设计原则？",
                "一种遍历集合的语法糖||将聚合对象的遍历行为从聚合对象本身分离出来——聚合对象不需要暴露内部结构，遍历逻辑封装在迭代器中。体现 SRP（单一职责）和 OCP（开闭原则）||一种提高遍历性能的优化技术||一种多线程同步机制",
                "2",
                "迭代器模式本质：分离聚合对象的遍历行为——聚合类只负责存储数据，迭代器负责遍历逻辑。体现了：① SRP——聚合类职责单一（存数据），遍历职责交给迭代器；② OCP——新增遍历方式只需新加迭代器类，不改聚合类；③ DIP——客户端依赖抽象的 Iterator 接口而非具体集合类。类比：传送带（迭代器）不管传送的物品是什么（聚合内容），只负责一件件送达。",
                "",
                "",
                "",
            ],
            ["ch7", "iterator", "essence", "choice"],
        ),
        # ═══ C15 · for-each 删除 · 单选 ═══
        note(
            model,
            [
                "C15",
                "choice",
                "为什么在 for-each 循环中直接调用集合的 remove() 方法会抛出 ConcurrentModificationException？正确的做法是什么？",
                "因为 for-each 是只读循环||因为 for-each 内部使用迭代器，直接修改集合结构会使迭代器的 expectedModCount 与集合的 modCount 不一致，触发并发修改检查||因为 Java 禁止在任何循环中删除集合元素||因为 HashSet 不支持删除操作",
                "2",
                "for-each 是 Iterator 的语法糖——编译器将其翻译为 Iterator 的 hasNext()+next() 循环。Iterator 内部维护一个 expectedModCount（期望的修改计数），每次 next() 会检查 expectedModCount == modCount（集合的实际修改计数）。直接调用集合的 remove() 会改变 modCount 但不更新 expectedModCount → 下次 next() 时两者不等 → 抛异常。正确做法：使用 Iterator 自己的 remove()——它删除元素后会同步 expectedModCount = modCount。",
                "",
                "",
                "",
            ],
            ["ch7", "iterator", "concurrent-modification", "choice"],
        ),

        # ═══ F01 · 集合体系填空 · 填空 ═══
        note(
            model,
            [
                "F01",
                "fill",
                "Java 集合框架：{{c1::Collection}}接口下分{{c2::List}}（有序可重复）和{{c3::Set}}（无序不重复）。List 实现类：{{c4::ArrayList}}（动态数组）和{{c5::LinkedList}}（双向链表）。Set 实现类：{{c6::HashSet}}（基于 HashMap，去重）和 TreeSet（排序）。{{c7::Map}}（键值对）是独立体系，不继承 Collection，实现类有{{c8::HashMap}}和 TreeMap。",
                "",
                "Collection||List||Set||ArrayList||LinkedList||HashSet||Map||HashMap",
                "泛型 <E> 只能是引用类型（Integer 而非 int）。集合位于 java.util 包。集合 vs 数组：数组定长可直接存基本类型，集合变长但只能存引用类型（自动装箱）。",
                "",
                "",
                "",
            ],
            ["ch7", "collection", "hierarchy", "fill", "multi-cloze"],
        ),
        # ═══ F02 · List 操作对比 · 填空 ═══
        note(
            model,
            [
                "F02",
                "fill",
                "ArrayList 核心操作：尾部添加{{c1::add(e)}}、指定位置插入{{c2::add(index, e)}}、获取{{c3::get(index)}}、替换{{c4::set(index, e)}}、删除{{c5::remove(index)}}、大小{{c6::size()}}。LinkedList 独有操作：头部添删{{c7::addFirst/removeFirst}}、尾部添删{{c8::addLast/removeLast}}、获取头尾{{c9::getFirst/getLast}}。",
                "",
                "add(e)||add(index, e)||get(index)||set(index, e)||remove(index)||size()||addFirst/removeFirst||addLast/removeLast||getFirst/getLast",
                "ArrayList 底层 Object[]，自动扩容（约 1.5 倍）。LinkedList 底层双向链表。性能口诀：随机访问用 ArrayList（O(1)），频繁头尾增删用 LinkedList（O(1)），中间增删两者都是 O(n)——LinkedList 费在找位置，ArrayList 费在移元素。",
                "",
                "",
                "",
            ],
            ["ch7", "list", "operations", "fill", "multi-cloze"],
        ),
        # ═══ F03 · 策略模式 · 填空 ═══
        note(
            model,
            [
                "F03",
                "fill",
                "策略模式三角色：① {{c1::抽象策略}}(Strategy)——接口/抽象类定义算法接口；② {{c2::具体策略}}(ConcreteStrategy)——封装具体算法实现；③ {{c3::环境}}(Context)——持有 Strategy 引用，调用策略方法。客户端创建具体策略传给 Context 并决定{{c4::使用哪个策略}}。核心特性：算法{{c5::平等性}}（可相互替换）、运行时{{c6::唯一性}}（同一时刻只有一个策略），切换由{{c7::客户端}}决定。",
                "",
                "抽象策略||具体策略||环境||使用哪个策略||平等性||唯一性||客户端",
                "策略模式是 OCP 和 DIP 的典型体现——加新算法（策略）不改 Context，Context 依赖抽象 Strategy 而非具体策略类。缺点：客户端需了解所有策略类；策略多时类数量多。",
                "",
                "",
                "",
            ],
            ["ch7", "strategy", "roles", "fill", "multi-cloze"],
        ),
        # ═══ F04 · Iterator · 填空 ═══
        note(
            model,
            [
                "F04",
                "fill",
                "Iterator 三核心方法：{{c1::hasNext()}}判断是否有下一个、{{c2::next()}}返回下一个元素并前进、{{c3::remove()}}删除刚返回的元素。获取迭代器：{{c4::collection.iterator()}}。在遍历中删除元素必须用{{c5::Iterator.remove()}}，直接调用集合的 remove() 会抛{{c6::ConcurrentModificationException}}——因为集合的 modCount 与迭代器的 expectedModCount 不一致。",
                "",
                "hasNext()||next()||remove()||collection.iterator()||Iterator.remove()||ConcurrentModificationException",
                "for-each 是 Iterator 的语法糖。本质是 SRP（聚合只负责存，迭代只负责遍历）+ OCP（新增遍历方式不改聚合类）+ DIP（客户端依赖 Iterator 接口）。换底层集合（List→Set），Iterator 遍历代码不变，for-i 遍历要改。",
                "",
                "",
                "",
            ],
            ["ch7", "iterator", "fill", "multi-cloze"],
        ),

        # ═══ Q01 · List 选型解答 · 问答 ═══
        note(
            model,
            [
                "Q01",
                "qa",
                "飞机大战中需要存储屏幕上的所有敌机，频繁操作包括：① 遍历所有敌机进行移动和碰撞检测（每秒 60 次）；② 敌机被击杀时删除；③ 波次开始时批量添加新敌机。应选 ArrayList 还是 LinkedList？说明理由。",
                "",
                "选 ArrayList。理由：① 核心操作是「遍历所有敌机进行 move() 和碰撞检测」，每秒 60 次——ArrayList 的 O(1) 随机访问 for-i 遍历和缓存友好性（连续内存）远超 LinkedList 的逐指针跳转；② 删除操作可以用「标记删除 + 批量清理」或 Iterator.remove()，ArrayList 删尾部元素也是 O(1)；③ 批量添加在尾部用 add() 是 O(1) 均摊。LinkedList 在头尾增删有优势，但这并非飞机大战的瓶颈操作——遍历才是。实际工程中 95% 的场景选 ArrayList 即可。LinkedList 只在频繁头部增删（如队列 Deque）场景才有优势。",
                "关键判断：识别出「频率最高的操作是遍历」——这是 ArrayList 的主场。不要因为「有删除操作」就无脑选 LinkedList——删除的比例和位置才是决定性因素。",
                "",
                "",
                "",
            ],
            ["ch7", "list", "selection", "qa"],
        ),
        # ═══ Q02 · 策略模式完整代码 · 问答 ═══
        note(
            model,
            [
                "Q02",
                "qa",
                "写出飞机大战中「难度策略」的策略模式完整实现。游戏难度（Easy/Normal/Hard）决定敌机生成速度、敌机血量倍率、道具掉落率。要求：接口 DifficultyStrategy + 三个具体策略类 + GameContext 环境类 + Client 使用示例。",
                "",
                "public interface DifficultyStrategy {\n    int getSpawnInterval();   // 敌机生成间隔（ms）\n    double getHpMultiplier();  // 血量倍率\n    double getDropRate();      // 道具掉落概率\n}\n\npublic class EasyStrategy implements DifficultyStrategy {\n    public int getSpawnInterval() { return 3000; }\n    public double getHpMultiplier() { return 0.7; }\n    public double getDropRate() { return 0.15; }\n}\n\npublic class NormalStrategy implements DifficultyStrategy {\n    public int getSpawnInterval() { return 2000; }\n    public double getHpMultiplier() { return 1.0; }\n    public double getDropRate() { return 0.08; }\n}\n\npublic class HardStrategy implements DifficultyStrategy {\n    public int getSpawnInterval() { return 1000; }\n    public double getHpMultiplier() { return 1.5; }\n    public double getDropRate() { return 0.03; }\n}\n\npublic class GameContext {\n    private DifficultyStrategy strategy;\n    public void setStrategy(DifficultyStrategy s) { this.strategy = s; }\n    public int getSpawnInterval() { return strategy.getSpawnInterval(); }\n    public double getHpMultiplier() { return strategy.getHpMultiplier(); }\n    public double getDropRate() { return strategy.getDropRate(); }\n}\n\n// Client\nGameContext ctx = new GameContext();\nctx.setStrategy(new HardStrategy());\nint interval = ctx.getSpawnInterval();  // 1000ms\n// 通一关后换难度：ctx.setStrategy(new NormalStrategy());",
                "考三个设计原则落地：① OCP——加新难度（如 Hell 难度）只需新建一个 HellStrategy 类，不改 GameContext 和现有策略；② DIP——GameContext 依赖抽象的 DifficultyStrategy 接口而非具体策略类；③ 策略模式的 if-else 替代——不在 spawnEnemy() 里写 if(difficulty==EASY) ... else if(difficulty==HARD) ...。",
                "",
                "",
                "",
            ],
            ["ch7", "strategy", "example", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 第七章 集合与策略迭代器模式", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
