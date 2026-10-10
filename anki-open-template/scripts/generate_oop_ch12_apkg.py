from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400522
OUTPUT = ROOT / "anki-第十二章-网络编程与观察者模式.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════ 网络基础 ═══════════
        # ═══ C01 · IP 与 DNS · 单选 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "以下关于 IP 地址和 DNS 的描述，哪项是正确的？",
                "一个 IP 地址对应一台计算机||IP 地址用于唯一标识网络接口（Network Interface）——一台机器可以有多个 IP（多网卡）。DNS 将域名映射为 IP 地址。127.0.0.1 是本机回环地址||IPv4 地址是无限的||DNS 将 IP 地址映射为域名",
                "2",
                "IP = 网络接口的唯一标识——一张网卡一个 IP，一台机器可以多个 IP。IPv4 = 32 位（如 101.202.99.12，已耗尽），IPv6 = 128 位。127.0.0.1 = 本机回环地址（localhost）。DNS 域名系统——域名→IP 的映射。域名结构：主机名.本地名.组名.最高层域名（如 www.baidu.com）。",
                "",
                "",
                "",
            ],
            ["ch12", "ip", "dns", "choice"],
        ),
        # ═══ C02 · TCP vs UDP · 单选 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "关于 TCP 和 UDP，以下哪项是正确的？",
                "UDP 比 TCP 更可靠||TCP 是面向连接的、可靠的、基于字节流的协议——保证送达和顺序。UDP 是无连接的——不保证送达，可能丢包乱序，但速度更快||TCP 是无连接的||TCP 和 UDP 没有区别",
                "2",
                "TCP：面向连接（三次握手建立连接）、可靠（确认/重传/排序）、字节流传输。适合文件传输、网页、排行榜上传等需要完整数据的场景。UDP：无连接、不可靠（可能丢包/乱序/重复）、数据报传输。适合实时视频、游戏位置同步等允许部分丢包但要求低延迟的场景。Java 在 java.net 包中提供两者的支持：TCP 用 Socket/ServerSocket，UDP 用 DatagramSocket。",
                "",
                "",
                "",
            ],
            ["ch12", "tcp", "udp", "choice"],
        ),

        # ═══════════ Socket 编程 ═══════════
        # ═══ C03 · Socket 概念 · 单选 ═══
        note(
            model,
            [
                "C03",
                "choice",
                "Socket（套接字）是什么？由什么唯一确定？ServerSocket 和 Socket 各自用于什么？",
                "Socket 是一种网络传输介质||Socket 是 TCP 通信的抽象端点，由 IP 地址 + 端口号唯一确定。ServerSocket 在服务器端监听端口（accept 阻塞等连接），Socket 用于两端实际数据传输——连接建立后两端都使用 Socket 的 I/O 流通信||Socket 是 UDP 的概念||Socket 就是 IP 地址的别名",
                "2",
                "Socket = IP + Port——一个端口的唯一标识。ServerSocket：服务器端专用，绑定端口监听。accept() = 阻塞方法——没有客户端连接时一直等，有连接返回一个新的 Socket 对象用于与该客户端通信。原 ServerSocket 继续监听下一个连接。连接建立后，服务器端和客户端都使用 Socket实例（而非 ServerSocket）进行通信——通过 getInputStream() 和 getOutputStream() 获取字节流。TCP 是字节流，Java 将其封装为标准 I/O 流——读写和文件 I/O 类似。",
                "",
                "",
                "",
            ],
            ["ch12", "socket", "concept", "choice"],
        ),
        # ═══ C04 · Socket 连接流程 · 单选 ═══
        note(
            model,
            [
                "C04",
                "choice",
                "TCP Socket 通信的完整建立流程是什么？accept() 方法的行为是什么？",
                "客户端直接调用服务器的所有方法||服务器：new ServerSocket(port) → accept() 阻塞等连接 → 返回新 Socket。客户端：new Socket(host, port) → 连接成功返回 Socket。之后两端通过 Socket.getInputStream/getOutputStream 获得 I/O 流进行双向通信||服务器和客户端同时调用 accept||只需要 Socket，不需要 ServerSocket",
                "2",
                "完整流程：① 服务器 new ServerSocket(6666)——在 6666 端口监听；② 服务器调用 accept()——阻塞，等待客户端连接请求；③ 客户端 new Socket(\"localhost\", 6666)——请求连接；④ accept() 返回一个新的 Socket 对象，服务器通过此 Socket 与该客户端通信。此后两端通过 Socket.getInputStream/getOutputStream 获取流——InputStream 读对方发来的数据，OutputStream 向对方写数据。ServerSocket 仅用于 accept，不参与实际数据传输。",
                "",
                "",
                "",
            ],
            ["ch12", "socket", "flow", "choice"],
        ),

        # ═══════════ URL ═══════════
        # ═══ C05 · URL 结构 · 单选 ═══
        note(
            model,
            [
                "C05",
                "choice",
                "URL 由哪四部分组成？URL 构造方法有哪四种形式？",
                "只有协议和主机名两部分||四部分：协议://主机名:端口/路径?查询。四种构造：① URL(String str) 完整字符串；② URL(protocol, host, file) 不指定端口；③ URL(protocol, host, port, file) 全部指定；④ URL(URL base, String relative) 基于已有 URL 的相对路径||URL 有无限种构造方法||URL 格式不固定",
                "2",
                "URL 结构：协议（http/https/ftp/file）→ 主机（域名或 IP）→ 端口（可选，默认 80/443）→ 路径和查询。读网页：URL.openStream() 返回 InputStream → 用 InputStreamReader 和 BufferedReader 包装 → 逐行读取。只能读取不能写入——与 Socket 不同。Socket 可双向通信且可同时多客户端；URL 被动响应单次请求。",
                "",
                "",
                "",
            ],
            ["ch12", "url", "structure", "choice"],
        ),

        # ═══════════ 观察者模式 ═══════════
        # ═══ C06 · 观察者四角色 · 单选 ═══
        note(
            model,
            [
                "C06",
                "choice",
                "观察者模式（Observer Pattern）的四个角色分别是什么？各自承担什么职责？",
                "发布者、订阅者、消息、队列||抽象目标（Subject——维护观察者集合 + attach/detach + notify）、具体目标（ConcreteSubject——状态变化时 notify）、抽象观察者（Observer——定义 update 接口）、具体观察者（ConcreteObserver——实现 update 响应变化）||生产者、消费者、缓冲区、锁||发送方、接收方、通道、协议",
                "2",
                "观察者模式 = 对象间一对多依赖关系——一个目标变化，所有依赖它的观察者自动收到通知并更新。别名：发布-订阅（Publish/Subscribe）、模型-视图（Model/View）、源-监听器（Source/Listener）。四角色：① Subject——管理观察者列表，定义 attach/detach/notify；② ConcreteSubject——调用 notify 通知所有观察者；③ Observer——定义 update/response；④ ConcreteObserver——具体响应逻辑。",
                "",
                "",
                "",
            ],
            ["ch12", "observer", "roles", "choice"],
        ),
        # ═══ C07 · 观察者设计原则 · 多选 ═══
        note(
            model,
            [
                "C07",
                "choice",
                "观察者模式体现了哪些设计原则？（多选）",
                "单一职责原则（SRP）——Subject 管数据，Observer 管显示||开闭原则（OCP）——增加新观察者不需修改目标代码||依赖倒转原则（DIP）——Subject 只依赖 Observer 接口||里氏代换原则（LSP）——ConcreteObserver 可替换 Observer||合成复用原则（CARP）——优先组合而非继承||接口隔离原则（ISP）——Observer 接口只有一个方法",
                "1||2||3",
                "观察者体现三大原则：① SRP——数据与显示分离；② OCP——增加新观察者（如加 Dog）只需实现 Observer 接口，Subject 代码不动；③ DIP——Subject 依赖抽象 Observer 接口而非具体 Mouse/Dog。缺点：① 通知所有观察者耗时；② 循环依赖可能导致崩溃；③ 观察者只知道目标变了，不知道具体怎么变的。",
                "",
                "",
                "",
            ],
            ["ch12", "observer", "principles", "choice", "multi"],
        ),
        # ═══ C08 · 观察者 vs MVC · 单选 ═══
        note(
            model,
            [
                "C08",
                "choice",
                "观察者模式和 MVC 模式是什么关系？",
                "完全无关的两种模式||观察者是 MVC 的重要组成部分——在 MVC 中，Model 作为 Subject，View 作为 Observer。当 Model 状态改变时，通过观察者机制通知所有 View 刷新||MVC 是观察者的子集||观察者是 MVC 的子集",
                "2",
                "观察者 vs MVC：MVC 中的 Model（目标）持有 View（观察者）列表。Model 状态变化 → notifyObservers() → 所有 View.update() → 重新渲染。这正是观察者模式的典型应用。区别：观察者是通用设计模式（适用任何一对多通知场景）；MVC 是特定的架构模式（专门用于 UI 与数据的分离）。MVC 不仅有观察者机制，还有 Controller 处理输入。Swing 的事件监听机制（addActionListener）本质也是观察者模式——Button 是 Subject，Listener 是 Observer。",
                "",
                "",
                "",
            ],
            ["ch12", "observer", "vs-mvc", "choice"],
        ),

        # ═══ F01 · Socket 流程 · 填空 ═══
        note(
            model,
            [
                "F01",
                "fill",
                "TCP Socket 连接四步：① 服务器 {{c1::new ServerSocket(port)}} 监听端口；② 服务器 {{c2::accept()}}——阻塞等客户端连接，返回{{c3::新 Socket}}；③ 客户端 {{c4::new Socket(host, port)}} 请求连接；④ 两端通过 Socket 的 {{c5::getInputStream()/getOutputStream()}} 获取流通信。TCP 是{{c6::面向连接}}的可靠字节流协议。127.0.0.1 是{{c7::本机回环地址}}。",
                "",
                "new ServerSocket(port)||accept()||新 Socket||new Socket(host, port)||getInputStream()/getOutputStream()||面向连接||本机回环地址",
                "TCP 保证可靠——数据无差错、不丢失、不重复、按序到达。ServerSocket 只用于监听和 accept，实际数据传输全部通过 Socket。底层 Java 将 Socket 流封装为标准 I/O 流——和使用文件 IO 一样简单。",
                "",
                "",
                "",
            ],
            ["ch12", "socket", "fill", "multi-cloze"],
        ),
        # ═══ F02 · 观察者模式 · 填空 ═══
        note(
            model,
            [
                "F02",
                "fill",
                "观察者模式四角色：{{c1::Subject}}(抽象目标)——维护 observers 列表 + attach/detach/notify；{{c2::ConcreteSubject}}(具体目标)——状态变化时调 notify；{{c3::Observer}}(抽象观察者)——定义 update 接口；{{c4::ConcreteObserver}}(具体观察者)——实现 update。别名：{{c5::发布-订阅}}模式 / {{c6::模型-视图}}模式 / 源-监听器模式。体现三大原则：{{c7::SRP/OCP/DIP}}。",
                "",
                "Subject||ConcreteSubject||Observer||ConcreteObserver||发布-订阅||模型-视图||SRP/OCP/DIP",
                "优缺点——优：分离表示层和数据层、抽象耦合、广播通信、符合 OCP。缺：通知所有观察者耗时、循环依赖可致崩溃、观察者不知变化细节。Swing 的 addActionListener 就是观察者模式——Button(Subject) + ActionListener(Observer)。",
                "",
                "",
                "",
            ],
            ["ch12", "observer", "fill", "multi-cloze"],
        ),

        # ═══ Q01 · Socket 通信代码 · 问答 ═══
        note(
            model,
            [
                "Q01",
                "qa",
                "写出飞机大战分数上传的 Socket 通信完整代码。服务器监听 6666 端口，接收客户端发送的 \"Name:Score\" 格式分数并打印。客户端发送 \"Player1:2500\"。",
                "",
                "// 服务器端\nServerSocket ss = new ServerSocket(6666);\nSystem.out.println(\"服务器启动，等待连接...\");\nSocket s = ss.accept();\nSystem.out.println(\"客户端已连接: \" + s.getInetAddress());\nBufferedReader in = new BufferedReader(\n    new InputStreamReader(s.getInputStream()));\nString data = in.readLine();\nSystem.out.println(\"收到分数: \" + data);\ns.close();\nss.close();\n\n// 客户端\nSocket s = new Socket(\"localhost\", 6666);\nPrintWriter out = new PrintWriter(s.getOutputStream(), true);\nout.println(\"Player1:2500\");  // true = autoFlush\nout.close();\ns.close();",
                "考察点：① ServerSocket vs Socket 分工——ServerSocket 只 accept，返回的 Socket 用于通信；② accept() 阻塞——直到有客户端连接才返回；③ getOutputStream 获得的 OutputStream 用 PrintWriter 包装（第二个参数 true = autoFlush）方便写字符串行；④ 关闭顺序——先关流再关 Socket——用 try-with-resources 更安全；⑤ 服务器端可循环 accept() 处理多个客户端：while(true) { Socket s = ss.accept(); handle(s); }。",
                "",
                "",
                "",
            ],
            ["ch12", "socket", "example", "qa"],
        ),
        # ═══ Q02 · 观察者模式飞机大战 · 问答 ═══
        note(
            model,
            [
                "Q02",
                "qa",
                "写出飞机大战中「游戏状态变化通知 UI」的观察者模式完整代码。GameState（具体目标）持有分数和敌机数量，变化时通知 ScorePanel 和 EnemyPanel（具体观察者）。要求四角色齐全，并说明体现了哪些设计原则。",
                "",
                "// 抽象观察者\npublic interface GameObserver {\n    void onGameStateChanged(int score, int enemyCount);\n}\n\n// 抽象目标\npublic abstract class GameSubject {\n    protected List<GameObserver> observers = new ArrayList<>();\n    public void attach(GameObserver o) { observers.add(o); }\n    public void detach(GameObserver o) { observers.remove(o); }\n    protected void notifyObservers(int score, int count) {\n        for (GameObserver o : observers) o.onGameStateChanged(score, count);\n    }\n}\n\n// 具体目标\npublic class GameState extends GameSubject {\n    private int score, enemyCount;\n    public void addScore(int pts) {\n        score += pts; enemyCount = calcEnemyCount();\n        notifyObservers(score, enemyCount);  // 状态改变 → 通知\n    }\n}\n\n// 具体观察者\npublic class ScorePanel implements GameObserver {\n    public void onGameStateChanged(int score, int count) {\n        repaintScore(score);  // 刷新分数显示\n    }\n}\n\npublic class EnemyPanel implements GameObserver {\n    public void onGameStateChanged(int score, int count) {\n        repaintEnemies(count);  // 刷新敌机数量显示\n    }\n}",
                "体现的设计原则：① SRP——GameState 只管游戏数据，ScorePanel/EnemyPanel 只管 UI 显示；② OCP——要加新的 UI 面板（如道具面板 ItemPanel），只需新建一个类实现 GameObserver 并 attach 到 GameState——已有代码不动；③ DIP——GameState 只依赖抽象的 GameObserver 接口，不依赖具体的 ScorePanel/EnemyPanel。对比 MVC：这里的 GameState = Model，ScorePanel/EnemyPanel = View，两者通过观察者机制通知——MVC 中的 Model→View 通信用的就是观察者模式。",
                "",
                "",
                "",
            ],
            ["ch12", "observer", "example", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 第十二章 网络编程与观察者模式", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
