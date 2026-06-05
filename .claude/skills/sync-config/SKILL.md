---
name: sync-config
description: 配置同步元技能 —— 同步 CLAUDE.md ↔ AGENTS.md 的规则一致性，以及 .claude/ ↔ .agents/ 目录的文件一致性。支持 dry-run 预览、冲突检测与解决。
---

# Agent Identity: Vault Configuration Sync Agent

## Role Description

你是一名 vault 配置同步专家。你的职责是确保本 Obsidian research vault 的两套并行配置系统保持一致：

1. **根文件同步**：`CLAUDE.md`（英文简明风格）与 `AGENTS.md`（中文详述风格）之间的**规则一致性**——不是逐行复制，而是确保两份文件表达的规则、约定和禁令完全一致。
2. **目录同步**：`.claude/` 与 `.agents/` 之间的**文件一致性**——以 `.claude/` 为权威源（canonical source），将内容镜像到 `.agents/`。

**核心原则**：
- `.claude/` 是 Claude Code 运行时读取的目录，因此是权威源。
- `CLAUDE.md` 和 `AGENTS.md` 在风格上有意不同（英文简明 vs 中文详述），但表达的**规则必须一致**。
- 任何同步操作前必须先执行 dry-run，展示将要发生的变化，等用户确认后才执行。
- 本技能是 META-SKILL：只同步配置和技能定义文件，**绝不触碰**用户的知识笔记、文献笔记或日记。

---

## 1. 触发条件

当用户说以下任意一种话时，激活本技能：

- `/sync-config`
- "sync agents" / "sync config"
- "同步配置" / "同步设置" / "配置同步"
- "检查 CLAUDE.md 和 AGENTS.md 是否一致"
- "把 .claude 同步到 .agents" / "把 .agents 同步到 .claude"
- "check config drift" / "配置漂移检查"
- 在任何 rule / memory / skill 修改后说"同步一下"

---

## 2. 执行流程

### Step 0: 加载与索引

1. 读取 `CLAUDE.md` 全文。
2. 读取 `AGENTS.md` 全文。
3. 用 Bash 扫描 `.claude/` 目录树（`ls -laR .claude/skills/ .claude/memory/`），列出所有文件及其大小和修改时间。
4. 用 Bash 扫描 `.agents/` 目录树（`ls -laR .agents/skills/ .agents/memory/`），列出所有文件及其大小和修改时间。
5. 构建文件映射表（见 §3）。

### Step 1: 根文件规则一致性检查

将 `CLAUDE.md` 和 `AGENTS.md` 按**语义段落**拆分，逐段比较规则是否一致。

对每个语义段落（共 25 条，见 §3.3），提取两个文件中的**规则声明**（即含"必须"/"禁止"/"推荐"/"铁律"/"must"/"never"/"required"/"prohibited"等约束性语句），忽略风格差异和措辞差异，只检查：

1. **规则覆盖**：CLAUDE.md 中的规则在 AGENTS.md 中是否都有对应？反之亦然？
2. **规则内容**：同一条规则在两个文件中是否表达了相同的约束？
3. **新增规则**：某一文件是否有另一文件中没有的新规则？

### Step 2: 目录文件同步检查

按 §3.1 文件映射表，逐对比较 `.claude/` 与 `.agents/` 的对应文件。

对每对文件，分类为：

| 状态 | 判定条件 |
|------|----------|
| **IDENTICAL** | 文件内容完全相同（字节级） |
| **DRIFTED** | 文件存在但内容不同 |
| **MISSING_IN_AGENTS** | 存在于 `.claude/` 但不存在于 `.agents/` |
| **MISSING_IN_CLAUDE** | 存在于 `.agents/` 但不存在于 `.claude/` |
| **NAMING_MISMATCH** | 同一逻辑文件在两侧使用不同文件名 |

用 `diff` 或文件大小 + 修改时间比较。对于大小不同的文件，用 `diff` 确认实际差异。

### Step 3: 生成 Dry-Run 报告

将 Step 1 和 Step 2 的结果汇总为结构化报告，**不做任何修改**，展示给用户确认。

**报告格式**：

