# Quantum Computing Research Vault — Agent Guidelines

## 这是什么

这是 Sihao 的**中性原子量子计算科研知识库**，记录里德堡原子量子计算的物理概念、文献笔记和研究进展。目标是形成一个可检索、可交叉引用的个人知识网络。

这是一个 **Obsidian markdown vault**，以下所有语法都是 Obsidian 原生支持的。

## Vault 结构

| 目录 | 用途 |
|------|------|
| `Literature/` | Zotero 导入的论文笔记（YAML frontmatter、PDF 批注、Better Notes） |
| `Rydberg atom/` | 自包含的物理概念知识笔记 |
| `Daily Notes/` | 每日科研日记 |
| `Handout by AI/` | AI 生成的论文讲义（含 Python 图表） |
| `tools/` | 模板文件（`Zotero_Template.md`） |
| `.agents/skills/` | 自定义技能（zotero-notes、weekly-summary、literature-handout、learning-path） |

## Obsidian 双链（Wiki-links）

Obsidian 的核心功能是用 `[[文件名]]` 在笔记之间建立双向链接。

### 基本双链

```
[[English-Name]]
```

- 链接到同 vault 内的另一篇笔记（按文件名匹配）
- 文件名不写 `.md` 后缀

### 带显示文本

```
[[English-Name|显示文本]]
```

示例：`[[Rydberg-Blockade|里德堡阻塞]]` → 在正文中只显示"里德堡阻塞"

### 嵌入笔记（Transclusion）`![[ ]]`

```
![[English-Name]]
```

- 将另一篇笔记的内容**直接嵌入**到当前笔记中渲染
- 常用于在总览笔记中引入多个子概念的完整内容
- 也可以只嵌入某个段落：`![[English-Name#段落标题]]`
- 或嵌入特定块：`![[English-Name^块ID]]`

### 嵌入块（Block Reference）`^块ID`

在段落末尾加 `^my-block-id` 标记块，然后通过 `[[English-Name^my-block-id]]` 引用：

```markdown
这是需要被引用的段落 ^definition-1
```

然后在另一篇笔记：`[[Rydberg-Blockade^definition-1]]`

## 双链策略

每次创建或更新笔记时，必须建立**双向链接**：

1. **新笔记 → 已有笔记**：在新笔记正文中用 `[[English-Name]]` 引用相关知识点（注意：**绝对不能**在双链外层包裹反引号 `` ` ``，否则 Obsidian 会将其渲染为行内代码从而使双链失效）
2. **已有笔记 → 新笔记**：在已有笔记末尾的"相关概念"部分添加 `[[English-Name]]`（同样**不能**包裹反引号）

长期目标：graph view 中每篇笔记至少有 1-2 条连接边。

## Obsidian Callouts（标注框）

用 `> [!类型]` 创建醒目的标注框：

```markdown
> [!tip] 物理直觉
> 里德堡阻塞就像"两个孩子抢一把椅子"。

> [!warning] 常见错误
> 横向门不是对整个码块施加一个大操作。

> [!info] 补充背景
> 这个概念的前置知识是 [[拉比振荡 (Rabi Flopping)]]。

> [!danger] 严重错误
> 混淆物理隐形传态和逻辑隐形传态会导致完全错误的理解。

> [!question] 思考
> 为什么横向门不能实现通用量子计算？

> [!example] 数值例子
> 当 n=60, R=5μm 时，V₁₂ ≈ 2π × 100 MHz。
```

**常用类型：** `note` `info` `tip` `warning` `danger` `question` `example` `quote`

在本 vault 中的推荐用法：

| Callout 类型 | 使用场景 |
|-------------|---------|
| `[!tip]` | 物理直觉、核心类比、记忆技巧 |
| `[!warning]` | 易错点、边界条件、常见误解 |
| `[!info]` | 补充背景知识、前置知识回顾 |
| `[!danger]` | 严重的常见错误 |
| `[!question]` | 值得深入思考的问题 |
| `[!example]` | 典型应用实例、数值计算 |

## YAML Frontmatter / Obsidian Properties

每篇笔记必须包含 YAML 头部（Obsidian 中称为 Properties）：

```yaml
---
aliases:
  - English Alias
  - 中文别名
