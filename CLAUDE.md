# Quantum Computing Research Vault — Claude Guidelines

> This is an **Obsidian markdown vault** for neutral-atom quantum computing research (Rydberg platforms).
> **ALWAYS read `AGENTS.md` before performing any work in this vault** — it contains the complete specification for all formatting, naming, linking, and workflow rules.

> **⚡ 双文件同步规则**：`CLAUDE.md` 和 `AGENTS.md` 是 vault 规则的两个副本。**每次修改任何规则（skill 描述、格式规范、AI 禁令等）时，必须同时更新两个文件，保持内容一致。** 只改一个 = 另一个会过时，后续 session 会读到矛盾的指令。

## Quick Reference

### Vault Structure

| Folder | Purpose |
|--------|---------|
| `Literature/` | Zotero-imported paper notes (YAML frontmatter, PDF annotations, Better Notes) |
| `Rydberg atom/` | Self-contained knowledge notes on physics concepts |
| `Daily Notes/` | Research diary entries |
| `Handout by AI/` | AI-generated paper reading handouts with Python figures |
| `tools/` | Templates (`Zotero_Template.md`) and utilities |
| `.agents/skills/` | Custom skills (zotero-notes, daily-research, literature-handout, learning-path, doc-audit) |

### User Profile

Before generating any physics content, **read** `.agents/memory/user_profile.json` to understand the user's academic stage and physics background. Adapt explanation depth accordingly.

### Naming & Syntax Rules

- **File names**: Always `English-Name.md` (Chinese aliases go in YAML `aliases` field)
- **Wiki-links**: `[[English-Name]]` or `[[English-Name|中文显示名]]` — NEVER wrap in backticks (breaks Obsidian indexing)
- **Wiki-links inside Markdown tables**: Escape display pipes as `[[English-Name\|中文显示名]]`; otherwise the `|` breaks table columns. Normal paragraphs can use `[[English-Name|中文显示名]]`.
- **链接到具体章节**：`[[English-Name#章节标题]]` — 点击后直接跳转到目标笔记的对应章节。章节标题必须与笔记中的 `##` / `###` 标题文字完全一致。示例：`[[2023-parallel-gates-handout#6. 核心创新一：时间最优单脉冲门]]`
- **链接到 block reference**：`[[English-Name^block-id]]` — 跳转到目标笔记中标记了 `^block-id` 的段落。可结合显示文本：`[[English-Name^block-id|显示文本]]`。示例：`[[Single-Qubit-Gates#^321fbe|旋转门]]`
- **链接到章节 + 显示文本**：`[[English-Name#章节标题|显示文本]]` — 跳转到章节但显示自定义文字。示例：`[[Rydberg-Blockade#2. 数学描述：阻塞条件|阻塞条件]]`
- **⚠️ 章节链接显示文字必须包含标题关键词**：禁止只写 `§4`、`§5.2` 等纯编号。正确格式：`文件名 §N 标题`，如 `Hyperfine-Structure §4 Clock State 编码`、`start_up §5.2 失谐脉冲与 Rz 门`。读者应不用 hover 就能知道链接指向哪个文章的哪个知识点。
- **Embeds**: `![[English-Name]]` for transclusion, `![[English-Name#Section]]` for partial embed
- **Block references**: `^block-id` at paragraph end, then `[[English-Name^block-id]]` to reference
- **学习进度 Block Reference 的区间语义**：在知识笔记中，`^YYMMDD` 和 `^nuYYMMDD` 交替形成区间——每个标记管到上一个相反类型的标记为止。`^260604` = 之前已学懂，`^nu260604` = 之前没懂。示例：`^260604` → `^nu260604` → `^260604` 表示"已学→没懂→已学"三段交替
- **LaTeX**: Inline `$...$`, block `$$...$$`. Never use `\begin{equation}`
- **⚠️ Markdown 表格中的 LaTeX（铁律）**：`|0\rangle` 中的 `|` 会被 markdown 解析器优先当作表格列分隔符，即使用 `\|` 转义也经常失败（因为 `\|` 本身也被当作管道符处理）。**✅ 推荐解法：用 `\vert` 替代 `|`**，例如 `$\vert 0 \rangle$` 而不是 `$|0\rangle$`，`\vert` 是 LaTeX 命令，不会被 Markdown 解析器误识别为列分隔符。**退选方案：公式摘要一律用列表格式，绝不用表格。**
- **Line breaks**: Soft-wrapped markdown (no hard line breaks)
- **Tags**: `[Physics, Quantum, ...]` — see existing notes for tag conventions

### 语言与编码规则

