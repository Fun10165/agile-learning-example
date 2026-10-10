---
name: guided-concept-learning
description: "Use when a user wants to learn, understand, or receive a rigorous explanation of a concept, mechanism, algorithm, or technical topic. Build understanding from the learner's relevant prior knowledge through a motivated main thread, precise definitions, operational detail, limitations, and a final coverage audit. Do not use this skill to create study cards. Also supports the agile-learning mode for multi-session topic builds（敏捷学习：git 管理的版本迭代、动机驱动、缺口清单作为下一版动机池）。"
---

# Guided Concept Learning

Use this skill to help someone genuinely understand a concept, not merely collect terminology.

## Scope

Use it for requests such as “teach me,” “help me understand,” “how does this work,” or “explain this concept.” Keep the result focused on learning and reasoning. Do not create Anki cards or introduce a card-authoring workflow; if the user asks for cards, use an appropriate card-authoring skill instead.

## 敏捷学习模式（git 管理的版本迭代）

当一个主题的目标从「一次讲清」变为「多次会话逐步建起来」时，用本模式：把它当一个迭代仓库来做。下面这套做法来自一个真实完成的实例（POSIX 权限系统的逐版迭代）。

本章节的规则使用 RFC 2119 关键词：**MUST** / **MUST NOT**（= **NEVER**）/ **SHOULD** / **SHOULD NOT**（= **AVOID**）/ **MAY**。违反 MUST 与 NEVER 的产出视为失败，MUST 撤回重做。

### 仓库

- 一个主题 MUST 对应一个 git 仓库。工作区 MUST 只放**当前版本的完整模型**：MUST NOT 保留旧版本、带版本号的小节、或「变更记录」——历史由 git 承载（`git log --oneline`、`git show <commit>`）。
- 文件 MAY 用普通 markdown；模型、动机、缺口清单 MAY 同放一个文件（例如 `README.md`），MUST 三者分区清楚。

### 起点版本（v0）：最原始的想法

v0 是迭代的起点，它 MUST 是这个问题「最小、最抽象、最幼稚」的一个想法：一个第一次遇到这个问题的人，只有主干路径可走。

- v0 MUST 只放最关键的机制，MUST 短——一个核心想法加上它解决什么，篇幅以几十行为宜；v0 MAY 完全没有边界条件，MAY 没有任何设计，「没用的东西」MUST NOT 出现。
- v0 MUST 从「这个问题最初为什么存在」出发，MUST NOT 从「现在的实现长什么样」出发。
- v0 MUST NOT 是「现有版本的片段选取」：NEVER 写成对任何现有实现的摘录、裁剪或对照。
- NEVER 把学习笔记对应到现有代码文件；笔记 MUST NOT 成为现有代码的导读。
- 为理解仓库而读现有实现 MAY：读取 MUST 带着一个明确的问题（「这个机制为什么存在、主干流程是什么」），读到能写清核心机制就 MUST 停；MUST NOT 继续下钻实现细节、异常分支与边界处理。
- 读取前 MUST 先写清「接下来输出的是什么」：是 v0——一个最原始的想法；MUST NOT 是完整设计，MUST NOT 是当前仓库版本的片段。停读后 MUST 立刻动笔，MUST NOT 以「再读一点更保险」为由继续读。
- 提交 v0 前 MUST 自检：它是否短到像「第一次遇到这个问题的人提出的想法」；任何一眼能看出是从现有实现里摘出来的内容，MUST 删除。
- 一个合格的 v0 例：posix 笔记的第一版——「三档身份 × 三种操作 + 为什么用位图」，一页以内。

### 每一版

- 每版 MUST 只引入**一个机制**（回答当前缺口所需的最小增量）；一次塞进两个以上机制的版本 MUST 撤回重做。
- 每版 MAY 粗糙、MAY 边界不明确；MUST 有动机，MUST 能承接下一版。
- **模型 MUST 完整**：每版的模型 MUST 包含此前已引入的全部机制；旧内容 MUST 保留，MUST 按新的设计适配、重新表述，与新增量成为一个整体（术语一致、交叉引用一致）。两种失败形态 MUST NOT 出现：
  - 在旧模型后面直接追加新内容（堆叠；未成为整体）；
  - 删掉旧内容、只留本版增量（残缺，机制凭空消失）。
- 动机 MAY 叠加（按引入顺序一条一条累积）。
- 动机 SHOULD 来自「上一版解释不了的观察」（反例驱动优先于推理驱动）；新机制的动机 MUST 写成新段落。
- 每版的结构 MUST 为：动机 → 模型 → 缺口清单（单次讲解的结构见本文档其他章节）。
- 每版 MUST 以实际动作推进：读完即写、写完即提交；MUST NOT 以「接下来将要做 X」结束一轮而没有实际调用。

