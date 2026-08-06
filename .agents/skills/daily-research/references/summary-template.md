<!-- daily-research 写入模板（从 SKILL.md 拆分）。-->
# 科研总结写入模板

本文件由 daily-research 的 SKILL.md 引用。每次运行按此模板填充并写入目标 Daily Note 的 research-summary 区块。

### 4.1 写入结构

每次运行后，将以下结构化内容写入目标 Daily Note：

```markdown
---

<!-- research-summary:start YYYY-MM-DD..YYYY-MM-DD -->
## 📅 今日/单日/本周/阶段性科研进展总结（YYYY-MM-DD 或 YYYY-MM-DD ~ YYYY-MM-DD）

> 时间范围：YYYY-MM-DD ~ YYYY-MM-DD

### 📚 阅读记录

- **[文献/讲义标题]**：阅读了哪些章节，重点关注了什么概念

### 📖 学了什么

| 知识点 | 学习状态 | 来源 |
|--------|---------|------|
| [概念名] | ✅ 已理解 / 🟠 初步了解 / 🔴 没懂 | [[笔记名#章节标题\|章节名]] 或 [[笔记名#^block-id\|章节名]] |

### ❓ 没懂的地方

- [[笔记名#^nuBlockId\|章节名]]：哪里卡住了，需要后续复习

### 📌 下一步

- [ ] [待学习的内容，引用具体章节链接]

<!-- research-summary:end YYYY-MM-DD..YYYY-MM-DD -->
---
```

