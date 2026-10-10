from __future__ import annotations

import genanki

from generate_apkg import ROOT, note, write_deck

DECK_ID = 2059400518
OUTPUT = ROOT / "anki-第八章-流与输入输出.apkg"


def build_notes(model: genanki.Model) -> list[genanki.Note]:
    return [
        # ═══════════ 流的概念 ═══════════
        # ═══ C01 · 流的定义与分类 · 单选 ═══
        note(
            model,
            [
                "C01",
                "choice",
                "Java 中的流可以从哪三个维度进行分类？",
                "速度、大小、颜色||方向（输入/输出）、数据单位（字节/字符）、功能（节点流/处理流）||同步/异步、阻塞/非阻塞、缓冲/非缓冲||文件流、网络流、内存流",
                "2",
                "流三维分类：① 方向——输入流（数据进程序）vs 输出流（数据出程序），以程序自身为参照；② 数据单位——字节流（Stream，8bit，适合所有类型数据）vs 字符流（Reader/Writer，16bit，仅纯文本）；③ 功能——节点流（直接连数据源）vs 处理流（包装另一个流，如 BufferedReader 包装 InputStreamReader）。三个维度正交——一个流同时属于每个维度的某一类。",
                "",
                "",
                "",
            ],
            ["ch8", "stream", "classification", "choice"],
        ),
        # ═══ C02 · 节点流 vs 处理流 · 单选 ═══
        note(
            model,
            [
                "C02",
                "choice",
                "节点流和处理流的核心区别是什么？BufferedReader 属于哪一类？",
                "节点流比处理流快||节点流直接与数据源相连（如 FileInputStream 连文件），处理流包装另一个流提供额外功能（如 BufferedReader 包装 InputStreamReader 提供缓冲和 readLine）——BufferedReader 是处理流||处理流替代节点流——用了处理流就不需要节点流||节点流只能读，处理流只能写",
                "2",
                "节点流：直接连接数据源/目的地，如 FileInputStream（连文件）、System.in（连键盘）。处理流：包装一个已有的流对象，添加缓冲、类型转换、压缩等功能——如 BufferedReader（加缓冲+readLine）、InputStreamReader（字节→字符转换）、ObjectInputStream（二进制→对象）。处理流不能独立存在——必须基于一个节点流。类比 C：fopen 返回的 FILE* 是节点流；Java 把缓冲、字符转换等功能拆成独立的处理流类，可以灵活组合。",
                "",
                "",
                "",
            ],
            ["ch8", "stream", "node-vs-processing", "choice"],
        ),
        # ═══════════ 系统流与输入 ═══════════
        # ═══ C03 · 系统流 · 单选 ═══
        note(
            model,
            [
                "C03",
                "choice",
                "Java 中 System.in、System.out、System.err 分别是什么类型的对象？默认连到什么设备？",
                "都是 InputStream 类型，默认连键盘||System.in 是 InputStream（默认键盘），System.out 和 System.err 是 PrintStream（默认控制台）||都是 File 类型，默认连文件系统||System.in 是 Reader，System.out 是 Writer",
                "2",
                "System.in → InputStream（字节输入流），默认设备 = 键盘。System.out → PrintStream（字节输出流），默认设备 = 控制台。System.err → PrintStream（字节输出流），默认设备 = 控制台——用于输出错误信息，与 out 独立（可分别重定向）。out 常用方法：print()（不换行）、println()（换行）、write()（写字节，少用）。",
                "",
                "",
                "",
            ],
            ["ch8", "system", "streams", "choice"],
        ),
        # ═══ C04 · BufferedReader 包装链 · 单选 ═══
        note(
            model,
            [
                "C04",
                "choice",
                "从键盘读取一行文本，需要使用 `BufferedReader br = new BufferedReader(new InputStreamReader(System.in));` ——这行代码涉及哪几个流？每个的作用？",
                "只有一个流——BufferedReader||三个流：System.in（字节节点流，连键盘）→ InputStreamReader（处理流，字节→字符转换）→ BufferedReader（处理流，加缓冲 + readLine() 方法）||两个流：System.in + BufferedReader，InputStreamReader 是可选的||不需要这些——直接用 Scanner 就行",
                "2",
                "包装链：System.in 是 InputStream（原始字节），直接用它只能读 int 类型的字节值。InputStreamReader 将字节流桥接为字符流（Reader），可以指定字符编码。BufferedReader 再包装一层，提供缓冲（减少系统调用次数）和 readLine() 方法（一次读一行）。这就是「处理流包装节点流」的典型模式——装饰器模式（Decorator Pattern）在 Java I/O 中的体现。",
                "",
                "",
                "",
            ],
            ["ch8", "bufferedreader", "chain", "choice"],
        ),

        # ═══════════ 流继承框架 ═══════════
        # ═══ C05 · 四大家族 · 单选 ═══
        note(
            model,
            [
                "C05",
                "choice",
                "Java 所有 I/O 流类都继承自哪四个抽象基类？类名命名规则是什么？",
                "FileReader/FileWriter/FileInputStream/FileOutputStream||InputStream/OutputStream（字节流）和 Reader/Writer（字符流）——类名以 Stream 结尾的是字节流，以 Reader/Writer 结尾的是字符流||NodeStream/FilterStream/DataStream/ObjectStream||Input/Output/Read/Write",
                "2",
                "四大家族 = InputStream（字节输入）、OutputStream（字节输出）、Reader（字符输入）、Writer（字符输出）。命名规则：Stream 结尾 → 字节流（FileInputStream、ObjectOutputStream）；Reader/Writer 结尾 → 字符流（FileReader、BufferedReader、PrintWriter）。所有流都实现了 Closeable 接口——都有 close() 方法，用完后必须关闭释放资源。字节流与字符流可以桥接：InputStreamReader(InputStream) 和 OutputStreamWriter(OutputStream)。",
                "",
                "",
                "",
            ],
            ["ch8", "stream", "hierarchy", "choice"],
        ),
        # ═══ C06 · 典型子类 · 多选 ═══
        note(
            model,
            [
                "C06",
                "choice",
                "以下哪些是 InputStream 的典型子类或包装类？（多选）",
                "FileInputStream（节点流，读文件）||BufferedInputStream（处理流，加缓冲）||DataInputStream（处理流，读基本 Java 类型）||ObjectInputStream（处理流，反序列化对象）||FileReader（字符流，不属于 InputStream 体系）",
                "1||2||3||4",
                "InputStream 家族：节点流——FileInputStream；处理流——BufferedInputStream、DataInputStream（以二进制读 int/double 等）、ObjectInputStream（反序列化）、ZipInputStream（读 ZIP）。FileReader 继承自 Reader 而非 InputStream——它属于字符流家族。误把 FileReader 归入 InputStream 体系是常见错误。",
                "",
                "",
                "",
            ],
            ["ch8", "inputstream", "subclasses", "choice", "multi"],
        ),

        # ═══════════ 文件操作 ═══════════
        # ═══ C07 · 传统 vs Files · 单选 ═══
        note(
            model,
            [
                "C07",
                "choice",
                "Java 中操作文件的两套 API 分别是什么？各自适用什么场景？",
                "Socket 和 HTTP——分别用于本地和远程文件||传统流（FileInputStream/FileOutputStream + OutputStreamWriter，适合大文件逐块读写）和 Files 工具类（Files.readString/writeString/copy/move/delete，适合小文件整文件操作）||ArrayList 和 LinkedList||File 对象和 Path 对象——没有区别",
                "2",
                "两套 API：① 传统流——FileInputStream/FileOutputStream 配合 InputStreamReader/OutputStreamWriter，逐字符或逐块读写，适合大文件；需手动 close()。② Files 工具类（JDK 7+ NIO.2）——Files.readString(path)、Files.readAllLines(path)、Files.writeString(path, str)、Files.copy/move/delete/createDirectory。便捷但受内存限制（整文件读入内存），不适合大文件。Path 类用 Paths.get(...) 创建。",
                "",
                "",
                "",
            ],
            ["ch8", "file", "api-comparison", "choice"],
        ),
        # ═══ C08 · Files 操作 · 单选 ═══
        note(
            model,
            [
                "C08",
                "choice",
                "Files.copy() 和 Files.move() 的区别是什么？如何覆盖已存在的目标文件？",
                "没有区别——两者都是复制||Files.copy 复制后原文件保留，Files.move 复制后删除原文件（相当于剪切）。覆盖已有目标用 StandardCopyOption.REPLACE_EXISTING||Files.copy 只复制目录，Files.move 只移动文件||Files.copy 是原子的，Files.move 不是",
                "2",
                "Files.copy(from, to) → 复制，原文件保留。Files.move(from, to) → 移动（复制 + 删除原文件），可用 ATOMIC_MOVE 选项使移动原子化——要么成功完成，要么源文件保持原位。覆盖已有目标：Files.copy(from, to, StandardCopyOption.REPLACE_EXISTING)；同时保留文件属性再加 COPY_ATTRIBUTES。删除：Files.delete(path) 不存在时抛异常；Files.deleteIfExists(path) 安全删除返回 boolean。路径：Paths.get(\"path/to/file\") 创建 Path 对象。",
                "",
                "",
                "",
            ],
            ["ch8", "files", "operations", "choice"],
        ),

        # ═══════════ 对象序列化 ═══════════
        # ═══ C09 · Serializable · 单选 ═══
        note(
            model,
            [
                "C09",
                "choice",
                "Serializable 接口是一个标记接口（Marker Interface），这意味着什么？它有什么方法需要实现？",
                "它有一个 serialize() 方法需要实现||它没有任何方法需要实现——只是给 JVM 一个标记：「这个类的对象可以被序列化」||它有三个方法需要实现||它必须和 Externalizable 一起使用",
                "2",
                "标记接口（Marker Interface）——接口中不声明任何方法，仅作为一种类型标记。Serializable 的作用：告诉 JVM「此类的对象可以通过 ObjectOutputStream 写入字节流，可以通过 ObjectInputStream 读回」。没有实现 Serializable 的类在调用 writeObject() 时会抛出 NotSerializableException。与 Externalizable 的区别：Externalizable 有 writeExternal/readExternal 两个方法，需要手动控制序列化细节。",
                "",
                "",
                "",
            ],
            ["ch8", "serializable", "marker-interface", "choice"],
        ),
        # ═══ C10 · 序列化步骤 · 单选 ═══
        note(
            model,
            [
                "C10",
                "choice",
                "对象序列化的完整步骤是什么？反序列化时返回的类型是什么？",
                "调用对象的 save() 方法 → 返回 String||序列化：new ObjectOutputStream(new FileOutputStream(...)) → oos.writeObject(obj)；反序列化：new ObjectInputStream(new FileInputStream(...)) → (目标类型) ois.readObject()，返回 Object，必须强转||序列化：Files.writeObject()；反序列化：Files.readObject()||序列化：obj.toString()；反序列化：Class.forName()",
                "2",
                "序列化步骤：① 类实现 Serializable；② 创建 ObjectOutputStream 包装 FileOutputStream；③ 调用 writeObject(obj)。反序列化步骤：① 创建 ObjectInputStream 包装 FileInputStream；② 调用 readObject() 返回 Object 类型，必须强转为目标类型。serialVersionUID 用于版本控制——类结构变化后需更新此值，否则旧数据反序列化失败。",
                "",
                "",
                "",
            ],
            ["ch8", "serialization", "steps", "choice"],
        ),
        # ═══ C11 · transient · 单选 ═══
        note(
            model,
            [
                "C11",
                "choice",
                "transient 关键字在序列化中的作用是什么？什么场景应该用它？",
                "transient 让字段序列化得更快||transient 修饰的字段不参与序列化——反序列化后该字段为默认值（0/false/null）。适用场景：密码、临时计算结果、可重新获取的数据（如缓存）||transient 让字段永久存储在文件中||transient 是 public 的替代",
                "2",
                "序列化时，所有非 static 非 transient 的字段都会被写入字节流。transient 字段被跳过——反序列化后恢复为默认值（引用类型=null，int=0，boolean=false）。典型场景：① 密码/密钥——不应持久化到文件中；② 临时缓存——反序列化后重新计算即可；③ 不可序列化的字段引用——如果某个字段的类没实现 Serializable，可将其声明为 transient 避免异常。static 字段也不序列化——它们属于类而非实例。",
                "",
                "",
                "",
            ],
            ["ch8", "transient", "serialization", "choice"],
        ),

        # ═══════════ DAO 模式 ═══════════
        # ═══ C12 · DAO 三角色 · 单选 ═══
        note(
            model,
            [
                "C12",
                "choice",
                "DAO（数据访问对象）模式的三个角色分别是什么？各自承担什么责任？",
                "Service / Repository / Entity||模型对象（Model，纯数据载体 POJO）、DAO 接口（定义标准 CRUD 操作）、DAO 实现类（具体实现——如文件存储、数据库存储）||Client / Server / Database||Factory / Product / Creator",
                "2",
                "三角色：① 模型对象（Model/Value Object）——纯数据载体，只有字段 + getter/setter（如 ScoreEntry）；② DAO 接口——定义标准 CRUD 操作签名（getAll/insert/update/delete），不暴露底层存储方式；③ DAO 实现类——具体实现（如用 ArrayList 模拟数据库、用文件序列化、用真实 JDBC 连数据库）。核心价值：隔离数据层——业务逻辑依赖 DAO 接口而非具体实现（体现 DIP）。换存储方式只需新建实现类，业务代码不动（体现 OCP）。",
                "",
                "",
                "",
            ],
            ["ch8", "dao", "roles", "choice"],
        ),
        # ═══ C13 · DAO 优点 · 单选 ═══
        note(
            model,
            [
                "C13",
                "choice",
                "DAO 模式的核心优点是什么？它体现了哪些设计原则？",
                "让代码运行更快||隔离数据层——业务逻辑与数据访问分离。体现 DIP（业务依赖 DAO 接口而非具体实现）+ OCP（换存储方式不改业务代码）+ SRP（DAO 只负责数据访问，业务只负责业务逻辑）||简化代码——少写几个类||让所有数据都存在内存中",
                "2",
                "DAO 核心价值：① 隔离数据层——数据访问错误在 DAO 层处理，不影响业务层；② 换存储方式只需建新 DAO 实现类（文件→数据库），业务代码不动（OCP）；③ 业务代码依赖 DAO 接口（DIP），不依赖具体存储技术；④ 分离关注点——DAO 管数据访问，Service 管业务逻辑（SRP）。缺点：增加代码量（多一层抽象），但对于实际项目该代价可忽略。",
                "",
                "",
                "",
            ],
            ["ch8", "dao", "advantages", "choice"],
        ),

        # ═══ F01 · 流分类 · 填空 ═══
        note(
            model,
            [
                "F01",
                "fill",
                "流的三维分类：① 按方向分为{{c1::输入流}}和{{c2::输出流}}，以程序为参照；② 按数据单位分为{{c3::字节流}}（8bit，Stream 结尾）和{{c4::字符流}}（16bit，Reader/Writer 结尾）；③ 按功能分为{{c5::节点流}}（直接连数据源）和{{c6::处理流}}（包装另一个流）。所有流都实现了{{c7::Closeable}}接口，有 close() 方法。",
                "",
                "输入流||输出流||字节流||字符流||节点流||处理流||Closeable",
                "字节流 ↔ 字符流桥接：InputStreamReader（字节→字符）、OutputStreamWriter（字符→字节）。处理流的典型：BufferedReader 包装 InputStreamReader 提供 readLine()。",
                "",
                "",
                "",
            ],
            ["ch8", "stream", "classification", "fill", "multi-cloze"],
        ),
        # ═══ F02 · 四大家族 · 填空 ═══
        note(
            model,
            [
                "F02",
                "fill",
                "Java I/O 四大家族抽象基类：字节输入{{c1::InputStream}}、字节输出{{c2::OutputStream}}、字符输入{{c3::Reader}}、字符输出{{c4::Writer}}。字节流子类示例：{{c5::FileInputStream}}（节点流）、{{c6::ObjectInputStream}}（处理流——反序列化）。字符流子类示例：{{c7::FileReader}}（节点流）、{{c8::BufferedReader}}（处理流——加缓冲+readLine）。",
                "",
                "InputStream||OutputStream||Reader||Writer||FileInputStream||ObjectInputStream||FileReader||BufferedReader",
                "命名规则：Stream 结尾 = 字节流，Reader/Writer 结尾 = 字符流。常见混淆：FileReader 是字符流（继承 Reader），不是字节流。InputStreamReader 是 Reader 的子类——它是字节→字符的桥接器。",
                "",
                "",
                "",
            ],
            ["ch8", "stream", "four-families", "fill", "multi-cloze"],
        ),
        # ═══ F03 · 序列化 · 填空 ═══
        note(
            model,
            [
                "F03",
                "fill",
                "对象序列化：类必须实现{{c1::Serializable}}接口（标记接口，无方法）。写出对象用{{c2::ObjectOutputStream}}的{{c3::writeObject(obj)}}方法，读回用{{c4::ObjectInputStream}}的{{c5::readObject()}}方法（返回 Object，需强转）。{{c6::transient}}修饰的字段不参与序列化；{{c7::static}}字段也不序列化（属于类而非实例）。版本控制用{{c8::serialVersionUID}}。",
                "",
                "Serializable||ObjectOutputStream||writeObject(obj)||ObjectInputStream||readObject()||transient||static||serialVersionUID",
                "反序列化不调用构造方法——对象直接从字节流重建。适用场景：持久化内存对象到硬盘（如游戏存档）、网络传输对象。transient 典型用途：密码字段（安全）、缓存字段（可重算）、不可序列化的引用。",
                "",
                "",
                "",
            ],
            ["ch8", "serialization", "fill", "multi-cloze"],
        ),
        # ═══ F04 · DAO 模式 · 填空 ═══
        note(
            model,
            [
                "F04",
                "fill",
                "DAO 模式三角色：① {{c1::模型对象}}(Model)——纯数据载体 POJO，只有字段+getter/setter；② {{c2::DAO 接口}}——定义标准 CRUD 操作，不暴露底层存储；③ {{c3::DAO 实现类}}——负责从具体数据源（文件/数据库/ArrayList）读写数据。体现的设计原则：{{c4::DIP}}（业务依赖接口而非实现）、{{c5::OCP}}（换存储方式不改业务代码）、{{c6::SRP}}（分离数据访问与业务逻辑）。",
                "",
                "模型对象||DAO 接口||DAO 实现类||DIP||OCP||SRP",
                "DAO 核心价值：隔离数据层——数据访问错误在 DAO 层处理不影响业务层。换存储方式只需新建 DAO 实现类（文件→数据库），GameService 一行不改。缺点：增加一层抽象，代码量略增。",
                "",
                "",
                "",
            ],
            ["ch8", "dao", "fill", "multi-cloze"],
        ),

        # ═══ Q01 · 传统流完整文件 I/O · 问答 ═══
        note(
            model,
            [
                "Q01",
                "qa",
                "写出用传统流方式读写一个文本文件（包含中英文）的完整代码，要求正确指定 UTF-8 编码，并正确处理流关闭。说明为什么要用 OutputStreamWriter 而不能直接用 FileOutputStream 写中文字符串。",
                "",
                "// 写文件\nFile f = new File(\"a.txt\");\nFileOutputStream fos = new FileOutputStream(f);\nOutputStreamWriter writer = new OutputStreamWriter(fos, \"UTF-8\");\nwriter.append(\"中文输入\");\nwriter.append(\"\\r\\n\");\nwriter.append(\"English\");\nwriter.close();  // 关闭写入流，同时 flush 缓冲区\nfos.close();      // 关闭输出流，释放系统资源\n\n// 读文件\nFileInputStream fis = new FileInputStream(f);\nInputStreamReader reader = new InputStreamReader(fis, \"UTF-8\");\nStringBuilder sb = new StringBuilder();\nwhile (reader.ready()) {\n    sb.append((char) reader.read());\n}\nreader.close();\nfis.close();\nSystem.out.println(sb.toString());",
                "为什么需要 OutputStreamWriter：FileOutputStream 是字节流——只能写出 byte[] 或单个 byte。中文字符在 UTF-8 下占 3 字节，在 UTF-16 下占 2 字节——它不是单个 byte。直接用 fos.write('中') 会截断高位只写低 8 位，产生乱码。OutputStreamWriter 作为处理流，将字符按指定编码（UTF-8）转换为正确的字节序列再通过底层的 FileOutputStream 写出——保证多字节字符的正确性。",
                "",
                "",
                "",
            ],
            ["ch8", "fileio", "traditional", "qa"],
        ),
        # ═══ Q02 · 序列化完整示例 · 问答 ═══
        note(
            model,
            [
                "Q02",
                "qa",
                "写出飞机大战排行榜的序列化存储完整代码。ScoreEntry 包含 name(String) 和 score(int)，要求：① 类实现 Serializable；② 用 transient 排除临时排序字段 rank；③ 序列化存储 ArrayList<ScoreEntry> 到文件；④ 反序列化读回。",
                "",
                "public class ScoreEntry implements Serializable {\n    private static final long serialVersionUID = 1L;\n    private String name;\n    private int score;\n    private transient int rank;  // 排名是展示时计算的，不需持久化\n    public ScoreEntry(String name, int score) { this.name = name; this.score = score; }\n    // getter/setter...\n}\n\n// 存储\npublic void saveScores(List<ScoreEntry> entries, String path) {\n    try (ObjectOutputStream oos = new ObjectOutputStream(\n            new FileOutputStream(path))) {\n        oos.writeObject(entries);\n    } catch (IOException e) { e.printStackTrace(); }\n}  // try-with-resources 自动 close\n\n// 读取\npublic List<ScoreEntry> loadScores(String path) {\n    try (ObjectInputStream ois = new ObjectInputStream(\n            new FileInputStream(path))) {\n        return (List<ScoreEntry>) ois.readObject();  // 强转\n    } catch (IOException | ClassNotFoundException e) { return new ArrayList<>(); }\n}",
                "考察点：① Serializable 标记接口——实现即可，无需任何方法；② transient rank——排名由 display() 时动态排序计算，存了也没用（下次加载分数变了排名就变了）；③ writeObject 可直接序列化整个 ArrayList——因为它也是 Serializable；④ readObject 返回 Object，必须强转为 List<ScoreEntry>（有泛型警告是正常的）；⑤ 用 try-with-resources 自动关闭流。",
                "",
                "",
                "",
            ],
            ["ch8", "serialization", "score", "qa"],
        ),
    ]


def main() -> None:
    write_deck(DECK_ID, "面向对象的软件构造 · 第八章 流与输入输出", OUTPUT, build_notes)


if __name__ == "__main__":
    main()