### 缺口清单（下一版的动机池）

- 每版 MUST 在末尾显式列出「故意留下的不明确处」。下一版 MUST 从清单里挑一个缺口，引入回答它所需的最小机制。
- 每个缺口 MUST 标注类型，类型决定「解决它要做什么」：
  - **内在矛盾**：现有规则产生的行为与需求冲突（解决它要调和规则，或补一个补偿机制）；
  - **未 spec 清楚**：机制已存在或已规定，但模型还没覆盖它（解决它是补描述）；
  - **扩展需求**：模型表达不了的、被需要的能力（解决它是加结构）。
- 缺口被回答后 MUST 从清单移除；新暴露的问题 MUST 加入。清单是活的路线图。

### 提交约定

- `v0: <动机> → <机制>`（起点版本）与 `vN: <动机> → <机制>`（后续版本）—— 一版模型；
- `vN 反思: ...` —— 在版本之上追加反思（通常就是缺口清单的更新）；
- `vN 澄清: ...` / `vN 修正: ...` —— 表述上的打磨与纠错。
- 提交信息 MUST 采用「动机 → 机制」的形式；只写「改了什么」的提交信息 MUST 重写。

### 实践中总结的写作纪律

- MUST 点名具体例子（真实的程序、路径、数字）：「某个 setuid 程序」不如写成 `/usr/bin/passwd` 及其 `ls -l` 形态与 `(real, effective, saved) = (1000, 0, 0)`。
- 运算描述 MUST 精确，MUST 选用核得住的数学词（`请求值 & ~umask` 是取差集）。
- 写进模型前 SHOULD 对照原始来源核对（标准原文、手册页）；发现说法出错，MUST 改文件，MUST 把承载它的历史一并修正。

### 示例

本 skill 自带一个完整的实例：`examples/posix-perms-notes/`（POSIX 权限系统的逐版笔记）。它保留完整 git 历史——`git log --oneline` 看迭代轨迹，`git show <hash>` 逐个看每版的 diff；工作区里的 `README.md` 是当前版本的完整模型。

## Language and Presentation

Use the learner's preferred language, inferring it from the conversation and source material unless the learner explicitly overrides it. When the learner's language is Chinese, prefer concise, fluent Chinese for faster reading and avoid unnecessary English headings or boilerplate; retain indispensable technical terms, symbols, code, and canonical names. Keep formatting readable without excessive line breaks, especially when the material may later be reviewed on mobile. Compact presentation must never remove strict definitions, equations, traces, limitations, alternatives, or the mandatory coverage audit.

## Teaching Workflow

### 1. Determine the relevant knowledge range first

Before explaining, identify only the learner knowledge that affects this topic:

- what they are trying to understand or accomplish
- which prerequisites they already know
- which notation, terminology, and implementation details they can use comfortably
- whether they need intuition, mathematical precision, implementation ability, or all three

Use the conversation and supplied material first. Ask a few targeted diagnostic questions when the range is genuinely unclear; do not conduct a broad background interview. If a useful explanation can begin from available evidence, state the assumed starting point and proceed, allowing the learner to correct it.

### 2. Establish motivation and a main thread

Start from the problem that makes the concept necessary. Prefer one concrete example whose complete journey can carry the explanation from input to result. Return to that same example as each mechanism is introduced.

Do not substitute a glossary-shaped list of definitions for a causal explanation. Definitions support the main thread; they are not the main thread by themselves.

### 3. Move from a rough solution to a precise one

Guide the learner through this progression:

1. formulate an intuitive first attempt
2. show exactly where it is ambiguous, inefficient, or incorrect
3. introduce the minimum new mechanism needed to repair it
4. make the result precise enough to calculate, predict, or implement
5. walk the main example through the precise mechanism end to end

The final account should expose inputs, outputs, state, decision rules, and update steps where applicable. Provide pseudocode, equations, invariants, or a worked trace when they materially make the solution implementable.

### 4. Surface important limitations early

For a complex topic, state decisive assumptions and limitations before the learner builds reasoning on a false model. Explain, as comprehensively as useful:

- assumptions the method depends on
- the situations in which it applies
- boundaries beyond which its model no longer fits
- common and consequential failure cases
- alternative methods and when their assumptions make them a better fit

Do not bury a limitation that changes the interpretation of the whole explanation in an ending footnote. Less central edge cases may be introduced when they become relevant to the main thread.

### 5. Teach vividly without decorative analogies

Use concrete states, traces, diagrams, counterexamples, and visible transformations to make the mechanism vivid. An analogy is optional and must clarify a specific structural relationship. Never let an analogy replace the real definition or mechanism, and remove it if the mapping breaks quickly or adds no predictive power.

## Strict-Definition Contract

