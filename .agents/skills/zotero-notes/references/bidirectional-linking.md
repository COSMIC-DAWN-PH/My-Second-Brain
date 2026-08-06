<!-- zotero-notes 双向链接工作流（从 SKILL.md 拆分）。章节编号保留，供其它技能引用（如 daily-research §6.2）。-->
# 双向链接建立工作流

本文件由 zotero-notes 的 SKILL.md 引用。创建或更新知识笔记时，必须按此流程完成双向链接。

## 6. 双向链接建立工作流（Bidirectional Linking Workflow）

本节规定 `literature/` 文献笔记与 `Rydberg atom/` 知识笔记之间**双向链接**的完整建立流程。  
每次创建或更新知识笔记时，必须同时完成以下四个步骤，确保两侧笔记均可互相跳转。

---

### 6.1 知识笔记 → 文献笔记（正向链接）

在 `Rydberg atom/` 知识笔记的 **YAML frontmatter** 中，必须声明来源文献的双链：

```yaml
---
aliases: [中文名, 缩写]
tags: [Physics, Quantum, ...]
date: YYYY-MM-DD
status: Draft
source: "[[Literature-File-Name]]"
---
```

同时，在笔记正文顶部（H1 标题下方）添加来源引用行：

```markdown
# English-Name

> 📄 来源文献：[[Literature-File-Name]] · 原始批注见 [p.XX](...)
```

**规则**：
- `source` 字段使用 Obsidian `[[双链]]` 格式，Obsidian 将自动识别反向链接。
- 若同一概念来源于多篇文献，`source` 改为列表：
  ```yaml
  source:
    - "[[Literature-A]]"
    - "[[Literature-B]]"
  ```

---

### 6.2 文献笔记 → 知识笔记（反向链接 / 回链）

在原文献笔记 `## 🖋️ PDF 批注` 区块中，找到对应批注的 `**我的评价**：` 行，将概念名称替换为双链，并注明知识笔记已建立：

```markdown
> [批注原文] [p.XX](zotero://...)

**我的评价**：[[English-Name|概念中文名]] — 知识笔记已建立 ✅
```

此外，在文献笔记末尾（`## 💡 AI 助理建议` 区块之后）新增或更新一个汇总区块：

```markdown
---
## 🔗 衍生知识笔记索引

本文献笔记已为以下概念建立独立知识笔记并完成双向链接：

| 概念 | 知识笔记 | 状态 |
|---|---|---|
| 量子纠错 | [[QEC]] | ✅ 双链已建立 |
| 张量积 | [[Tensor-Product]] | ✅ 双链已建立 |
| CZ 门 | [[CZ-Gate]] | ✅ 双链已建立 |
```

> **注意**：每次新增知识笔记后，必须同步更新此索引表。

---

### 6.3 链接完整性验证

完成知识笔记写作后，按以下清单逐项确认双向链接是否完整：

| 检查项 | 预期状态 |
|---|---|
| 知识笔记 frontmatter 含 `source: "[[文献笔记]]"` | ✅ |
| 知识笔记正文顶部含 `> 📄 来源文献：[[...]]` | ✅ |
| 文献笔记对应批注行已替换为 `[[概念双链]]` | ✅ |
| 文献笔记末尾 `## 🔗 衍生知识笔记索引` 已更新 | ✅ |
| Obsidian 反向链接面板（Backlinks）中两侧均可见对方 | ✅（手动验证） |

若任一项未完成，须立即补全，不得遗留单向链接。

---

### 6.4 双链书写约定

| 场景 | 正确写法 | 错误写法 |
|---|---|---|
| 标准双链 | `[[Rydberg-Blockade\|里德堡阻塞]]` | `[[中文名 (English)]]`（已弃用） |
| 带显示文字 | `[[Rydberg-Blockade\|里德堡阻塞]]` | `[里德堡阻塞](Rydberg-Blockade)` |
| 跨文件夹链接 | `[[Rydberg atom/Rydberg-Blockade]]` | 仅在 Obsidian 无法自动解析时使用 |
| 链接到特定标题 | `[[Rydberg-Blockade#物理直觉]]` | — |

> **原则**：文件名必须与 §5.2 规定的命名格式（`English-Name.md`）完全一致，双链才能被 Obsidian 正确解析。中文别名统一放在 YAML frontmatter `aliases` 字段中，Obsidian 搜索中文时可通过别名找到文件。