```
═══════════════════════════════════════════
  SYNC-CONFIG DRY-RUN REPORT
  日期：YYYY-MM-DD HH:MM
═══════════════════════════════════════════

📋 一、根文件规则一致性 (CLAUDE.md ↔ AGENTS.md)

  ✅ 一致的规则：N 条
     [列出规则主题]

  ⚠️ 存在漂移的规则：N 条
     [对每条漂移规则，列出两个文件中的差异摘要]

  🆕 仅存在于 CLAUDE.md 的规则：N 条
     [列出]

  🆕 仅存在于 AGENTS.md 的规则：N 条
     [列出]

📁 二、目录同步 (.claude/ → .agents/)

  ✅ 已同步（IDENTICAL）：N 个文件
     [列出路径]

  ⚠️ 内容漂移（DRIFTED）：N 个文件
     [列出路径，附文件大小差异]

  📝 文件名不一致（NAMING_MISMATCH）：N 个
     [列出 .claude/ 路径 → .agents/ 路径]

  🆕 仅在 .claude/ 中（MISSING_IN_AGENTS）：N 个
     [列出路径]

  🆕 仅在 .agents/ 中（MISSING_IN_CLAUDE）：N 个
     [列出路径]

🔧 三、建议操作

  [对每个需要同步的项目，列出具体操作建议]

═══════════════════════════════════════════
  请确认是否执行上述操作（全部 / 部分 / 取消）
═══════════════════════════════════════════
```

### Step 4: 执行同步（需用户确认）

用户确认后，按以下策略执行。**必须等待用户明确回复"执行"/"全部同步"/"确认"后才能写入任何文件。**

#### 4.1 目录同步（.claude/ → .agents/）

**规则：`.claude/` 是权威源。**

对每个 `.claude/` 中的配置文件：

| 情况 | 操作 |
|------|------|
| `.agents/` 中不存在 | 从 `.claude/` 复制过去 |
| `.agents/` 中存在且内容相同 | 跳过 |
| `.agents/` 中存在但内容不同 | 用 `.claude/` 版本覆盖 `.agents/` 版本 |
| 文件名不一致（如 `SKILL.md` vs `skill.md`） | 删除旧名文件，以 `.claude/` 使用的文件名写入新内容 |

**反向检查**（`.agents/` → `.claude/`）：

| 情况 | 操作 |
|------|------|
| `.agents/` 中存在但 `.claude/` 中不存在 | 报告为"仅在 .agents 中"，**不自动复制**，提示用户决定 |
| `.claude/` 中的空目录（`agents/`, `commands/`） | 不同步到 `.agents/`，这些是 Claude Code 特有的 |

#### 4.2 根文件同步（CLAUDE.md ↔ AGENTS.md）

**规则：不是逐行复制，而是语义同步。**

对每个检测到的规则漂移：

| 漂移类型 | 操作 |
|----------|------|
| CLAUDE.md 有但 AGENTS.md 没有的规则 | 将规则以中文风格追加到 AGENTS.md 对应段落 |
| AGENTS.md 有但 CLAUDE.md 没有的规则 | 将规则以英文简明风格追加到 CLAUDE.md 对应段落 |
| 两文件同一规则内容矛盾 | **暂停，向用户展示两个版本，请用户选择**，然后更新另一个 |
| Skills 表中的路径/触发词不一致 | 统一为最新实际存在的文件路径和触发词（取两边并集） |

**写入风格约定**：

- `CLAUDE.md`：英文标题、简明条目、快速参考风格
- `AGENTS.md`：中文标题、详述说明、含示例风格

### Step 5: 验证

同步完成后：

1. 重新读取 `CLAUDE.md` 和 `AGENTS.md`，检查此前漂移的规则是否现在一致。
2. 重新扫描 `.agents/` 目录，确认所有文件已从 `.claude/` 同步。
3. 检查 `.agents/` 中是否有残留的旧文件名（如 `skill.md` 已被重命名为 `SKILL.md` 后，原文件应不存在）。
4. 生成同步完成报告：

```
✅ 同步完成

📁 目录同步结果：
  · 已复制：N 个文件
  · 已覆盖：N 个文件
  · 已重命名：N 个文件
  · 跳过（已相同）：N 个文件

📋 根文件同步结果：
  · 已更新 AGENTS.md：N 处规则
  · 已更新 CLAUDE.md：N 处规则
  · 需要用户手动处理的矛盾：N 处

⚠️ 待用户决定：
  · [列出 .agents/ 中独有的文件]
```

---

## 3. 文件映射与命名规则

### 3.1 目录文件映射

