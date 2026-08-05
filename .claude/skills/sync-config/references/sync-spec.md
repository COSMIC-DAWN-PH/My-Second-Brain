<!-- sync-config 文件映射与命名规则（从 SKILL.md 拆分）。-->
# 文件映射与命名规则（同步规格）

本文件由 sync-config 的 SKILL.md 引用。执行 SKILL.md 中的 Step 1（根文件一致性检查）与 Step 2（目录文件同步检查）时，读取本文件，按其中的文件映射表、目录树与 R01–R25 语义段落映射逐项操作。

## 3. 文件映射与命名规则

### 3.1 目录文件映射

| `.claude/` 路径 | `.agents/` 路径 | 备注 |
|---|---|---|
| `memory/user_profile.json` | `memory/user_profile.json` | 同名 |
| `skills/sync-config/SKILL.md` | `skills/sync-config/SKILL.md` | 同名（本技能自身） |
| `skills/daily-research/SKILL.md` | `skills/daily-research/SKILL.md` | 同名 |
| `skills/learning-path/SKILL.md` | `skills/learning-path/SKILL.md` | 同名 |
| `skills/literature-handout/SKILL.md` | `skills/literature-handout/SKILL.md` | 同名 |
| `skills/literature-handout/references/vault-inventory.md` | `skills/literature-handout/references/vault-inventory.md` | 同名 |
| `skills/zotero-notes/SKILL.md` | `skills/zotero-notes/SKILL.md` | 同名 |

**标准文件名约定**：所有技能定义文件统一使用 `SKILL.md`（全大写）。历史遗留的 `skill.md`（小写）应重命名为 `SKILL.md`。

### 3.2 目录结构映射（可视化）

```
.claude/                          .agents/
├── memory/                       ├── memory/
│   └── user_profile.json    ↔    │   └── user_profile.json
├── skills/                       ├── skills/
│   ├── sync-config/              │   ├── sync-config/
│   │   └── SKILL.md         ↔    │   │   └── SKILL.md
│   ├── daily-research/           │   ├── daily-research/
│   │   └── SKILL.md         ↔    │   │   └── SKILL.md
│   ├── learning-path/            │   ├── learning-path/
│   │   └── SKILL.md         ↔    │   │   └── SKILL.md
│   ├── literature-handout/      │   ├── literature-handout/
│   │   ├── SKILL.md         ↔    │   │   ├── SKILL.md
│   │   └── references/           │   │   └── references/
│   │       └── vault-inventory.md ↔  │       └── vault-inventory.md
│   └── zotero-notes/             │   └── zotero-notes/
│       └── SKILL.md         ↔    │       └── SKILL.md
├── agents/  (Claude Code 特有)   │
├── commands/ (Claude Code 特有)  │
```

### 3.3 根文件语义段落映射（25 条规则主题）

根文件同步不是结构对齐，而是**语义对齐**。以下列出需要保持一致的规则主题，不要求段落顺序或标题文字相同：

| ID | 规则主题 | CLAUDE.md 参考位置 | AGENTS.md 参考位置 |
|----|----------|-------------------|-------------------|
| R01 | Vault 结构表 | `### Vault Structure` | `## Vault 结构` |
| R02 | 文件命名规则 | `### Naming & Syntax Rules` | `## 文件命名规则` |
| R03 | Wiki-link 基本语法 | `### Naming & Syntax Rules` | `## Obsidian 双链` |
| R04 | Wiki-link 表格转义 | `### Naming & Syntax Rules` | `### Markdown 表格中的双链转义` |
| R05 | Block Reference 语法 | `### Naming & Syntax Rules` | `### 嵌入块（Block Reference）` |
| R06 | Block Reference 区间语义 | `### Naming & Syntax Rules` | `### 学习进度 Block Reference 的区间语义` |
| R07 | 章节链接语法 | `### Naming & Syntax Rules` | `### 链接到具体章节` |
| R08 | Embed/Transclusion 语法 | `### Embed 语法` | `### 嵌入笔记（Transclusion）` |
| R09 | 双链策略（双向链接要求） | `### Bidirectional Linking` | `## 双链策略` |
| R10 | LaTeX 规范 | `### Naming & Syntax Rules` | `## 知识点笔记内容规范` |
| R11 | LaTeX 表格铁律（`\vert` 替代） | `### Naming & Syntax Rules` | （检查是否缺失） |
| R12 | YAML Frontmatter 字段规范 | `### YAML Frontmatter (Required)` | `## YAML Frontmatter / Obsidian Properties` |
| R13 | 知识笔记内容结构 | `### Knowledge Note Structure` | `## 知识点笔记内容规范` |
| R14 | 可读性标准 | `### 可读性标准` | `### 可读性标准` |
| R15 | 语言与编码规则 | `### 语言与编码规则` | `### 语言与编码铁律` |
| R16 | Callout 类型表 | `### Obsidian Callouts` | `## Obsidian Callouts` |
| R17 | 知识点成熟度状态表 | `### 知识点成熟度` | `## 知识点成熟度` |
| R18 | 理解程度状态表 | `### 理解程度` | `## 理解程度` |
| R19 | Comprehension AI 禁令 | `### 理解程度` 中 | `## 理解程度` 中 |
| R20 | Python 图表规则 | `### Python Plotting Rules` | `## Python 图表` |
| R21 | Interactive HTML / iframe | `### Interactive HTML / iframe` | `## Interactive HTML / iframe` |
| R22 | 更新记录格式 | `### 更新记录` | `## 更新记录` |
| R23 | Skills 表（含路径和触发词） | `### Available Skills` | `## Custom Skills` |
| R24 | Literature Note 段落结构 | `### Literature Note Sections` | `## Literature Note Workflow` |
| R25 | Agent Memory 与 User Profile | `## Agent Memory & User Profile` | `## 🧠 智能体长期记忆与用户画像` |

---

