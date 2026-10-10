# Agile Learning Example（敏捷学习示例）

这套示例展示一种搭配：用 agent 规则文件（`AGENTS.md`、`RULES.md`）约束 agent 的工作方式，用 `guided-concept-learning` skill 做概念教学；其中「敏捷学习模式」把一个主题按动机驱动的版本迭代，做成一份 git 管理的笔记——本包附带一个完整实例：POSIX 权限系统的逐版迭代。学习之后的长期记忆由制卡侧承接：`rigorous-anki-card-authoring` skill 从选定版本取材制卡，`anki-open-template` 生成程序负责出包。

## 目录

| 路径 | 是什么 |
|---|---|
| `AGENTS.md` | agent 身份与汇报规范（motivation / design / spec 三层等） |
| `RULES.md` | 用户侧的规则（文件操作安全、工具偏好、代码仓库风格等） |
| `guided-concept-learning/SKILL.md` | 教学 skill（契约式写法：前置条件 / 后置条件 / 不变式 / 违约处理；RFC 2119 关键词）：单次讲解流程 + 敏捷学习模式 |
| `guided-concept-learning/examples/posix-perms-notes/` | 敏捷学习的实例：POSIX 权限系统笔记，含完整 git 历史（`v0` 起） |
| `rigorous-anki-card-authoring/SKILL.md` | 制卡 skill：逐卡审计与审批的严苛流程；含「与敏捷学习联动」（从选定版本取材、深度跟随版本、版本演进时维护卡组） |
| `anki-open-template/` | 卡片生成程序（TypeScript 模板 + Python 打包脚本，产出 APKG）；完整开发版见 GitHub：`Fun10165/anki-open-template` |

## 从哪里看起

- **感受迭代**：`cd guided-concept-learning/examples/posix-perms-notes && git log --oneline`。从下往上是完整的一次迭代：`v0: <动机> → <机制>`（起点版本）、`vN: <动机> → <机制>`（后续版本）、`vN 反思: ...`（更新缺口清单）、`vN 澄清: ...` / `vN 修正: ...`（表述打磨）；每一版提交的 `README.md` 都是该版的完整模型（知识范围 → 动机 → 模型 → 缺口清单 → 概念覆盖审计）。示例历史之上是打包提交与 `SKILL.md` 的历次同步提交。
- **方法的定义**：`guided-concept-learning/SKILL.md` 里的「敏捷学习模式（git 管理的版本迭代）」一节。
- **约束 agent 的规则长什么样**：`AGENTS.md` 与 `RULES.md`。
- **做出可复习的卡组**：`rigorous-anki-card-authoring/SKILL.md`（逐卡审计、审批后出包；可从选定版本取材）；生成程序在 `anki-open-template/`（入口 `uv run scripts/generate_apkg.py`，细节见其 `README.md`）。

## 范围说明

`examples/posix-perms-notes` 按 `SKILL.md` 的每版要求完整示范敏捷学习模式：动机驱动的版本迭代、每版完整模型（含知识范围与概念覆盖审计）、缺口清单标注三种类型（内在矛盾 / 未 spec 清楚 / 扩展需求）。

制卡程序的完整开发版与问题跟踪在 GitHub（`Fun10165/anki-open-template`）；本包内的 `anki-open-template/` 是它的已提交快照。

## 新增 Skill：专家课程目录（guided-course-outline）

### motivation / 应用场景

准备系统学习一个主题时，需要先确定学哪些内容、按什么顺序学习，以及怎样从基础知识走向独立解决问题。`guided-course-outline` 为这个阶段提供课程目录，随后可以沿目录使用 `guided-concept-learning` 逐节深入学习。

### design

- **输入与起点**：接收学习主题，以及可选的参考资料、已有能力、目标范围和篇幅或课时限制；默认学习者未学过目标学科，将必要的专业前置知识编入课程。
- **课程规划**：围绕目标范围内的独立建模、严谨论证、方法选择、失败诊断与综合工作安排章节，保证前置知识先于使用它的内容，并在课程中安排具体的实践和研究训练。
- **交付形式**：默认只输出课程名称、按学习顺序编号的章名和节名。调整主题、起点或顺序时，同步修复前置依赖与编号，返回完整的新目录。
- **与主 Skill 的衔接**：作为 `guided-concept-learning` 的附属 Skill，负责学习内容、顺序和章节边界；后续逐节展开由主 Skill 负责，并依据完整目录和实际学习进度开展讲解或相应的练习、实验、项目与文献研读。

### spec

| 路径 | 是什么 |
|---|---|
| [guided-course-outline/SKILL.md](guided-course-outline/SKILL.md) | 课程目录生成与修订的完整契约，包含课程边界、设计流程、质量条件和输出要求 |
| [guided-course-outline/agents/openai.yaml](guided-course-outline/agents/openai.yaml) | 界面名称“专家课程目录”、简短说明与默认提示词 |

使用示例：

> 请使用 $guided-course-outline，为 POSIX 权限系统生成专家课程目录。默认我没有学过这个主题，只输出按学习顺序编排的章名和节名。

获得目录后，可以继续：

> 请使用 $guided-concept-learning，结合上面的完整目录，从第一章第一节开始讲解；后续按照我的实际学习进度展开。

目录生成阶段只规划章节，不展开正文、不创建学习仓库，也不修改主 Skill。它适用于原创设计或修订学习目录；提取现有书籍目录、普通概念讲解、关键词清单和直接撰写整门课程不属于其用途。用户指定保存文件时保存，否则直接在对话中提供目录。课程中的能力训练需要在后续学习中实际完成，读完讲解本身不代表获得专家资历。
