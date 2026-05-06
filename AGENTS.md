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
3. **Wiki-link cross-references**: `[[概念名 (English)]]` for all linked concepts
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
- **Bilingual naming**: Files named `中文名 (English).md` for knowledge notes
- **Wiki links**: Always use `[[filename]]` syntax, prefer the English suffix for disambiguation: `[[量子纠错 (QEC)]]`

## Commands

- **Skills**: Type `/` in chat and select the skill name, or describe the task naturally
- **File creation**: Use `create_file` for new markdown notes; follow the YAML frontmatter and section conventions from existing notes