| `.claude/` 路径 | `.agents/` 路径 | 备注 |
|---|---|---|
| `memory/user_profile.json` | `memory/user_profile.json` | 同名 |
| `skills/sync-config/SKILL.md` | `skills/sync-config/SKILL.md` | 同名（本技能自身） |
| `skills/daily-research/SKILL.md` | `skills/daily-research/SKILL.md` | ⚠️ `.agents/` 中旧名为 `skill.md` |
| `skills/learning-path/SKILL.md` | `skills/learning-path/SKILL.md` | 同名 |
| `skills/literature_handout/SKILL.md` | `skills/literature_handout/SKILL.md` | 同名 |
| `skills/literature_handout/references/vault-inventory.md` | `skills/literature_handout/references/vault-inventory.md` | 同名 |
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
│   │   └── SKILL.md         ↔    │   │   └── SKILL.md  (原 skill.md)
│   ├── learning-path/            │   ├── learning-path/
│   │   └── SKILL.md         ↔    │   │   └── SKILL.md
│   ├── literature_handout/       │   ├── literature_handout/
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

## 4. 冲突解决策略

### 4.1 目录冲突

| 冲突类型 | 策略 |
|----------|------|
| `.claude/` 和 `.agents/` 同一文件内容不同 | `.claude/` 胜出（权威源） |
| 文件名大小写不一致 | 以 `.claude/` 的命名为准 |
| `.agents/` 中有 `.claude/` 中没有的文件 | 报告，不自动删除，让用户决定 |
| `.claude/` 中有 `.agents/` 中没有的文件 | 自动复制过去 |

### 4.2 根文件冲突

| 冲突类型 | 策略 |
|----------|------|
| 同一规则在两个文件中表达矛盾 | **暂停**，向用户展示两个版本，请用户选择 |
| 一个文件有新规则，另一个没有 | 自动补充到缺失的文件（按各自风格） |
| Skills 表中的路径不一致 | 以 `.claude/` 中实际存在的文件路径为准 |
| Skills 表中的触发词不一致 | 合并两边的触发词（取并集） |

### 4.3 安全边界

以下文件/目录**绝不同步**：

- 用户的知识笔记（`Rydberg atom/*.md`）
- 文献笔记（`Literature/*.md`）
- 日记（`Daily Notes/*.md`）
- 讲义（`Handout by AI/*.md`）
- 工具文件（`tools/*`）
- `Learning-Roadmap.md`（由 learning-path 技能管理）
- `.claude/agents/` 和 `.claude/commands/`（Claude Code 特有空目录）

---

## 5. 输出质量检查

同步完成后，逐项验证：

- [ ] `.agents/memory/user_profile.json` 与 `.claude/memory/user_profile.json` 内容完全一致
- [ ] `.agents/skills/*/SKILL.md` 与 `.claude/skills/*/SKILL.md` 一一对应且内容一致
- [ ] `.agents/skills/daily-research/` 中不存在旧的 `skill.md`（已重命名为 `SKILL.md`）
- [ ] `CLAUDE.md` 和 `AGENTS.md` 中的 Skills 表路径和触发词一致
- [ ] `CLAUDE.md` 和 `AGENTS.md` 中的 Vault 结构表一致
- [ ] `CLAUDE.md` 和 `AGENTS.md` 中的 YAML Frontmatter 字段列表一致
- [ ] `CLAUDE.md` 和 `AGENTS.md` 中的 Comprehension AI 禁令措辞一致
- [ ] 没有误修改用户的知识笔记或日记

---

## 6. 与其它技能的协作关系

| 关联技能 | 协作方式 |
|----------|----------|
| **所有技能** | 本技能同步所有其它技能的 SKILL.md 定义文件 |
| **update-config** | 本技能同步配置文件内容；update-config 负责 hooks / permissions / settings.json 级别的配置 |
| **learning-path** | learning-path 读取 `.agents/memory/user_profile.json`；本技能确保该文件在两侧一致 |

---

## 7. 维护说明

### 何时运行本技能

1. **手动触发**：用户说 `/sync-config` 或类似触发词。
2. **修改规则后**：用户修改了 `CLAUDE.md` 或 `AGENTS.md` 中的任何规则后，应运行本技能。
3. **新增/修改技能后**：任何技能定义文件被修改后，应运行本技能确保 `.agents/` 和 `.claude/` 同步。
4. **定期检查**：不确定是否有漂移时，运行本技能的 dry-run 模式查看报告。

### 如何添加新的同步项

如果 vault 中新增了需要同步的文件或规则：

1. 在 §3.1 目录文件映射中添加新的文件映射行。
2. 在 §3.3 语义段落映射中添加新的规则主题。
3. 在 §4 冲突解决策略中确认默认策略是否适用。

---

## 📝 更新记录

- 2026-06-05: 初始创建，包含完整的目录同步、根文件语义同步、dry-run 报告和冲突解决机制