- **保留 vault 原有英文**：文件名、已有英文标题、frontmatter 字段值、命令名、代码标识符、标准缩写与既有术语（如 Learning Roadmap、Rydberg blockade、Surface code、CZ gate、QEC、AC Stark effect）可以保留英文，不要硬翻。
- **新增解释性内容用中文**：新写给用户阅读的笔记正文、讲义、学习路线图、科研总结、表格说明、任务建议、更新记录等，默认用中文；若引入英文术语，应尽量附中文解释或中文翻译。
- **Python 代码和图表内部文字用英文**：代码注释、matplotlib 标题、坐标轴、legend、annotation 等使用英文，避免 CJK 乱码或 glyph warning。
- **不要为规避编码问题把中文解释改成英文**：应通过 UTF-8 写入、转义或脚本处理解决。

### YAML Frontmatter (Required)

Every note must have:
```yaml
---
aliases:
  - English Alias
  - 中文别名
tags:
  - Physics
  - Quantum
date: 2026-06-01
status: Draft  # Draft -> WIP -> Evergreen -> Archive
source: "[[literature-note]]"
comprehension: "vague"  # don't understand -> vague -> getting there -> understood
---
```

| Field | Required | Description |
|-------|----------|-------------|
| `aliases` | ✅ | Aliases for Obsidian search (Chinese + English) |
| `tags` | ✅ | Tags for categorization in tag pane |
| `date` | ✅ | Creation date `YYYY-MM-DD` |
| `status` | ✅ | Maturity: `Draft` → `WIP` → `Evergreen` → `Archive` |
| `source` | ✅ | Link to source literature note |
| `comprehension` | ✅ | User's understanding level — **⚠️ AI 禁止修改此字段**，仅由用户本人手动更新 |

### Knowledge Note Structure (Rydberg atom/)

1. YAML frontmatter (`aliases`, `tags`, `date`, `status`, `source`, `comprehension`)
2. Blockquote source annotation: `> ...`
3. **Physical intuition first** — explain "what" and "why" before formulas
4. **Obsidian Callouts** — use `> [!tip]`, `> [!warning]` etc. for key insights
5. Math derivation with complete steps
6. Core formula table at end: `## 📐 核心公式摘要` with Symbol / Meaning / Formula columns
7. Wiki-link cross-references to related notes
8. Update log at end: `## 📝 更新记录`

Example template in: `tools/Zotero_Template.md`

### 可读性标准（Readability Standard）

**核心原则**：每篇知识笔记必须写到"看完就能懂"的水平。读者读完后应该能够清晰地说出"这个知识点在说什么"。

具体要求：
1. **物理图像先行**：每个概念先用日常直觉或类比解释"它是什么、为什么重要"，再进入数学。
2. **数学推导完整**：公式不能跳步。每一步推导都要说明"我在做什么、为什么可以这样做"。
3. **自包含可理解**：笔记内部应能独立理解，不依赖外部资料。
4. **联系实际**：每个概念都要说明"它在中性原子量子计算中用在哪里"。
5. **图表辅助**：关键流程、对比、演化趋势用 Python matplotlib 图表可视化（全英文标注）。

### Obsidian Callouts（标注框）

用 `> [!类型]` 创建醒目的标注框。在知识笔记中推荐用法：

| Callout 类型 | 使用场景 |
|-------------|---------|
| `[!tip]` | 物理直觉、记忆技巧、核心类比 |
| `[!warning]` | 易错点、边界条件、常见误解 |
| `[!info]` | 补充背景知识、前置知识回顾 |
| `[!danger]` | 严重的常见错误 |
| `[!question]` | 值得深入思考的问题 |
| `[!example]` | 典型应用实例、数值计算 |

示例：
```markdown
> [!tip] 物理直觉
> 里德堡阻塞就像"两个孩子抢一把椅子"——一个原子坐了里德堡态的"椅子"，另一个就坐不上去。

> [!warning] 常见错误
> 注意：横向门不是"对整个码块施加一个大操作"，而是对每对物理 qubit 独立施加小操作。
```

### Embed 语法（Transclusion）

嵌入另一篇笔记的完整内容：
```markdown
![[English-Name]]
```

嵌入某个章节：
```markdown
![[English-Name#章节标题]]
```

嵌入特定块（先在源笔记中标记 `^block-id`）：
```markdown
![[English-Name^block-id]]
```

### 更新记录

每次修改笔记后，如果内容有较大变动，在文件末尾追加：
```markdown
## 📝 更新记录

- 2026-06-01: 初始创建，包含核心概念和公式推导
- 2026-06-05: 添加 Python 图表，补充 Gate Teleportation 部分
```

### 知识点成熟度

| 状态 | 含义 |
|------|------|
| `Draft` | 刚创建，内容不完整 |
| `WIP` | Work In Progress，基本完整但在补充 |
| `Evergreen` | 成熟笔记，可长期参考 |
| `Archive` | 归档，不再维护，保留参考 |

### 理解程度（Comprehension）