tags:
  - Physics
  - Quantum
date: 2026-06-01
status: Draft     # Draft → WIP → Evergreen → Archive
source: "[[literature-note]]"
comprehension: "vague"  # don't understand → vague → getting there → understood
---
```

各字段说明：

| 字段 | 必填 | 说明 |
|------|------|------|
| `aliases` | ✅ | 别名（Obsidian 搜索时能匹配到这些词） |
| `tags` | ✅ | 详细标签，Obsidian 的 tag pane 会用 |
| `date` | ✅ | 创建日期 `YYYY-MM-DD` |
| `status` | ✅ | `Draft` → `WIP` → `Evergreen` → `Archive` |
| `source` | ✅ | 链接到来源文献笔记 |
| `comprehension` | ✅ | 理解程度：`don't understand` → `vague` → `getting there` → `understood` |

## 文件命名规则（必须遵守）

格式：**纯英文** `English-Name.md`

- 只使用英文（字母、数字、连字符、空格）
- 中文别名写在 YAML frontmatter 的 `aliases` 字段中
- 避免特殊字符（`/ \ : * ? " < > |`）

| ✅ 正确 | ❌ 错误 |
|---------|--------|
| `Rydberg-Blockade.md` | `里德堡阻塞.md` |
| `Transversal-Teleportation.md` | `横向隐形传态 (TT).md` |
| `Surface-Code.md` | `表面码.md` |

## 知识点笔记内容规范

1. **物理直觉优先** — 先讲核心物理图像，再给公式。用 Callout 标注核心洞察
2. **公式用 KaTeX** — `$...$` 行内，`$$...$$` 行间（不用 `\begin{equation}`）
3. **双链交叉引用** — `[[English-Name]]` 关联其他知识点（**绝对不能**在双链外包围反引号）
4. **Callout 标注** — 用 `> [!tip]` 等做重点标注
5. **核心公式表** — 结尾用 `## 📐 核心公式摘要` 总结关键公式
6. **层级结构** — `#` → `##` → `###`，不要跳级
7. **更新记录** — 文件末尾追加 `## 📝 更新记录`

### 可读性标准（Readability Standard）

**核心原则**：每篇知识笔记必须写到"看完就能懂"的水平。读者读完后应该能够清晰地说出"这个知识点在说什么"。

具体要求：
1. **物理图像先行**：每个概念先用日常直觉或类比解释"它是什么、为什么重要"，再进入数学。
2. **数学推导完整**：公式不能跳步。每一步推导都要说明"我在做什么、为什么可以这样做"。
3. **自包含可理解**：笔记内部应能独立理解，不依赖外部资料。
4. **联系实际**：每个概念都要说明"它在中性原子量子计算中用在哪里"。
5. **图表辅助**：关键流程、对比、演化趋势用 Python matplotlib 图表可视化（全英文标注）。

## 知识点成熟度

| 状态 | 含义 |
|------|------|
| `Draft` | 刚创建，内容不完整 |
| `WIP` | Work In Progress，基本完整但在补充 |
| `Evergreen` | 成熟笔记，可长期参考 |
| `Archive` | 归档，不再维护，保留参考 |

## 理解程度（Comprehension）

| 级别 | 含义 |
|------|------|
| `don't understand` | 完全不理解，需要从头学习 |
| `vague` | 有模糊印象，但不能独立阐述 |
| `getting there` | 能理解主要思路，细节还需巩固 |
| `understood` | 能独立、完整地解释这个概念 |

## Literature Note Workflow

Notes from Zotero import include these sections:
- `## 📖 摘要` — Abstract
- `## 📝 Zotero 笔记 (Better Notes)` — LLM chat history / deep dives
- `## 🖋️ PDF 批注` — Annotations with `**我的评价**` fields

When creating derivative knowledge notes, use the `zotero-notes` skill (see below).

## Custom Skills (on-demand, invoke via `/`)

