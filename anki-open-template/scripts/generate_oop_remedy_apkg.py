from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400599
OUTPUT = ROOT / "anki-补漏卡.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══ 线程状态：6 种而非 5 种 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "Java 线程有几种状态？Waiting 和 Timed Waiting 算同一种还是两种？",
                "5 种——Waiting 和 Timed Waiting 是同一种||6 种——新建(New)、可运行(Runnable)、阻塞(Blocked)、等待(Waiting)、计时等待(Timed Waiting)、终止(Terminated)。Waiting 和 Timed Waiting 是不同的状态||4 种——新建、运行、等待、终止||7 种——多了暂停状态",
                "2",
                "6 种状态严格区分：① 新建——new Thread() 后；② 可运行——start() 后等 CPU；③ 阻塞——争 synchronized 锁失败；④ 等待——wait()/join() 后无限等 notify；⑤ 计时等待——sleep(ms)/wait(ms)/join(ms) 限时等，时间到自动返回；⑥ 终止——run() 结束或异常。Waiting 和 Timed Waiting 的核心区别：Waiting 必须被外部唤醒（notify/notifyAll）；Timed Waiting 可以在指定时间自行返回——不需要外部唤醒。",
                "",
                "",
                "",
            ],
            ["remedy", "thread", "6-states", "choice"],
        ),
        # ═══ 数组声明不能带长度 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "以下数组声明中，哪个会导致编译错误？",
                "int[] a = new int[5];||int[] a = {1, 2, 3};||int a[5];||int[] a = new int[]{1, 2, 3};",
                "3",
                "Java 数组声明规则：声明时不能指定长度——int a[5] 是 C 风格的写法，在 Java 中编译错误。正确的写法：① 只声明：int[] a；② 声明 + 创建定长：int[] a = new int[5]；③ 声明 + 静态初始化：int[] a = {1,2,3} 或 int[] a = new int[]{1,2,3}。长度信息在 new 时给出（动态）或由初始化元素个数推断（静态），不在声明部分写。和 C 的重要区别——C 允许 int a[5]，Java 不允许。",
                "",
                "",
                "",
            ],
            ["remedy", "array", "declaration", "choice"],
        ),
        # ═══ GoF 23 种完整分类 · 填空 ═══
        note(
            model,
            [
                "C03",
                "fill",
                "GoF 23 种设计模式按目的+范围分类：类模式——创建型：{{c1::工厂方法}}；结构型：{{c2::适配器（类）}}；行为型：{{c3::模板方法}}、{{c4::解释器}}。对象模式——创建型：{{c5::抽象工厂、生成器、原型、单例}}；结构型：适配器（对象）、桥接、组合、装饰、外观、享元、代理；行为型：职责链、命令、迭代器、中介者、备忘录、{{c6::观察者}}、状态、{{c7::策略}}、访问者。总数：5(创建)+7(结构)+11(行为)=23。",
                "",
                "工厂方法||适配器（类）||模板方法||解释器||抽象工厂、生成器、原型、单例||观察者||策略",
                "分类口诀——创建型：单原工建抽（单例、原型、工厂方法、建造者、抽象工厂）。结构型：适桥组外装享代（适配器、桥接、组合、外观、装饰、享元、代理）。行为型：责命解迭中备观状策模访（职责链、命令、解释器、迭代器、中介者、备忘录、观察者、状态、策略、模板方法、访问者）。",
                "",
                "",
                "",
            ],
            ["remedy", "gof", "full-table", "fill", "multi-cloze"],
        ),
        # ═══ 抽象类 vs 接口（考试高频）· 填空 ═══
        note(
            model,
            [
                "C04",
                "fill",
                "抽象类 vs 接口完整对比表：抽象类用{{c1::abstract class}}声明，{{c2::可以}}(可以/不可以)有实例字段和构造方法，类只能继承{{c3::一个}}；接口用{{c4::interface}}声明，{{c5::不可以}}(可以/不可以)有实例字段和构造方法（只有常量 final static），类可以实现{{c6::多个}}。抽象方法是{{c7::is-a}}关系（定义骨架），接口是{{c8::can-do}}能力契约。接口方法默认{{c9::public abstract}}。",
                "",
                "abstract class||可以||一个||interface||不可以||多个||is-a||can-do||public abstract",
                "选择标准：需要共享字段/构造逻辑 → 抽象类；需要多实现/纯粹能力契约 → 接口。接口允许多继承（extends 多个接口），因为无方法体不冲突。抽象类不能实例化，可以有具体方法。",
                "",
                "",
                "",
            ],
            ["remedy", "abstract", "vs-interface", "fill", "multi-cloze"],
        ),
        # ═══ sleep vs wait 完整对照 · 填空 ═══
        note(
            model,
            [
                "C05",
                "fill",
                "sleep vs wait 完整对照：sleep 是{{c1::Thread}}类的{{c2::静态}}方法——线程休眠{{c3::不释放锁}}（释放/不释放），时间到或被打断自动醒；wait 是{{c4::Object}}类的{{c5::实例}}方法——线程等待{{c6::释放锁}}，必须在{{c7::synchronized}}块中调用，需{{c8::notify/notifyAll}}唤醒。wait 的 while 循环防{{c9::虚假唤醒}}和{{c10::条件被抢先改变}}。",
                "",
                "Thread||静态||不释放锁||Object||实例||释放锁||synchronized||notify/notifyAll||虚假唤醒||条件被抢先改变",
                "口诀：sleep = 闭眼不放手（不释放锁），wait = 松手等人叫（释放锁后等 notify）。wait 必须用 while 而非 if——被唤醒时不意味条件一定满足（可能虚假唤醒或数据已被其他唤醒的线程取走）。",
                "",
                "",
                "",
            ],
            ["remedy", "sleep", "wait", "fill", "multi-cloze"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 补漏卡", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
