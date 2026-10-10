# Agile Learning Example（敏捷学习示例）

这套示例展示一种搭配：用 agent 规则文件（`AGENTS.md`、`RULES.md`）约束 agent 的工作方式，用 `guided-concept-learning` skill 做概念教学；其中「敏捷学习模式」把一个主题按动机驱动的版本迭代，做成一份 git 管理的笔记——本包附带一个完整实例：POSIX 权限系统的逐版迭代。

## 目录

| 路径 | 是什么 |
|---|---|
| `AGENTS.md` | agent 身份与汇报规范（motivation / design / spec 三层等） |
| `RULES.md` | 用户侧的规则（文件操作安全、工具偏好、代码仓库风格等） |
| `guided-concept-learning/SKILL.md` | 教学 skill（契约式写法：前置条件 / 后置条件 / 不变式 / 违约处理；RFC 2119 关键词）：单次讲解流程 + 敏捷学习模式 |
| `guided-concept-learning/examples/posix-perms-notes/` | 敏捷学习的实例：POSIX 权限系统笔记，含完整 git 历史（`v0` 起） |

## 从哪里看起

- **感受迭代**：`cd guided-concept-learning/examples/posix-perms-notes && git log --oneline`。从下往上是完整的一次迭代：`v0: <动机> → <机制>`（起点版本）、`vN: <动机> → <机制>`（后续版本）、`vN 反思: ...`（更新缺口清单）、`vN 澄清: ...` / `vN 修正: ...`（表述打磨）；每一版提交的 `README.md` 都是该版的完整模型（知识范围 → 动机 → 模型 → 缺口清单 → 概念覆盖审计）。示例历史之上是打包提交与 `SKILL.md` 的历次同步提交。
- **方法的定义**：`guided-concept-learning/SKILL.md` 里的「敏捷学习模式（git 管理的版本迭代）」一节。
- **约束 agent 的规则长什么样**：`AGENTS.md` 与 `RULES.md`。

## 范围说明

`examples/posix-perms-notes` 按 `SKILL.md` 的每版要求完整示范敏捷学习模式：动机驱动的版本迭代、每版完整模型（含知识范围与概念覆盖审计）、缺口清单标注三种类型（内在矛盾 / 未 spec 清楚 / 扩展需求）。
