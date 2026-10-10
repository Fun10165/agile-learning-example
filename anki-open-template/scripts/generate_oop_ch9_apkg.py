from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400519
OUTPUT = ROOT / "anki-第九章-Swing图形用户界面.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════ Swing 框架 ═══════════
        # ═══ C01 · Swing vs AWT · 单选 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "Swing 与 AWT 的关系和区别是什么？",
                "Swing 完全取代了 AWT，AWT 已废弃||Swing 构建在 AWT 之上——AWT 提供底层窗口机制和事件处理，Swing 用纯 Java 代码模拟控件，不依赖本地平台||Swing 和 AWT 是完全独立的两个 GUI 库||Swing 比 AWT 更底层",
                "2",
                "Swing 不是 AWT 的完全替代，而是构建在 AWT 架构之上。AWT 提供：窗口工具包的底层机制（如事件处理）、Component/Container 基类。Swing 提供：更丰富的 UI 组件（J* 类族）、纯 Java 实现的跨平台控件。Swing 的 JComponent 继承自 AWT 的 Container，能使用 AWT 的事件处理框架。JavaFX 是后继者，但 Java 11 起不再打包 JDK。",
                "",
                "",
                "",
            ],
            ["ch9", "swing", "awt", "choice"],
        ),
        # ═══ C02 · 组件层级 · 单选 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "关于 Swing 组件层级，以下哪项描述是正确的？",
                "所有容器都是组件，所有组件都是容器||JPanel 是中间层容器——它继承自 JComponent，本身既是组件（可放入其他容器）也是容器（可容纳其他组件）||JFrame 继承自 JComponent||JButton 是顶层容器",
                "2",
                "组件层级：Component → Container → JComponent（轻量级组件基类）。顶层容器（JFrame/JDialog/JApplet）不继承 JComponent，不被其他容器包含。中间层容器（JPanel/JScrollPane）继承 JComponent，本身也是组件——可以放入 JFrame 也可以容纳按钮等基本组件。JButton/JLabel 是基本组件，不是容器。口诀：容器都是组件，但不是所有组件都是容器。",
                "",
                "",
                "",
            ],
            ["ch9", "swing", "hierarchy", "choice"],
        ),
        # ═══ C03 · 顶层 vs 中间容器 · 单选 ═══
        note(
            model,
            [
                "C03",
                "choice",
                "Swing 中顶层容器和中间层容器的根本区别是什么？",
                "没有区别||顶层容器（JFrame/JDialog）不继承 JComponent，不能被其他容器包含；中间层容器（JPanel/JScrollPane）继承 JComponent，可被包含也可包含其他组件||顶层容器用于显示，中间层容器用于存储||顶层容器一定有标题栏，中间层容器没有",
                "2",
                "两层区分：① 顶层容器——JFrame、JDialog、JApplet，不继承 JComponent，只能作为界面程序的最顶层容器来包含其他组件。② 中间层容器——JPanel、JScrollPane 等，继承 JComponent，本身也是组件，可以（也必须）包含在其他容器中。特点：顶层是「重量级」——由操作系统绘制标题栏/边框；中间层是「轻量级」——纯 Java 绘制。",
                "",
                "",
                "",
            ],
            ["ch9", "container", "top-vs-intermediate", "choice"],
        ),
        # ═══ C04 · 布局管理器 · 单选 ═══
        note(
            model,
            [
                "C04",
                "choice",
                "以下布局管理器会让组件从左到右排列、一行放不下就自动换到下一行？",
                "BorderLayout——分东/南/西/北/中五个方位||GridLayout——等大小网格||FlowLayout——流式排列，自动换行||BoxLayout——水平或垂直排列",
                "3",
                "五种布局：① FlowLayout——从左到右，自动换行。② BorderLayout——东/南/西/北/中五方位（JFrame 默认）。③ GridLayout——等大小的二维网格。④ BoxLayout——水平或垂直线性排列，不换行。⑤ GridBagLayout——可放置不同大小组件的最灵活网格。不使用布局管理器需手动设定每个组件坐标和大小——不推荐（窗口大小变化时组件位置不变）。",
                "",
                "",
                "",
            ],
            ["ch9", "layout", "flowlayout", "choice"],
        ),

        # ═══════════ 窗体与绘制 ═══════════
        # ═══ C05 · JFrame 生命周期 · 单选 ═══
        note(
            model,
            [
                "C05",
                "choice",
                "为什么所有 Swing 组件必须在 EventQueue.invokeLater() 中创建？这三个方法各有什么作用？",
                "这是 Java 的历史遗留问题，没有实际意义||Swing 是单线程模型——所有 UI 操作必须在事件分派线程（EDT）中串行执行，避免并发问题。setDefaultCloseOperation 设定关闭行为，setVisible(true) 让窗体显示||为了让代码运行更快||为了兼容 AWT",
                "2",
                "三个关键点：① EventQueue.invokeLater(()->{...})——将 UI 创建代码放入事件分派线程（EDT），Swing 所有组件必须由 EDT 配置。② setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)——关闭窗口时退出进程（不设则关窗口了进程还在）。③ setVisible(true)——JFrame 初始不可见，添加完所有组件后才让它显示。pack() 根据子组件首选大小自动调整窗口尺寸。",
                "",
                "",
                "",
            ],
            ["ch9", "jframe", "lifecycle", "choice"],
        ),
        # ═══ C06 · paintComponent · 单选 ═══
        note(
            model,
            [
                "C06",
                "choice",
                "在 Swing 中如何实现自定义绘制？paintComponent 方法的参数 Graphics g 是什么？为什么需要强转为 Graphics2D？",
                "实现 Runnable 接口的 run 方法||覆盖 JComponent 的 paintComponent(Graphics g) 方法——g 是绘图的「画笔」对象，强转为 Graphics2D 获得更强大的 2D 绘图能力（浮点坐标、填充、颜色管理等）||实现 Drawable 接口||直接调用 JFrame 的 draw 方法",
                "2",
                "步骤：① 定义一个扩展 JComponent 的类；② 覆盖 paintComponent(Graphics g)；③ 在方法内通过 g 进行所有绘制操作。Graphics = 基本绘图（drawString、drawLine），Graphics2D = 增强版（draw/fill Rectangle2D/Ellipse2D，setPaint 设置颜色）。Java 中所有绘制都必须通过 Graphics 对象，不像 C 直接写显存。getPreferredSize() 返回首选尺寸——供 pack() 使用。",
                "",
                "",
                "",
            ],
            ["ch9", "paintcomponent", "graphics2d", "choice"],
        ),
        # ═══ C07 · 颜色 · 单选 ═══
        note(
            model,
            [
                "C07",
                "choice",
                "Graphics2D 中 setPaint 和 fill 的区别是什么？如何创建自定义颜色？",
                "没有区别——都可以设置颜色||setPaint(Color) 设置后续绘制操作的颜色（画笔颜色），fill(Shape) 用当前颜色填充封闭图形的内部——只影响 fill 不影响 draw。自定义颜色：new Color(r, g, b)，每分量 0~255 的整数||setPaint 用于文字，fill 用于图形||setPaint 是画笔，fill 是橡皮",
                "2",
                "setPaint(Color c) = 设置「画笔」颜色，影响之后所有 draw 和 fill 操作。fill(Shape) = 填充封闭图形内部（如用红色填充矩形）。draw(Shape) = 只画轮廓不填充。颜色体系：① 预定义常量——Color.RED/BLUE/GREEN 等 13 种；② 自定义 RGB——new Color(147, 112, 219)，每分量 0~255。颜色设置是立即生效的——想用多种颜色，就反复 setPaint → draw/fill → setPaint → draw/fill。",
                "",
                "",
                "",
            ],
            ["ch9", "color", "setpaint", "choice"],
        ),
        # ═══ C08 · copyArea · 单选 ═══
        note(
            model,
            [
                "C08",
                "choice",
                "为什么在平铺图像时使用 copyArea() 比循环 drawImage() 更高效？",
                "copyArea 更精确||copyArea 直接在显存中复制像素块（位块传输），不经过 Java 绘制管线——避免了多次 drawImage 的逐次调用开销||drawImage 不支持平铺||copyArea 自动调整图像大小",
                "2",
                "copyArea(x, y, w, h, dx, dy) = 将矩形区域 (x,y,w,h) 的像素块复制到目标位置 (dx, dy)。这是显存级别的位块传输操作，不经过 Java 的 Graphics 绘制管线，效率远高于循环中反复调用 drawImage。平铺模式：先在左上角画一次原图 → 用 copyArea 将整块复制到同行/同列 → 行列同时无重叠时直接复制。关键是避免每次 re-draw 都走完整的 decode→transform→blit 管线。",
                "",
                "",
                "",
            ],
            ["ch9", "copyarea", "tiling", "choice"],
        ),

        # ═══════════ 事件机制 ═══════════
        # ═══ C09 · 三类对象 · 单选 ═══
        note(
            model,
            [
                "C09",
                "choice",
                "Swing 事件处理机制涉及哪三类对象？一个事件源可以注册几个监听器？",
                "生产者/消费者/代理——只能注册一个监听器||事件（Event，如 ActionEvent）、事件源（Event Source，如 JButton）、事件监听器（Listener，实现 ActionListener 接口）——一个事件源可以注册多个监听器||发送方/接收方/路由器——最多三个监听器||产生器/处理器/过滤器——只能注册一个",
                "2",
                "三类对象：① 事件（Event）——携带事件信息（来源、类型等）的对象，如 ActionEvent；② 事件源（Event Source）——产生事件的组件（JButton、JTextField 等），负责创建事件对象并发送给注册的监听器；③ 事件监听器（Listener）——实现特定监听器接口的类实例，接收并响应事件。一个事件源可以有多个监听器——如按钮同时有声音反馈和逻辑处理两个监听器。",
                "",
                "",
                "",
            ],
            ["ch9", "event", "three-objects", "choice"],
        ),
        # ═══ C10 · 事件流程 · 单选 ═══
        note(
            model,
            [
                "C10",
                "choice",
                "从用户点击按钮到程序执行响应代码，完整的事件流程是怎样的？",
                "按钮直接调用响应方法||事件源（JButton）创建 ActionEvent → 遍历已注册的监听器 → 调用每个监听器的 actionPerformed(ActionEvent) 方法 → 监听器执行响应代码||系统捕获点击 → 通知 JVM → JVM 随机选择一个监听器||按钮发送 HTTP 请求到服务器",
                "2",
                "完整流程：① 用户点击按钮 → ② JButton 创建 ActionEvent 对象（封装事件源引用和动作命令）→ ③ JButton 遍历所有已通过 addActionListener 注册的监听器 → ④ 对每个监听器调用 listener.actionPerformed(event) → ⑤ 监听器内部通过 event.getSource() 获取事件源、event.getActionCommand() 获取命令、执行业务逻辑。监听器接口是函数式接口（只有一个方法）——可完美用 Lambda 简化。",
                "",
                "",
                "",
            ],
            ["ch9", "event", "flow", "choice"],
        ),
        # ═══ C11 · Lambda 监听器 · 单选 ═══
        note(
            model,
            [
                "C11",
                "choice",
                "btn.addActionListener(event -> System.out.println(\"clicked\")); 这行 Lambda 等价于什么？Lambda 在这里替代了什么？",
                "等价于 btn.onClick = ...||等价于传统的匿名内部类 new ActionListener() { public void actionPerformed(ActionEvent event) { System.out.println(\"clicked\"); } }——Lambda 替代了匿名内部类的样板代码||等价于 if(btn.clicked) ...||等价于 btn.setAction(...)",
                "2",
                "Lambda 表达式本质是匿名函数——用简洁语法定义一个函数而无需显式命名。Java 8 引入，主要用于替换单方法接口的匿名内部类。语法：(参数) -> { 函数体 }。适用条件：接口只有一个抽象方法（函数式接口，如 ActionListener、Runnable）。优势：代码从 5 行样板减少到 1 行。Lambda 可以捕获所在作用域的变量（effectively final）。",
                "",
                "",
                "",
            ],
            ["ch9", "lambda", "listener", "choice"],
        ),

        # ═══════════ Swing 基本组件 ═══════════
        # ═══ C12 · 文本组件 · 单选 ═══
        note(
            model,
            [
                "C12",
                "choice",
                "JTextField、JTextArea、JPasswordField 三者的区别是什么？为什么 getPassword() 返回 char[] 而不是 String？",
                "没有区别——都可以输入文本||JTextField=单行文本，JTextArea=多行文本（回车换行，每行以 \\n 结尾），JPasswordField=单行且字符被回显符号（如*）遮挡。getPassword() 返回 char[] 而非 String 是因为 char[] 可以手动清零——String 不可变且留在字符串池中，可能有安全隐患||JTextField 是密码框，JPasswordField 是普通框||JTextArea 只能输入数字",
                "2",
                "三者均继承自 JTextComponent（抽象类）。JTextField：单行文本，getText()/setText()。JTextArea：多行文本，需包裹在 JScrollPane 中才有滚动条——JTextArea 自己不带滚动条。JPasswordField：单行 + 回显遮挡，getPassword() 返回 char[]（安全——用后可以 Arrays.fill(password, '0') 清零），不用 String（不可变，GC 前一直留在内存中可能被 dump 读取）。",
                "",
                "",
                "",
            ],
            ["ch9", "text", "components", "choice"],
        ),
        # ═══ C13 · 选择组件 · 单选 ═══
        note(
            model,
            [
                "C13",
                "choice",
                "JRadioButton 必须配合什么类使用才能实现互斥选择？ButtonGroup 的作用是什么？",
                "配合 JCheckBox 使用||必须配合 ButtonGroup——将多个 JRadioButton 加入同一个 ButtonGroup 后，组内自动互斥（只能选一个）。ButtonGroup 不是组件，没有视觉表现，只负责管理选择状态||配合 JComboBox||配合 ArrayList",
                "2",
                "ButtonGroup 用法：① 创建 ButtonGroup group = new ButtonGroup()；② group.add(radio1); group.add(radio2)；③ 通过 group.getSelection().getActionCommand() 获取被选中的按钮。注意：ButtonGroup 不是可视组件——按钮仍需逐个添加到 JPanel 中。JCheckBox 不需要 ButtonGroup——每个独立开关，isSelected() 获取状态。JComboBox 是下拉列表——addItem()/getSelectedItem()/removeItemAt()。",
                "",
                "",
                "",
            ],
            ["ch9", "radiobutton", "buttongroup", "choice"],
        ),
        # ═══ C14 · 菜单 · 单选 ═══
        note(
            model,
            [
                "C14",
                "choice",
                "Swing 菜单的三层嵌套结构是什么？addSeparator() 的作用是什么？",
                "JFrame→JPanel→JButton||JMenuBar（菜单栏）→ JMenu（菜单）→ JMenuItem（菜单项）。addSeparator() 在菜单项之间插入分隔线||JDialog→JMenu→JLabel||JComboBox→JList→JCheckBox",
                "2",
                "菜单结构：① JMenuBar——菜单栏，通过 frame.setJMenuBar(menuBar) 添加到窗体顶部；② JMenu——菜单，如「File」「Edit」，用 menuBar.add(fileMenu) 加入菜单栏；③ JMenuItem/JCheckBoxMenuItem——具体菜单项，用 menu.add(item) 加入菜单。addSeparator() 在菜单项之间插入分隔线。子菜单：一个 JMenu 对象也可以 add 另一个 JMenu——形成「Edit → Options → Read-only」的嵌套。",
                "",
                "",
                "",
            ],
            ["ch9", "menu", "structure", "choice"],
        ),

        # ═══════════ MVC 模式 ═══════════
        # ═══ C15 · MVC 三角色 · 单选 ═══
        note(
            model,
            [
                "C15",
                "choice",
                "MVC 模式中 Model、View、Controller 各自负责什么？三者之间的交互规则是什么？",
                "Model 负责显示，View 负责存储，Controller 负责网络||Model 存储内容和业务逻辑（不可见，不依赖 UI）、View 显示内容（可多个 View 对应一个 Model）、Controller 处理用户输入并决定转化为 Model 修改还是 View 操作——Model 不直接知道 View 的存在，通过观察者模式通知 View 更新||三者完全独立，互不知晓||Model=数据库，View=HTML，Controller=Servlet",
                "2",
                "三角色：① Model——存储完整内容，提供查找/修改方法。完全不可见，不依赖任何 UI 类。② View——显示模型内容。一个 Model 可有多个 View（如飞机大战中 GamePanel 和 ScorePanel 都观察同一个 GameState）。Model 更新时通知所有 View 刷新。③ Controller——处理用户输入事件（键鼠点击）。决定事件应当转化为 Model 修改（如空格→hero.fire()）还是仅 View 操作（如方向键→滚动窗口，模型不变）。交互规则：Model 通过事件机制通知 View，自己不持有 View 引用。",
                "",
                "",
                "",
            ],
            ["ch9", "mvc", "roles", "choice"],
        ),
        # ═══ C16 · MVC 示例 · 单选 ═══
        note(
            model,
            [
                "C16",
                "choice",
                "在飞机大战中，用户按下空格键让英雄射击，MVC 的交互流程是怎样的？",
                "View 直接修改 Model||Controller（键盘监听器）收到空格事件 → 调用 Model.hero.fire() 修改数据 → Model 通知所有 View 刷新 → View 调用 repaint() 重绘画面||Model 直接调用 View 的 repaint||View 自己检测到按键并修改自己",
                "2",
                "MVC 交互流程：① 用户按下空格 → 键盘事件发给 Controller（KeyListener）；② Controller 判断「空格 = 射击命令」→ 调用 model.hero.fire()（修改 Model——创建新 Bullet 加入列表）；③ Model 状态改变 → 通知所有注册的 View（GamePanel、ScorePanel）；④ 每个 View 调用 repaint() 重新执行 paintComponent，从 Model 读取最新数据并绘制。对比方向键——如果只是滚屏，Controller 直接通知 View 调整偏移量，不修改 Model。这是 MVC 的灵活性——Controller 选择改 Model 还是改 View。",
                "",
                "",
                "",
            ],
            ["ch9", "mvc", "example", "choice"],
        ),

        # ═══ F01 · 组件层级 · 填空 ═══
        note(
            model,
            [
                "F01",
                "fill",
                "Swing 组件继承层级：{{c1::Component}} → {{c2::Container}} → {{c3::JComponent}}（轻量级基类）。顶层容器（{{c4::JFrame}}/JDialog/JApplet）不继承 JComponent。中间层容器（{{c5::JPanel}}/JScrollPane）继承 JComponent——本身是组件也是容器。Swing 构建在{{c6::AWT}}之上，AWT 提供底层窗口和事件机制。",
                "",
                "Component||Container||JComponent||JFrame||JPanel||AWT",
                "所有容器都是组件（可放入其他容器），但不是所有组件都是容器（JButton 不是容器）。JPanel 既是组件又是容器——可放入 JFrame 也可容纳按钮。",
                "",
                "",
                "",
            ],
            ["ch9", "swing", "hierarchy", "fill", "multi-cloze"],
        ),
        # ═══ F02 · 事件机制 · 填空 ═══
        note(
            model,
            [
                "F02",
                "fill",
                "Swing 事件三类对象：① {{c1::事件}}(Event)——携带事件信息的对象（如 ActionEvent）；② {{c2::事件源}}(Event Source)——产生事件的组件（如 JButton）；③ {{c3::事件监听器}}(Listener)——实现特定接口的对象。点击按钮的流程：JButton 创建{{c4::ActionEvent}}→ 遍历{{c5::注册的监听器}}→ 调用{{c6::actionPerformed(ActionEvent)}}方法。注册语法：button.{{c7::addActionListener}}(listener)。",
                "",
                "事件||事件源||事件监听器||ActionEvent||注册的监听器||actionPerformed(ActionEvent)||addActionListener",
                "监听器接口是函数式接口（单方法），可用 Lambda 简化：button.addActionListener(e -> { ... })。一个事件源可注册多个监听器。Lambda 本质是匿名内部类的语法糖——要求接口只有一个抽象方法。",
                "",
                "",
                "",
            ],
            ["ch9", "event", "fill", "multi-cloze"],
        ),
        # ═══ F03 · MVC 模式 · 填空 ═══
        note(
            model,
            [
                "F03",
                "fill",
                "MVC 三角色：① {{c1::Model}}——存储完整内容，提供查找/修改方法，不可见，不依赖 UI；② {{c2::View}}——显示内容，一个 Model 可有多个 View，Model 更新时通知 View 刷新；③ {{c3::Controller}}——处理用户输入，决定事件转化为{{c4::Model 修改}}还是{{c5::View 操作}}。Model 不直接持有 View 引用——通过{{c6::事件/观察者机制}}通知 View。",
                "",
                "Model||View||Controller||Model 修改||View 操作||事件/观察者机制",
                "MVC 体现：SRP——存储/显示/控制三职责分离；OCP——换 View（如从 Swing 换 JavaFX）不改 Model 和 Controller；DIP——Controller 依赖 Model 接口而非具体 Model 实现。Swing 组件如 JButton 内部就是 MVC 架构——Model 存按下状态，View 画按钮外观，Controller 处理鼠标事件。",
                "",
                "",
                "",
            ],
            ["ch9", "mvc", "fill", "multi-cloze"],
        ),

        # ═══ Q01 · 设置界面完整代码 · 问答 ═══
        note(
            model,
            [
                "Q01",
                "qa",
                "写出飞机大战「游戏设置」窗口的完整代码。要求：① JFrame 含 BorderLayout；② JPanel 用 FlowLayout 放 3 个 JRadioButton（简单/中等/困难）+ ButtonGroup 互斥；③ 底部 JTextField 输入玩家名；④ 复选框「开启音效」；⑤ OK 按钮点击后在控制台打印所有设置——用 Lambda 写监听器。",
                "",
                "Frame frame = new JFrame(\"飞机大战 - 设置\");\nframe.setLayout(new BorderLayout());\n\n// 难度选择（JPanel + 单选按钮）\nJPanel diffPanel = new JPanel(new FlowLayout());\nJRadioButton easy = new JRadioButton(\"简单\");\nJRadioButton normal = new JRadioButton(\"中等\"); normal.setSelected(true);\nJRadioButton hard = new JRadioButton(\"困难\");\nButtonGroup group = new ButtonGroup();\ngroup.add(easy); group.add(normal); group.add(hard);\ndiffPanel.add(easy); diffPanel.add(normal); diffPanel.add(hard);\nframe.add(diffPanel, BorderLayout.NORTH);\n\n// 玩家名\nJTextField nameField = new JTextField(20);\nframe.add(nameField, BorderLayout.CENTER);\n\n// 音效复选框 + OK 按钮\nJPanel bottom = new JPanel();\nJCheckBox soundCheck = new JCheckBox(\"开启音效\", true);\nJButton okBtn = new JButton(\"OK\");\nbottom.add(soundCheck); bottom.add(okBtn);\nframe.add(bottom, BorderLayout.SOUTH);\n\n// Lambda 监听器\nokBtn.addActionListener(e -> {\n    System.out.println(\"玩家: \" + nameField.getText());\n    System.out.println(\"音效: \" + soundCheck.isSelected());\n    System.out.println(\"难度: \" + group.getSelection().getActionCommand());\n});\n\nframe.pack();\nframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);\nframe.setVisible(true);",
                "考察点：① BorderLayout 分南北——北放难度面板，中放输入框，南放按钮；② ButtonGroup 不是组件——单选按钮需单独加入 diffPanel，ButtonGroup 只管理互斥逻辑；③ JPasswordField 可用 char[] 获取密码（安全），此处用 JTextField 即可；④ Lambda 替代匿名内部类——必须函数式接口。",
                "",
                "",
                "",
            ],
            ["ch9", "swing", "example", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 第九章 Swing图形用户界面", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
