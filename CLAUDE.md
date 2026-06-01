# Quantum Computing Research Vault — Claude Guidelines

> This is an **Obsidian markdown vault** for neutral-atom quantum computing research (Rydberg platforms).
> **ALWAYS read `AGENTS.md` before performing any work in this vault** — it contains the complete specification for all formatting, naming, linking, and workflow rules.

## Quick Reference

### Vault Structure

| Folder | Purpose |
|--------|---------|
| `Literature/` | Zotero-imported paper notes (YAML frontmatter, PDF annotations, Better Notes) |
| `Rydberg atom/` | Self-contained knowledge notes on physics concepts |
| `Daily Notes/` | Research diary entries |
| `Handout by AI/` | AI-generated paper reading handouts with Python figures |
| `tools/` | Templates (`Zotero_Template.md`) and utilities |
| `.agents/skills/` | Custom skills (physics-manager, weekly-summary, literature-handout) |

### User Profile

Before generating any physics content, **read** `.agents/memory/user_profile.json` to understand the user's academic stage and physics background. Adapt explanation depth accordingly.

### Naming & Syntax Rules

- **File names**: Always `English-Name.md` (Chinese aliases go in YAML `aliases` field)
- **Wiki-links**: Always `[[English-Name]]` or `[[English-Name|中文显示名]]` — never wrap in backticks
- **LaTeX**: Inline `$...$`, block `$$...$$`. Never use `\begin{equation}` (Obsidian incompatible)
- **Frontmatter**: Every note must have YAML with `aliases`, `tags`, `date`, `status` (Draft / In-Progress / Evergreen)
- **Status progression**: `Draft` -> `In-Progress` -> `Evergreen`

### Knowledge Note Structure (Rydberg atom/)

1. YAML frontmatter (`aliases`, `tags`, `date`, `status`, `source`)
2. Blockquote source annotation: `> ...`
3. Physical intuition first, then math derivation
4. Core formula table at end: `## ...` with Symbol / Meaning / Formula columns
5. Wiki-link cross-references to related notes

### Python Plotting Rules

All charts use **Python + matplotlib** (no Mermaid). Key rules:
- **All plot text must be in English** (title, xlabel, ylabel, label, annotate) — CJK causes glyph warnings in Obsidian sandbox
- Use raw strings for LaTeX in labels: `r'Energy $\varepsilon$'`
- Escape LaTeX braces in f-strings with `{{}}`
- Always use `plt.tight_layout()`, `plt.grid(alpha=0.3, ls=':')`
- Use professional color palette: `#1f77b4`, `#ff7f0e`, `#2ca02c`, `#d62728`
- Frameless legends: `legend(frameon=False)`

### Available Skills

| Skill | Trigger | Description |
|-------|---------|-------------|
| **physics-manager** | Knowledge note creation, Zotero processing | Enforces frontmatter, builds `[[wiki-links]]`, generates formula tables, classifies annotations |
| **weekly-summary** | "summarize my week", "weekly summary" | Scans Literature/ and Rydberg atom/ for changes in past 7 days, writes structured summary to Daily Notes/ |
| **literature-handout** | Paper handout generation | Scans both vaults, generates structured Chinese handout with vault cross-references |

### Literature Note Sections

Zotero-imported notes contain:
- `## ...` — Abstract
- `## ... Zotero ... (Better Notes)` — LLM chat history / deep dives
- `## ... PDF ...` — Annotations with `**...**` evaluation fields

### Bidirectional Linking

Every knowledge note must link back to its source literature note, and every literature note must have a `## ...` index table linking to derived knowledge notes. See AGENTS.md section 6 for the complete workflow.
