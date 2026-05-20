# Quantum Computing Research Vault — Agent Guidelines

## Vault Structure

This is an **Obsidian markdown vault** for neutral-atom quantum computing research. Key folders:

| Folder | Purpose |
|---|---|
| `Literature/` | Zotero-imported paper notes (YAML frontmatter, PDF annotations, Better Notes) |
| `Rydberg atom/` | Self-contained knowledge notes on physics concepts |
| `Daily Notes/` | Research diary entries |
| `.agents/skills/` | Custom Copilot skills (see below) |
| `tools/` | Templates (e.g., `Zotero_Template.md`) |

## Knowledge Note Conventions (Rydberg atom/)

Each note follows a strict structure:

1. **YAML frontmatter**: `aliases`, `tags`, `date`, `status` (Draft / In-Progress / Evergreen), `source` (linked to literature note)
2. **Blockquote source annotation**: `> 来源批注：*"quote"* — Author et al., year, p.X`
3. **Wiki-link cross-references**: `[[English-Name]]` for all linked concepts
4. **Core formula table** at end: `## 📐 核心公式摘要` with Symbol / Meaning / Formula columns
5. **Math**: `$...$` inline, `$$...$$` block only (no `\begin{equation}`)

Example template in: `tools/Zotero_Template.md`

## Literature Note Workflow

Notes from Zotero import include these sections:
- `## 📖 摘要` — Abstract
- `## 📝 Zotero 笔记 (Better Notes)` — LLM chat history / deep dives
- `## 🖋️ PDF 批注` — Annotations with `**我的评价**` fields

When creating derivative knowledge notes, use the `physics-manager` skill (see below).

## Custom Skills (on-demand, invoke via `/`)

| Skill | File | Trigger |
|---|---|---|
| **physics-manager** | `.agents/skills/physics-manager/SKILL.md` | Knowledge note creation, Zotero processing, ontology linking |
| **weekly-summary** | `.agents/skills/weekly-summary/SKILL.md` | "总结我这周干了啥", "weekly summary" |

Key skill behaviors:
- **physics-manager**: Enforces frontmatter, builds `[[双链]]` cross-references, generates formula tables, classifies annotations by category (实验方法 / 关键公式 / 创新点 / 待深入问题)
- **weekly-summary**: Scans `Literature/` and `Rydberg atom/` for new/changed files in the past 7 days, writes structured summary to today's `Daily Notes/`

## File Formatting Rules

- **Line breaks**: Soft-wrapped markdown (no hard line breaks)
- **Tags**: `[Physics, Quantum, ...]` — see existing notes for tag conventions
- **Status values**: `Draft` → `In-Progress` → `Evergreen`
- **English-only naming**: Files named `English-Name.md` for knowledge notes. Chinese aliases go in YAML `aliases` field.
- **Wiki links**: Always use `[[English-Name]]` syntax, with optional display text: `[[Rydberg-Blockade|里德伯阻塞]]`

## Python 图表（替代 Mermaid）

所有曲线图/分布图/统计图统一用 **Python + matplotlib** 绘制，配合 Obsidian Execute Code 插件实时渲染。

为了避免 Obsidian 内置 Python 沙盒环境因为系统字体缺失而产生中文乱码或 `DejaVu Sans` 缺字警告（Glyph missing warnings），且符合国际学术规范，**代码中的所有图表元素（标题、坐标轴标签、图例、数据标注等）必须统一使用标准英文书写**。

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
- **全英文绘图标签**：图表内部所有文本（`title`, `xlabel`, `ylabel`, `label`, `annotate`）必须使用英文，彻底杜绝 CJK 字符警告。不要在代码中设置 `font.sans-serif` 或 `unicode_minus`。
- **LaTeX 大括号与 f-string 冲突防范**：在 Python 的 f-string（即 `f"..."` 或 `fr"..."`）中，LaTeX 能级或单位里的 `{}` 会被 Python 误识别为插值变量，从而抛出 `NameError` 或 `KeyError`。
  - **错误示范**：`fr"Radius $R_b \approx {Rb:.2f}\,\mathrm{m}$"` 会因为 `\mathrm{m}` 中的 `{m}` 报错，Python 会尝试寻找名为 `m` 的变量。
  - **正确防范方法**：
    1. **避免大括号**：用简单的物理符号/单位（如 `\mu m` 代替 `\mathrm{m}`）。
    2. **大括号转义**：如果必须用大括号，必须使用双重括号 `{{}}`（如 `\mathrm{{m}}`）。
- **数学公式支持**：含数学公式的标签用 raw string + `$...$` 包裹（如 `r'Energy $\varepsilon$'`）。
- **布局美化**：统一使用 `plt.tight_layout()` 避免标签裁切，使用 `plt.grid(alpha=0.3, ls=':')` 使网格轻量美观。
- **自包含与高颜值**：图表应具备极高美感（精心挑选颜色如 `#1f77b4`, `#ff7f0e`, `#2ca02c`, `#d62728`，无边框图例 `frameon=False`），并且能够独立说明问题。

> 本 vault 不再使用 Mermaid 图表，所有数据图均由 Python 生成。

## Commands

- **Skills**: Type `/` in chat and select the skill name, or describe the task naturally
- **File creation**: Use `create_file` for new markdown notes; follow the YAML frontmatter and section conventions from existing notes
