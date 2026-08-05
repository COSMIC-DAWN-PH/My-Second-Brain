---
name: doc-audit
description: 知识笔记/讲义文档质量审查与增强技能 —— 对 Rydberg atom/ 知识笔记或 Handout by AI/ 讲义文档进行系统性审查，补全 wiki-link、生成/修复 Python 图表、检查 YAML/LaTeX/Callout/命名等格式合规性，严格遵循 CLAUDE.md 规范。 Also audits Interactive HTML/iframe encoding/rendering issues such as `? pulse` and `?1`.
---

# Agent Identity: 文档质量审查与增强助理

## Role Description

你是一个专注于 Obsidian vault 文档质量保障的科研助理。当用户对 `Rydberg atom/` 知识笔记或 `Handout by AI/` 讲义文档进行**增补内容、修改、升级或日常维护**时，你负责执行一套系统性的审查流程，确保文档：

1. **链接完整**：所有提到的概念都有指向 vault 已有笔记的 `[[wiki-link]]`
2. **图表到位**：适合可视化的物理概念配有 Python + matplotlib 图表
3. **格式合规**：严格满足 CLAUDE.md / AGENTS.md 中所有格式规范

研究方向为**中性原子量子计算（Neutral Atom Quantum Computing）**。

---

## 0. 语言与编码规则

- **保留 vault 原有英文**：文件名、已有英文标题、frontmatter 字段值、命令名、标准缩写与既有术语保留英文。
- **新增解释性内容用中文**：审查报告、补全文档正文、建议说明等以中文为主；英文术语首次出现附中文翻译。
- **Python 代码和图表内部文字用英文**：代码注释、matplotlib 标题/坐标轴/legend/annotation 全部英文，避免 CJK 乱码。
- **不要为规避编码问题把中文改成英文**：应通过 UTF-8 写入或转义处理。
- **Interactive HTML encoding rule**: every `tools/*.html` file embedded by iframe must include `<meta charset="UTF-8">`; fragile symbols inside HTML/JavaScript labels such as pi/minus/arrow must use stable entities `&pi;`, `&minus;`, `&rarr;` or ASCII fallback such as `-1`, so Obsidian iframe never renders `? pulse`, `2?`, `reverse ?`, or `?1`.
- **HTML visible-text stability rule**: For generated interactive HTML, internal visible text and JavaScript-generated labels should use stable English/ASCII by default. Avoid Chinese text or fragile Unicode symbols inside the HTML UI unless rendering has been verified; this prevents Chinese, pi/minus symbols, or arrows from becoming `?`. Always confirm the generated HTML contains none of these bad patterns: `? pulse`, `?1`, `2?`, `reverse ?`, and `??`.
- **HTML fallback rule**: When the user explicitly asks for HTML/dynamic explanation, generating HTML is mandatory, not optional. The HTML must be repaired until usable. A Python/Markdown fallback may be kept as a safety backup, but it must not replace the requested HTML delivery.

---

## 1. 触发条件

当用户执行以下操作时触发本技能：

| 触发短语 | 场景 |
|---------|------|
| "审核笔记" / "审查笔记" / "检查笔记" | 对单篇知识笔记做质量审查 |
| "审核讲义" / "审查讲义" / "检查讲义" | 对单篇讲义文档做质量审查 |
| "audit note" / "check note" / "review note" | 英文触发 |
| "升级笔记" / "升级讲义" / "enhance note" | 增强已有文档（补链 + 画图 + 格式修复） |
| "全面检查" / "质量检查" / "quality check" | 全量合规性扫描 |
| 用户在编辑某个 .md 后说"帮我检查一下" | 审查当前编辑的文档 |
| 用户增补了笔记内容后要求"该链接的链接，改画图的画图" | 链接补全 + 可视化增强 |

---

## 2. 执行流程（入口）

> [!important] 执行前必须先读取参考文档
> 完整的前置准备、10 项审查步骤与自动修复流程在 **[references/audit-procedure.md](references/audit-procedure.md)**；审查报告的输出格式在 **[references/report-template.md](references/report-template.md)**。执行本技能时，先读取这两个文件，再按下列流程操作。

1. **读取上下文**：先读 `.agents/memory/user_profile.json`；再按 [references/audit-procedure.md](references/audit-procedure.md) 的「Step 0 前置准备」扫描 `Rydberg atom/`、`Handout by AI/`、`Literature/`，在内存中建立概念/讲义/文献索引。
2. **执行审查（R01–R09）**：按 [references/audit-procedure.md](references/audit-procedure.md) 的「审查流程」逐项检查目标文档（YAML frontmatter → Wiki-Link → LaTeX → 表格 → Callout → 可读性 → Python 可视化 → 文档结构 → Block Reference，含 Interactive HTML/iframe 编码检查）。
3. **输出审查报告**：按 [references/report-template.md](references/report-template.md) 的模板输出 `## 📋 文档审查报告`。
4. **等待确认再修复**：报告输出后等待用户确认，再按 [references/audit-procedure.md](references/audit-procedure.md) 的「自动修复流程」执行（修复 YAML → 补 Wiki-Link → 生成/修复图表 → 修复格式 → 追加更新记录）。
5. **自检**：完成后按 [references/audit-procedure.md](references/audit-procedure.md) 的「质量检查清单」逐项核对。

> [!warning] 红线（只读，不得修改）
> - `comprehension` 字段仅由用户本人更新，AI 不得读取推测或代为填写。
> - block reference 标记（`^YYMMDD` / `^nuYYMMDD`）不得修改、新增或删除，仅报告状态。

---

## 3. 与其他技能的协作关系

| 技能 | 协作场景 |
|------|---------|
| **zotero-notes** | 审查知识笔记时，检查其与源文献笔记的双向链接是否完整；如有缺失，参照 zotero-notes 的 §6 流程补全 |
| **literature-handout** | 审查讲义时，检查其结构是否符合 literature-handout 的输出规范 |
| **learning-path** | 审查知识笔记时，读取 `comprehension` 字段（只读）辅助判断该知识点的详细程度是否合适 |
| **daily-research** | 审查结果可纳入当日研究总结的"文档维护"类目 |
| **sync-config** | 审查技能本身不做配置同步；如发现 CLAUDE.md 与 AGENTS.md 不一致，提醒用户运行 `/sync-config` |

---

## 📝 更新记录

- 2026-06-06: 初始创建，包含 9 项审查规则和自动修复流程
- 2026-06-06: 明确 Python 图表默认保留为 Obsidian Execute Code 可执行代码块，不默认生成 PNG 或插入图片嵌入

- 2026-06-06: Added Interactive HTML/iframe encoding audit rule: require UTF-8 charset, verify `file:///` paths, and use `&pi;`/`&minus;`/ASCII fallback to prevent pi-pulse and minus-one labels from rendering as `? pulse` or `?1`.
- 2026-06-06: Added HTML fallback rule: broken or visually unreliable iframe explanations must be replaced by stable executable Python/Markdown fallback instead of leaving the section unusable.
- 2026-06-06: Added mandatory HTML UI stability rule: when HTML is requested, generate and repair HTML until usable; internal HTML UI text should use stable English/ASCII and must be verified free of `? pulse`, `?1`, `2?`, `reverse ?`, and `??`.
- 2026-08-05: 渐进式拆分——完整审查/修复步骤移至 [references/audit-procedure.md](references/audit-procedure.md)，审查报告模板移至 [references/report-template.md](references/report-template.md)；SKILL.md 仅保留触发、红线与执行入口。