| Skill | File | Trigger |
|---|---|---|
| **zotero-notes** | `.agents/skills/zotero-notes/SKILL.md` | Zotero 文献笔记处理：提取批注、生成知识笔记、建立双向链接 |
| **weekly-summary** | `.agents/skills/weekly-summary/SKILL.md` | "总结我这周干了啥", "weekly summary" |
| **literature-handout** | `.agents/skills/literature-handout/SKILL.md` | Paper handout generation |
| **learning-path** | `.agents/skills/learning-path/SKILL.md` | "学习路径", "下一步学什么", "learning path", "学习规划" |

Key skill behaviors:
- **zotero-notes**: Enforces frontmatter, builds `[[双链]]` cross-references, generates formula tables, classifies annotations
- **weekly-summary**: Scans `Literature/` and `Rydberg atom/` for new/changed files in past 7 days, writes structured summary to today's `Daily Notes/`
- **learning-path**: Scans comprehension fields & dependency graph in `Rydberg atom/`, generates personalized learning roadmap with tier-based path, bottleneck analysis, and progress visualization

## Python 图表（替代 Mermaid）

所有曲线图/分布图/统计图统一用 **Python + matplotlib** 绘制，配合 Obsidian Execute Code 插件实时渲染。

**代码中的所有图表元素必须统一使用标准英文书写**，以避免 CJK 字符警告。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label=r'Sine Wave $y = \sin(x)$')
plt.xlabel(r'Time $x$ (s)')
plt.ylabel(r'Amplitude $y$')
plt.title('Sine Wave Coherent Dynamics')
plt.grid(alpha=0.3, ls=':')
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
```

**注意事项（必须严格遵守）：**
- **全英文绘图标签**：图表内部所有文本必须使用英文，不要设置 `font.sans-serif` 或 `unicode_minus`。
- **LaTeX 大括号与 f-string 冲突防范**：使用双重括号 `{{}}` 转义。
- **数学公式支持**：含数学公式的标签用 raw string + `$...$` 包裹。
- **布局美化**：统一使用 `plt.tight_layout()` 和 `plt.grid(alpha=0.3, ls=':')`。
- **自包含与高颜值**：图表应具备极高美感，能够独立说明问题。
- **Python 代码自检**：写入笔记前至少用 `ast.parse` 检查代码块语法。

> 本 vault 不再使用 Mermaid 图表，所有数据图均由 Python 生成。

## Interactive HTML / iframe

当需要嵌入动态、可交互的物理图像时，可在 `tools/` 下创建独立 HTML 文件，并用 `<iframe>` 嵌入笔记。

```html
<iframe src="file:///C:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/tools/example.html" width="100%" height="680" style="border:1px solid #d8dee9; border-radius:6px;"></iframe>
```

注意：
- 优先使用绝对 `file:///` URL
- Windows 路径中的空格必须 URL 编码为 `%20`
- 如果 iframe 不能渲染，检查：(1) 插件是否允许 iframe (2) 路径是否正确 (3) 空格是否编码

## 更新记录

每次修改笔记后，如果内容有较大变动，在文件末尾追加 `## 📝 更新记录`：
```markdown
## 📝 更新记录

- 2026-06-01: 初始创建
- 2026-06-05: 添加 Python 图表
```

## 🧠 智能体长期记忆与用户画像 (Agent Memory & User Profile)

任何进入本笔记库的 AI 助理，**在生成任何物理推导、编写讲义或解释概念前，必须率先读取并在内存中加载** `.agents/memory/user_profile.json`。

AI 助理必须根据该画像中所记录的用户学业阶段与物理背景，动态调整所有技术内容的解释深度：
- **严格适配知识边界**：绝不引入超出用户当前学习进度的数学或物理大山。
- **语言与绘图风格偏好**：严格遵循用户在 `vault_preferences` 中设置的双语分工与 CJK-Warning-Free 绘图审美风格。

## Commands

- **Skills**: Type `/` in chat and select the skill name, or describe the task naturally
- **File creation**: Use `create_file` for new markdown notes; follow the YAML frontmatter and section conventions from existing notes
