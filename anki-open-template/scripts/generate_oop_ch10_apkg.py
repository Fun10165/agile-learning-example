from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400520
OUTPUT = ROOT / "anki-第十章-多线程.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════ 进程与线程 ═══════════
        # ═══ C01 · 进程 vs 线程 · 单选 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "进程和线程的核心区别是什么？线程之间共享什么、不共享什么？",
                "没有区别——进程就是线程||进程是 OS 分配资源的基本单位（私有地址空间，不共享内存），线程是 OS 调度的最小单位（同一进程内共享堆和方法区，不共享栈和程序计数器）||线程是进程的一种||进程比线程更轻量级",
                "2",
                "进程（Process）：正在运行的程序的实例，OS 资源分配的基本单位。私有地址空间——不同进程间不共享内存，通过 IPC（消息传递）通信。线程（Thread）：进程内的单一顺序控制流，OS 调度的最小单位。同进程线程共享：堆（对象实例）+ 方法区（类信息、静态字段）。不共享：栈（每线程独立栈帧）+ 程序计数器。一个进程至少一个线程。类比：进程 = 工厂（独立厂房），线程 = 工人（共享厂房内的设备）。",
                "",
                "",
                "",
            ],
            ["ch10", "process", "thread", "choice"],
        ),
        # ═══ C02 · 线程状态 · 单选 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "Java 线程的五种状态是什么？start() 后线程进入什么状态？",
                "创建→运行→暂停→恢复→终止||新建(New)→可运行(Runnable)→运行(Running)→阻塞/等待(Blocked/Waiting)→终止(Terminated)。start() 后进入可运行（就绪）状态——等 OS 分配 CPU 时间片||开始→执行→等待→唤醒→结束||活着和死了两种状态",
                "2",
                "五种状态：① 新建——new Thread() 后；② 可运行——start() 后，等待 CPU 调度；③ 阻塞——争抢锁失败或被主动暂停（wait/sleep/join）；④ 等待——wait() 后等 notify，或计时等待（sleep(time)/wait(time)/join(time)）；⑤ 终止——run() 正常结束或未捕获异常。阻塞 vs 等待：阻塞是被动等锁，等待是主动暂歇。",
                "",
                "",
                "",
            ],
            ["ch10", "thread", "states", "choice"],
        ),
        # ═══ C03 · sleep vs wait · 单选 ═══
        note(
            model,
            [
                "C03",
                "choice",
                "sleep() 和 wait() 的核心区别是什么？（考试重点）",
                "没有区别——都是让线程暂停||sleep 是 Thread 的静态方法——线程休眠不释放锁；wait 是 Object 的实例方法——释放锁并等待 notify 唤醒。sleep 任何地方可用，wait 必须在 synchronized 块中调用||sleep 是 Object 方法，wait 是 Thread 方法||sleep 释放锁，wait 不释放锁",
                "2",
                "sleep vs wait 对照：① 归属——Thread.sleep(ms) 静态方法 vs Object.wait() 实例方法；② 锁——sleep 不释放锁 vs wait 释放锁；③ 唤醒——sleep 时间到或被打断 vs wait 需 notify/notifyAll 或被打断；④ 使用位置——sleep 任意位置 vs wait 必须在 synchronized 块内（需持有监视器锁）。场景：sleep 用于定时等待，wait 用于线程间协作（如生产者-消费者）。",
                "",
                "",
                "",
            ],
            ["ch10", "sleep", "wait", "choice"],
        ),

        # ═══════════ 线程创建与控制 ═══════════
        # ═══ C04 · 创建方式 · 单选 ═══
        note(
            model,
            [
                "C04",
                "choice",
                "Java 创建线程的两种方式是什么？为什么推荐 Runnable 而非继承 Thread？",
                "new Thread() 和 start()||继承 Thread 类（覆盖 run）和实现 Runnable 接口（实现 run）。推荐 Runnable 原因：① 任务与线程解耦——同一 Runnable 可交 Thread 或线程池执行；② Java 单继承——继承了 Thread 就不能继承其他类；③ 更容易资源共享——多线程共享同一 Runnable 实例||Runnable 和 Callable||只有一种方式——继承 Thread",
                "2",
                "两种方式：① class MyThread extends Thread { void run(){} } → new MyThread().start()；② class MyTask implements Runnable { void run(){} } → new Thread(new MyTask()).start()。Lambda 简化：new Thread(() -> { ... }).start()。关键是 .start() 而非 .run()——直接调 run() 不会创建新线程，只是同步方法调用。",
                "",
                "",
                "",
            ],
            ["ch10", "thread", "creation", "choice"],
        ),
        # ═══ C05 · 控制方法 · 多选 ═══
        note(
            model,
            [
                "C05",
                "choice",
                "以下哪些是 Java 线程控制的正确操作？（多选）",
                "thread.start()——启动线程进入就绪状态||Thread.sleep(1000)——当前线程休眠 1 秒，不释放锁||thread.join()——当前线程等待 thread 执行完毕||thread.stop()——安全终止线程||thread.interrupt()——向线程发送中断信号||thread.setDaemon(true)——必须在 start() 之前调用",
                "1||2||3||5||6",
                "正确操作：① start——启动线程（只能调一次）；② sleep(ms)——静态方法，休眠不释放锁；③ join——等目标线程结束；⑤ interrupt——设置中断标志，不强制终止线程——被中断线程自行决定响应；⑥ setDaemon——守护线程标志，必须在 start 前调用。stop 已废弃——会释放所有锁但数据可能不一致。线程被中断时应检查 isInterrupted() 并优雅退出。",
                "",
                "",
                "",
            ],
            ["ch10", "thread", "control", "choice", "multi"],
        ),
        # ═══ C06 · 守护线程 · 单选 ═══
        note(
            model,
            [
                "C06",
                "choice",
                "什么是守护线程（Daemon Thread）？Java 中最典型的守护线程是什么？",
                "守护线程比普通线程优先级更高||守护线程是为其他线程提供服务的后台线程——当所有非守护线程结束时 JVM 自动退出，守护线程被强制终止。最典型的是 GC 垃圾回收器||守护线程永远不会被终止||守护线程不能调用 sleep",
                "2",
                "守护线程特点：① 用 setDaemon(true) 设置——必须在 start() 前；② 唯一用途是服务其他线程；③ 所有非守护线程结束 → JVM 退出，守护线程被强制杀死。典型：GC、计时器发送线程。飞机大战中 BGM 线程设为守护——游戏退了音乐自然停。main 线程结束不意味进程结束——只要还有非守护线程在跑。",
                "",
                "",
                "",
            ],
            ["ch10", "daemon", "thread", "choice"],
        ),

        # ═══════════ 同步与死锁 ═══════════
        # ═══ C07 · synchronized 原理 · 单选 ═══
        note(
            model,
            [
                "C07",
                "choice",
                "synchronized 关键字在 Java 中的精确语义是什么？synchronized 方法和 synchronized(lock) 块的区别？",
                "它让代码运行更快||synchronized 锁住一个对象的监视器（monitor）——进入块的线程必须独占该锁，退出时释放。synchronized 方法 = synchronized(this) 整个过程锁定；synchronized(lock) 块可指定任意对象作为锁，粒度更细||synchronized 方法锁定类，synchronized 块锁定对象||两者没有区别",
                "2",
                "synchronized 语义：每个 Java 对象都有一个内置监视器锁（monitor）。进入 synchronized(obj) 块的线程必须先获得 obj 的锁——若已被其他线程持有，当前线程进入阻塞状态等锁。线程退出块时自动释放锁。JVM 层面：插入 monitorenter/monitorexit 指令。synchronized 实例方法锁 this，synchronized 静态方法锁 Class 对象。synchronized(obj) 块比修饰方法更灵活——可精确控制临界区范围。",
                "",
                "",
                "",
            ],
            ["ch10", "synchronized", "choice"],
        ),
        # ═══ C08 · 死锁 · 单选 ═══
        note(
            model,
            [
                "C08",
                "choice",
                "死锁的四个必要条件是什么？如何避免死锁（给出具体方案）？",
                "锁、等待、超时、重试——用 tryLock 避免||互斥、持有并等待、不可剥夺、环路等待——破坏任意一个即可。最实用的方法：破坏环路等待——所有线程按相同顺序获取锁||只有一个条件：两个线程互相等待||死锁无法避免——只能重启程序",
                "2",
                "死锁四条件：① 互斥——资源只能被一个线程持有；② 持有并等待——线程占着锁 A 等锁 B；③ 不可剥夺——锁不能被强行抢走；④ 环路等待——A 等 B，B 等 A（闭合成环）。避免方案——破坏环路等待：所有线程按相同的全局顺序获取锁。如约定锁顺序为 A→B，那么所有线程必须先拿 A 再拿 B。即使顺序不同（如 B→A）也 OK——关键是全局一致，不让环形成。",
                "",
                "",
                "",
            ],
            ["ch10", "deadlock", "choice"],
        ),

        # ═══════════ 线程池 ═══════════
        # ═══ C09 · 线程池步骤 · 单选 ═══
        note(
            model,
            [
                "C09",
                "choice",
                "ThreadPoolExecutor 收到新任务时的五步决策流程是什么？（考试重点）",
                "直接新建线程执行||① 当前线程 < corePoolSize？→ 新建线程；② ≥ corePoolSize？→ 入队列；③ 队列满？→ 线程 < maxPoolSize？→ 新建；④ 队列满且线程 = maxPoolSize？→ 执行拒绝策略；⑤ 非核心线程空闲超 keepAliveTime → 销毁||根据任务类型随机选择||所有任务先入队列再依次执行",
                "2",
                "五步流程：① 线程数 < corePoolSize → 创建核心线程直接执行，即使有空闲线程。② 线程数 ≥ corePoolSize → 任务放入 workQueue 排队。③ 队列满 + 线程数 < maximumPoolSize → 创建非核心线程执行。④ 队列满 + 线程数 = maximumPoolSize → 执行拒绝策略（默认 AbortPolicy 抛异常）。⑤ 非核心线程空闲超过 keepAliveTime → 回收销毁。七个参数：corePoolSize, maximumPoolSize, keepAliveTime, unit, workQueue, threadFactory, handler。",
                "",
                "",
                "",
            ],
            ["ch10", "threadpool", "flow", "choice"],
        ),
        # ═══ C10 · Callable · 单选 ═══
        note(
            model,
            [
                "C10",
                "choice",
                "Callable 与 Runnable 的区别是什么？FutureTask 的作用是什么？",
                "没有区别||Callable<V> 的 call() 有返回值且可抛异常，Runnable 的 run() 无返回值无异常声明。FutureTask 包装 Callable——它实现了 Runnable（可放入 Thread），同时通过 get() 方法阻塞获取执行结果||Callable 是 Runnable 的子接口||FutureTask 是 Callable 的实现类",
                "2",
                "Callable<V>：泛型接口，call() 返回 V 类型值，可声明 throws Exception。FutureTask：同时实现 Runnable 和 Future<V>——可传给 Thread 启动，用 get() 阻塞获取结果。用法：FutureTask<Integer> ft = new FutureTask<>(callable); new Thread(ft).start(); Integer result = ft.get()。线程池中直接用 executor.submit(callable) 返回 Future<V>。",
                "",
                "",
                "",
            ],
            ["ch10", "callable", "futuretask", "choice"],
        ),

        # ═══════════ 生产者-消费者 ═══════════
        # ═══ C11 · wait/notify 三铁规 · 单选 ═══
        note(
            model,
            [
                "C11",
                "choice",
                "生产者-消费者模式中使用 wait/notify 的三条铁规是什么？为什么用 while 而非 if？",
                "没有特殊规则——随意使用||① wait/notify/notifyAll 必须在 synchronized 块中调用——否则 IllegalMonitorStateException；② 用 while 而非 if 检查条件——线程被唤醒时条件可能又变了（其他线程抢先消费/生产导致）；③ 在共享对象（缓冲区）上调 wait——同一把锁同步生产者和消费者||wait 必须在 try-catch 中，notify 必须在 finally 中||wait 只能用一次，notify 可以用多次",
                "2",
                "三条铁规的深层原因：① wait 需要释放当前持有的锁——释放的前提是你确实持有一把锁（synchronized 保证）。② while 而非 if——wait 被唤醒不意味条件满足：可能是虚假唤醒、可能是 notifyAll 唤醒了多个线程但数据只够一个线程消费。while 循环在线程睡眠前后都检查条件。③ 缓冲区对象做 wait——生产者和消费者通过同一对象同步通信，确保操作缓冲区的代码互斥执行。",
                "",
                "",
                "",
            ],
            ["ch10", "wait", "notify", "rules", "choice"],
        ),
        # ═══ C12 · 生产者-消费者优点 · 单选 ═══
        note(
            model,
            [
                "C12",
                "choice",
                "生产者-消费者模式的优点是什么？它让生产者和消费者通过什么来解耦？",
                "提高单线程性能||优点：① 并发/异步——生产者和消费者各司其职互不等待，通过异步支持高并发；② 解耦——两者通过缓冲区通信，互不知道对方存在。改变生产者不影响消费者，反之亦然||没有优点||通过共享变量解耦",
                "2",
                "生产者-消费者核心设计：生产者将数据放入缓冲区（队列）后立即返回继续生产，消费者从缓冲区取数据处理。两者速率不匹配时缓冲区自动调节——生产者快则缓冲区满阻塞生产者；消费者快则缓冲区空阻塞消费者。设计原则：永远在 synchronized 方法/对象里使用 wait/notify；永远在 while 循环里而非 if 下使用 wait；永远在共享对象（缓冲区）上调 wait。",
                "",
                "",
                "",
            ],
            ["ch10", "producer-consumer", "pattern", "choice"],
        ),

        # ═══ F01 · 线程状态 · 填空 ═══
        note(
            model,
            [
                "F01",
                "fill",
                "线程五种状态：{{c1::新建}}(New)→[start()]→{{c2::可运行}}(Runnable)→[CPU]→运行→[失去CPU或暂停]→{{c3::阻塞/等待}}→{{c4::终止}}(Terminated)。{{c5::sleep}}不释放锁（Thread 静态方法），{{c6::wait}}释放锁（Object 实例方法，必须在 synchronized 块中）。守护线程用{{c7::setDaemon(true)}}设置，必须在{{c8::start()}}之前调用。stop()已{{c9::废弃}}。",
                "",
                "新建||可运行||阻塞/等待||终止||sleep||wait||setDaemon(true)||start()||废弃",
                "sleep/wait 被中断时抛出 InterruptedException。线程被中断后应检查 isInterrupted() 标志并优雅退出。join() 让调用者线程等目标线程结束。interrupt() 只设标志不强制终止——被中断线程自己决定如何响应。",
                "",
                "",
                "",
            ],
            ["ch10", "thread", "states", "fill", "multi-cloze"],
        ),
        # ═══ F02 · 线程池流程 · 填空 ═══
        note(
            model,
            [
                "F02",
                "fill",
                "ThreadPoolExecutor 五步调度流程：① 线程 < {{c1::corePoolSize}} → 新建线程；② ≥ corePoolSize → 入{{c2::workQueue}}排队；③ 队列满 + 线程 < {{c3::maximumPoolSize}} → 新建非核心线程；④ 队列满 + 线程 = max → 执行{{c4::拒绝策略}}；⑤ 非核心线程空闲 > {{c5::keepAliveTime}} → 回收销毁。七个参数：corePoolSize/maximumPoolSize/keepAliveTime/unit/workQueue/threadFactory/{{c6::handler}}。",
                "",
                "corePoolSize||workQueue||maximumPoolSize||拒绝策略||keepAliveTime||handler",
                "池化技术核心：复用线程而非反复创建/销毁——降低资源消耗、提高响应速度。默认拒绝策略 AbortPolicy 抛 RejectedExecutionException。继承关系：Executor 接口 → ExecutorService → AbstractExecutorService → ThreadPoolExecutor。",
                "",
                "",
                "",
            ],
            ["ch10", "threadpool", "fill", "multi-cloze"],
        ),
        # ═══ F03 · 死锁 · 填空 ═══
        note(
            model,
            [
                "F03",
                "fill",
                "死锁四个必要条件：{{c1::互斥}}——资源一次只有一个线程能持有；{{c2::持有并等待}}——线程占着锁等别的锁；{{c3::不可剥夺}}——锁不能被强行拿走；{{c4::环路等待}}——A等B，B等A。最实用的避免方案：破坏{{c5::环路等待}}——让所有线程按{{c6::相同顺序}}获取锁。",
                "",
                "互斥||持有并等待||不可剥夺||环路等待||环路等待||相同顺序",
                "死锁示例：线程 A 先锁 lockA 再等 lockB，线程 B 先锁 lockB 再等 lockA——形成环。修复：两者都先锁 lockA 再锁 lockB——环断开，死锁不可能发生。",
                "",
                "",
                "",
            ],
            ["ch10", "deadlock", "fill", "multi-cloze"],
        ),
        # ═══ F04 · 生产者-消费者 · 填空 ═══
        note(
            model,
            [
                "F04",
                "fill",
                "生产者-消费者模式三条铁规：① wait/notify/notifyAll 必须在{{c1::synchronized}}块中调用——否则抛 IllegalMonitorStateException；② 用{{c2::while}}而非{{c3::if}}检查条件——线程被唤醒时条件可能已变；③ 在{{c4::共享对象（缓冲区）}}上调 wait。生产者向缓冲区{{c5::put}}数据，消费者从缓冲区{{c6::take}}数据。缓冲区满→生产者{{c7::wait}}；缓冲区空→消费者{{c8::wait}}。使用{{c9::notifyAll}}唤醒所有等待线程。",
                "",
                "synchronized||while||if||共享对象（缓冲区）||put||take||wait||wait||notifyAll",
                "为什么用 notifyAll 而非 notify：notify 随机唤醒一个等待线程——可能唤醒的仍是生产者（缓冲区满）→ 再次 wait → 所有线程都沉睡（死锁）。notifyAll 唤醒所有等待线程，大家重新争锁并检查条件，符合条件的继续。",
                "",
                "",
                "",
            ],
            ["ch10", "producer-consumer", "rules", "fill", "multi-cloze"],
        ),

        # ═══ Q01 · 线程同步例题 · 问答 ═══
        note(
            model,
            [
                "Q01",
                "qa",
                "飞机大战中，两个线程分别执行 addScore() 和 getScore() 操作共享的 int totalScore。分析为什么需要 synchronized，写出带 synchronized 的完整代码，并解释 synchronized 到底锁住了什么。",
                "",
                "public class ScoreManager {\n    private int totalScore = 0;\n    // 任何一个对象都可以作为锁\n    private final Object lock = new Object();\n\n    public void addScore(int points) {\n        synchronized (lock) {        // 获取 lock 的监视器\n            totalScore += points;     // 临界区：读-改-写\n        }                             // 释放锁\n    }\n\n    public int getScore() {\n        synchronized (lock) {\n            return totalScore;\n        }\n    }\n}",
                "为什么需要 synchronized：totalScore += points 不是原子操作——对应 3 条字节码指令（ILOAD/IADD/ISTORE）。两个线程同时 addScore 时可能读到同一旧值，导致一次加法被覆盖。synchronized 做了什么：synchronized(lock) 意味着「要执行块内代码，必须独占 lock 对象的监视器」。同一时刻只有一个线程能持有该锁——其他线程在入口处阻塞等待。退出块时 JVM 自动 monitorexit 释放锁。用单独的 Object lock 而非 synchronized(this) 更安全——避免外部代码也锁同一个 ScoreManager 对象导致意外的锁竞争。",
                "",
                "",
                "",
            ],
            ["ch10", "synchronized", "example", "qa"],
        ),
        # ═══ Q02 · 生产者-消费者完整代码 · 问答 ═══
        note(
            model,
            [
                "Q02",
                "qa",
                "写出生产者-消费者模式的完整 Buffer 类。要求：① ArrayList 作为缓冲区，容量 MAX=5；② put(int) 和 take() 方法用 synchronized + wait + notifyAll；③ while 检查条件；④ 解释为什么用 notifyAll 而非 notify。",
                "",
                "public class Buffer {\n    private List<Integer> data = new ArrayList<>();\n    private static final int MAX = 5;\n\n    public synchronized void put(int value) {\n        while (data.size() == MAX) {  // while, 非 if\n            try { wait(); } catch (InterruptedException e) {\n                Thread.currentThread().interrupt(); return;\n            }\n        }\n        data.add(value);\n        System.out.println(\"produced: \" + value);\n        notifyAll();\n    }\n\n    public synchronized Integer take() {\n        while (data.isEmpty()) {\n            try { wait(); } catch (InterruptedException e) {\n                Thread.currentThread().interrupt(); return null;\n            }\n        }\n        Integer val = data.remove(0);\n        System.out.println(\"consumed: \" + val);\n        notifyAll();\n        return val;\n    }\n}",
                "为什么用 notifyAll 而非 notify：notify 随机唤醒一个等待线程——如果缓冲区刚满，两个生产者都在 wait，消费者取走一个数据后 notify 可能唤醒另一个生产者——该生产者检查条件发现仍满，再次 wait，而消费者无人唤醒 → 死锁。notifyAll 唤醒所有等待线程，大家重新争锁并 while 检查条件——符合条件的继续，不符合的再次 wait。这就是为什么 while 必须配合 notifyAll 使用。",
                "",
                "",
                "",
            ],
            ["ch10", "producer-consumer", "code", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 第十章 多线程", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