Maintain an internal coverage ledger while writing. Add every concept, term, symbol, abbreviation, operation, or method that the learner may not already know and that the explanation relies on.

For each ledger item:

1. give a clear, non-metaphorical definition at first use or immediately nearby
2. state what it operates on and what result it produces
3. explain its operational mechanism or decision rule
4. provide mathematical detail where applicable, defining every symbol, unit, index, and convention used
5. connect it to the main example with an actual step, not merely another analogy
6. distinguish it from easily confused neighboring concepts when that distinction matters

Do not define an unfamiliar concept only through another undefined concept. Order prerequisites before dependents, or briefly define a prerequisite before using it. Familiarity with a broad subject does not imply familiarity with every specialized term inside it.

Depth should follow relevance: a side concept may receive a compact but complete definition, while the central mechanism receives a full trace. Strict coverage does not require bloating every explanation to the same length.

## Quality Examples

### Cache: insufficient versus rigorous

**Insufficient:** “A cache is a small, fast cupboard near the CPU. A cache hit means the requested item is already there.” This may suggest speed, but it does not let the learner determine where an address is checked or predict a hit.

**Required standard of rigor:** Assume byte-addressed main memory with an $A$-bit address, a direct-mapped cache with $S=2^s$ cache lines, and a block size of $B=2^b$ bytes. Define the address, from low to high bits, as: a $b$-bit **block offset** $[b-1:0]$ selecting the target byte inside the cached block; an $s$-bit **index** $[b+s-1:b]$ uniquely selecting the cache line; and an $A-(s+b)$-bit **tag** in the remaining high bits identifying which main-memory block currently occupies that line. Given an address, retain its offset, use the index to select one line, and read that line's **valid bit**. If valid is 0, the access is a miss. If valid is 1, compare the stored tag bit-for-bit with the address tag: equality means a hit, so use the offset to select the requested byte; inequality means a miss. On a miss, fetch the entire aligned $2^b$-byte block from the next memory level, write it into the indexed line, update the stored tag, set valid to 1, and return the requested data.

This address-bit definition and hit flow are the benchmark for operational precision. Match their rigor where a topic needs it; do not copy their length into unrelated simple explanations.

### K-means: glossary versus motivated journey

**Weak:** List “centroid,” “distance,” “assignment,” and “iteration,” then give one-sentence definitions without showing why the learner needs them or how a dataset changes.

**Strong:** Begin with a concrete dataset of numerical points that must be divided into $k$ groups. Let the learner first solve the limiting cases $k=1$ and $k=n$, then ask how to optimize one fixed cluster's center. Connect this derivation to the already-known idea of moment of inertia only if the learner knows it, and calculate that the cluster's arithmetic mean minimizes the sum of squared distances. State early that the general k-means problem has no universal closed-form solution, so an iterative method is needed. Then derive and execute Lloyd's loop: for data points $x_i$, initialize centers $\mu_1,\ldots,\mu_k$; assign point $i$ to group $c_i=\arg\min_j\lVert x_i-\mu_j\rVert_2^2$, where $\arg\min$ returns the index $j$ with the smallest value; replace each $\mu_j$ by the coordinate-wise arithmetic mean of points assigned to group $j$; and repeat until assignments stop changing or the decrease in $J=\sum_i\lVert x_i-\mu_{c_i}\rVert_2^2$ falls below a stated threshold. Define every symbol and trace actual points through assignment and update. Make clear that Lloyd's algorithm is not the only method: state its assumptions and favorable cases, show boundaries such as unequal feature scales, initialization sensitivity, outliers, empty clusters, and convergence to a local rather than global minimum, then describe the major alternative methods as comprehensively as useful and say which violated assumption or failure case each alternative addresses.

## Response Shape

Adapt length and form to the topic, but normally include:

1. assumed learner range and learning target
2. motivating problem and main example
3. intuitive rough solution and its gap
4. precise definitions and mechanism developed along the example's journey
5. assumptions, applicability boundaries, failure cases, and useful alternatives
6. a worked prediction, calculation, trace, or implementation sketch when applicable
7. the coverage audit

Do not force headings when a short explanation reads better, but preserve the reasoning sequence and audit.

## Mandatory Coverage Audit

End every explanation with a concise **Coverage audit**. List every potentially unfamiliar concept actually mentioned in the response and point to where it was given a non-metaphorical definition and, where applicable, operational or mathematical detail. Verify that:

- no term is only named, analogized, or circularly defined
- every symbol and abbreviation is expanded or defined
- every alternative method mentioned is defined enough for the comparison being made
- assumptions, boundaries, and failure cases needed for independent reasoning were covered

If an item fails the audit, repair the explanation before sending it. Do not report an unexplained item as a harmless omission.