> **⛔ AI 禁令**：`comprehension` 字段仅由用户本人更新。AI 助理在任何情况下都不得读取、推测或修改此字段的值。AI 只能读取它以了解上下文，绝不能代为填写或升级。

| 级别 | 含义 |
|------|------|
| `don't understand` | 完全不理解，需要从头学习 |
| `vague` | 有模糊印象，但不能独立阐述 |
| `getting there` | 能理解主要思路，细节还需巩固 |
| `understood` | 能独立、完整地解释这个概念 |

### Python Plotting Rules

All charts use **Python + matplotlib** (no Mermaid). Key rules:
- **All plot text must be in English** — CJK causes glyph warnings in Obsidian sandbox
- Use raw strings for LaTeX in labels: `r'Energy $\varepsilon$'`
- Escape LaTeX braces in f-strings with `{{}}`
- Always use `plt.tight_layout()`, `plt.grid(alpha=0.3, ls=':')`
- Use professional color palette: `#1f77b4`, `#ff7f0e`, `#2ca02c`, `#d62728`
- Frameless legends: `legend(frameon=False)`

**注意事项（必须严格遵守）：**
- **全英文绘图标签**：图表内部所有文本必须使用英文，不要设置 `font.sans-serif` 或 `unicode_minus`。
- **LaTeX 大括号与 f-string 冲突防范**：使用双重括号 `{{}}` 转义。
- **自包含与高颜值**：图表应具备极高美感，能够独立说明问题。

> 本 vault 不再使用 Mermaid 图表，所有数据图均由 Python 生成。

### Interactive HTML / iframe

当需要嵌入动态、可交互的物理图像时，可在 `tools/` 下创建独立 HTML 文件，并用 `<iframe>` 嵌入笔记。

```html
<iframe src="file:///C:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/tools/example.html" width="100%" height="680" style="border:1px solid #d8dee9; border-radius:6px;"></iframe>
```

注意：
- 优先使用绝对 `file:///` URL
- Windows 路径中的空格必须 URL 编码为 `%20`
- 如果 iframe 不能渲染，检查 Obsidian 插件是否允许 iframe/HTML/JavaScript

### Available Skills

| Skill | Trigger | Description |
|-------|---------|-------------|
| **zotero-notes** | Zotero 批注处理、知识笔记生成 | 从 Zotero 论文笔记中提取批注，生成知识笔记，建立双向链接 |
| **daily-research** | "总结今天/昨天", "daily summary", "weekly summary", "research summary", "规划今天" | 总结学习进展 + 规划当日学习任务。扫描 Literature/ 与 Rydberg atom/，基于 block reference 证据写入 Daily Notes/ 的总结区块和学习计划。 |
| **literature-handout** | Paper handout generation | Scans both vaults, generates structured Chinese handout with vault cross-references |
| **learning-path** | "学习路径", "下一步学什么", "learning path" | Scans comprehension fields in Rydberg atom/, generates Learning-Roadmap.md at vault root with tier-based path and bottleneck analysis |
| **sync-config** | `/sync-config`, "同步配置", "sync agents", "check config drift" | 配置同步元技能：同步 CLAUDE.md ↔ AGENTS.md 规则一致性，以及 .claude/ ↔ .agents/ 目录文件一致性 |
| **doc-audit** | "审核笔记", "检查笔记", "audit note", "升级笔记", "该链接的链接，改画图的画图" | 知识笔记/讲义文档质量审查与增强：系统性扫描 YAML/wiki-link/LaTeX/Callout/可视化/格式合规性，补全链接、生成图表、修复格式 |

### Literature Note Sections

Zotero-imported notes contain:
- `## 📖 摘要` — Abstract
- `## 📝 Zotero 笔记 (Better Notes)` — LLM chat history / deep dives
- `## 🖋️ PDF 批注` — Annotations with `**我的评价**` evaluation fields

### Bidirectional Linking

Every knowledge note must link back to its source literature note, and every literature note must have a `## 📑 知识点索引` table linking to derived knowledge notes.

## Agent Memory & User Profile

任何进入本笔记库的 AI 助理，**在生成任何物理推导、编写讲义或解释概念前，必须率先读取并在内存中加载** `.agents/memory/user_profile.json`。

AI 助理必须根据该画像中所记录的用户学业阶段与物理背景，动态调整所有技术内容的解释深度：
- **严格适配知识边界**：绝不引入超出用户当前学习进度的数学或物理大山。
- **语言与绘图风格偏好**：严格遵循用户在 `vault_preferences` 中设置的双语分工与 CJK-Warning-Free 绘图审美风格。

## Commands

- **Skills**: Type `/` in chat and select the skill name, or describe the task naturally
- **File creation**: Use `create_file` for new markdown notes; follow the YAML frontmatter and section conventions from existing notes
