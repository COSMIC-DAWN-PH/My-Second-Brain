<!-- daily-research 知识地图 HTML 规范（从 SKILL.md 拆分）。-->
# 交互式知识地图标准（tools/knowledge-map.html）

本文件由 daily-research 的 SKILL.md 引用。每次更新日记时必须同步更新 HTML 中的节点状态。

### 5.2.3 知识地图：交互式 HTML 标准

> 知识地图使用**交互式 HTML** 文件，存放在 `tools/knowledge-map.html`。
> **每次更新日记时，必须同步更新 HTML 中的节点状态。**

**HTML 必须包含的交互功能（2026-06-10 标准）：**

| 功能 | 说明 |
|------|------|
| 深色主题 | 专业科技风格，渐变标题（`--bg: #0f172a`） |
| 统计面板 | 顶部显示各状态数量（understood / getting there / vague / don't know / not started） |
| 加权进度条 | 按 comprehension 加权计算百分比，渐变动画 |
| 状态筛选按钮 | 点击过滤只显示某个状态的节点 |
| 可折叠 Phase | 点击 Phase 标题展开/收起，带动画 |
| 节点点击展开 | 点击任意节点显示详情（block ref、关键公式、wiki-link、状态说明） |
| 左侧色条 | 每个节点左边有 4px 状态色条 |
| 标签系统 | `tag-ref`(紫色) = wiki-link, `tag-block`(红色) = blocker/没懂, `tag-done`(绿色) = block ref, `tag-date`(蓝色) = 日期 |
| 悬停动画 | 节点上浮 + 阴影效果 |

**状态着色规则：**
- `cls-understood` → 绿色 `#10b981`
- `cls-getting` → 蓝色 `#3b82f6`
- `cls-vague` → 橙色 `#f59e0b`
- `cls-dont` → 红色 `#ef4444`
- `cls-todo` → 灰色 `#94a3b8`

**数据结构：**
```javascript
const DATA = [
  {
    label: "Phase A — Title",
    badge: "done" | "wip" | "todo",
    badgeLabel: "06-05 Done",
    nodes: [
      {
        name: "Node Name",
        cls: "understood" | "getting" | "vague" | "dont" | "todo",
        brief: "One-line description",
        detail: "<strong>Status:</strong> ...<br><strong>Block ref:</strong> ...<br><strong>Wiki:</strong> [[...]]",
        tags: [{t:"^260605", c:"done"}, {t:"[[Note]]", c:"ref"}, {t:"BLOCKER", c:"block"}]
      }
    ]
  }
];
```

**嵌入方式：**
```html
<iframe src="file:///C:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/tools/knowledge-map.html" width="100%" height="680" style="border:1px solid #d8dee9; border-radius:6px;"></iframe>
```

**更新规则：**
- 当用户在知识笔记中放置新的 block reference 时，同步更新 HTML 中对应节点的 `cls` 和 `tags`
- 新增笔记时，在对应 Phase 的 `nodes` 数组中添加新节点
- 新增学习阶段时，添加新的 Phase 对象
- HTML 文件路径：`tools/knowledge-map.html`

