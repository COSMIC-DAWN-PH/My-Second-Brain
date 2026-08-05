---
name: literature-handout
description: 从学术论文生成结构化中文讲义（markdown），存放在 Obsidian vault 中，纯 Obsidian 原生导航（[[#Heading]]）。触发条件：用户提供论文（arXiv URL / PDF / 标题），要求生成讲义 / 写讲义 / 读论文写讲义 / 生成 handout。
---

# 文献讲义生成流程（Vault-Aware, Obsidian Native）

从学术论文生成结构化中文讲义，中文学术风格，物理系视角。**默认产物是纯 Obsidian markdown 文件**（`[[#Heading]]` 导航，无 `{#anchor-N}`）。不主动问是否要 PDF，用户说了才生成。自动扫描用户的两个 Obsidian 知识库，引用已有知识、检测新知识点并提示补全。

## 当前默认讲义标准（start_up 标准，2026-06-06 更新）

> 完整讲义标准（12 条核心特征）与推荐章节骨架见 **[references/handout-standard.md](references/handout-standard.md)**。生成讲义时必须遵守其中的写作质量与结构规范。

## 核心约束

- **讲解要详细**：多解释"为什么这么做"，不堆公式
- **正文语言**：保留论文标题、文件名、已有英文标题和标准术语；讲义正文、表格说明、总结、导航说明、学习建议等新增解释性内容必须以中文为主，标准术语首次出现时可附英文或中文解释。
- **Python 与图表内部英文**：所有 Python 代码、代码注释、matplotlib 标题/坐标轴/legend/annotation 必须使用英文，避免 CJK 乱码或 glyph warning。不要因为图表规则把讲义正文改成英文。
- **默认 Obsidian markdown**：目录用 `[[#章节标题]]` 链接到对应 `##` 标题，**不在标题末尾加 `{#anchor-N}`**（PDF 锚点）
- **可选 PDF 生成**：仅当用户明确说「生成 pdf / 转 pdf / 发 pdf」时才执行 PDF 步骤。没说要 PDF 就只给 .md
- **物理视角**：假设读者已掌握量子力学算符基础、量子门概念和拉比振荡物理
- **Vault 感知**：生成前必扫 vault，后必检新知
- **中英双语术语**：每个关键名词（概念、方法、门操作、物理量）首次出现时，都标注英文。格式：`CZ 门（Controlled-Z Gate）` 或 `拉比振荡（Rabi Oscillation / Rabi Flopping）`。后续可直接用中文或缩写，但首次必须附英文。
- **Python 可视化**：遇到物理情景（拉比振荡、里德堡势、DRAG 脉冲、RB 衰减等），必须在讲义中添加可运行的 Python + matplotlib 代码块。代码需遵循 vault 规范（CJK-Warning-Free 英文标签、`plt.tight_layout()`、无框图例 `frameon=False`）。

---

## 标准流程

### 第零步：扫描知识库（前置）

**目的**：了解用户已经学过什么，避免重复基础讲解，并在讲义中引用 vault 笔记。

> 两个 vault 的笔记文件清单见 [references/vault-inventory.md](references/vault-inventory.md)。

**扫描内容**：
1. **Quantum Computing Vault**：`C:\Personal Profile\Profile\ScienceResearch\Quantum Computing\Rydberg atom\` 下的所有知识点笔记
2. **MathPhysCore Vault**：`C:\Personal Profile\Profile\MathPhysCore\Knowledge Point\` 下的所有笔记
3. **User Profile**：`C:\Personal Profile\Profile\ScienceResearch\Quantum Computing\.agents\memory\user_profile.json` — 获取用户学业阶段、已完成/进行中的课程

**输出**：建立「已有知识索引」，包含：
- vault 中已有的概念名称列表（从笔记文件名 + YAML aliases 提取）
- 每条笔记的 status（Draft / In-Progress / Evergreen）
- 用户的数学和物理背景完成度

**原则**：
- 对已学概念，讲义中直接引用 vault 笔记：*"你在 [[Rabi-Flopping]] 中学过拉比振荡…"*
- 对已学但不用在讲义主体中重复推导的内容，一句话带过并指向 vault
- 对 status=Draft 或空内容的笔记，视为「知道名字但未深入」，可按需在讲义中适当补充

### 第一步：获取论文信息

根据用户提供的线索定位论文：

- **arXiv URL** → 直接用 `browser_navigate` 打开 arXiv 摘要页
- **arXiv ID** → 导航到 `https://arxiv.org/abs/<ID>`
- **标题关键词** → 用 `mmx search` 或 `browser_navigate` 到 arXiv 搜索
- **PDF 文件** → 用 `pdf-read` skill 提取文本内容

读取摘要、作者、单位、关键图表标题，建立对论文的第一印象。

### 第二步：分析论文结构（深度阅读）

通过以下方式深度理解论文：

1. **读摘要**：提取核心创新点、方法、关键结果
2. **读引言**：理解动机、领域背景、科学问题
3. **读方法/理论部分**：理解核心技术路线
4. **读结果**：关键数据、图表解读
5. **读结论**：意义、局限性、延伸方向

用 `mmx search` 补充背景知识（相关工作、术语解释）。

**输出**：在脑中建立论文的章节框架，识别需要详细讲解的核心内容。

### 第三步：规划讲义结构

根据论文内容设计讲义章节，原则：

- 按论文自然逻辑展开，但不抄原文
- 每章聚焦一个核心概念，用**物理图像**引入
- 公式要解释"这是什么"、"为什么重要"、"怎么用"
- 避免大段引用原文，转化为自己的讲解语言
- **Vault 感知**：对已在 vault 中的概念，用 wiki-link 引用回顾；对不在 vault 中的新概念，做完整讲解
- **分层讲解策略**：
  - status=Evergreen / In-Progress 的概念 → 引用 vault 笔记，一句话回顾核心，直接进入新内容
  - status=Draft（有空内容）的概念 → 可适当补充推导细节以完善理解
  - 不在 vault 中的概念 → 做完整物理图像 + 公式推导

默认优先采用 `start_up.md` 式“物理故事线”结构，而不是机械复述论文目录；典型章节骨架见 [references/handout-standard.md](references/handout-standard.md)。章节名称要按论文内容定制；每一部分都要像 `start_up.md` 一样围绕一个具体物理问题展开。

### 第四步：写 Markdown 讲义

写讲义时的关键规范：

**文件命名**：`[年份]-[论文关键词]-handout.md`，例如 `2023-parallel-gates-handout.md`

**文件头**：默认参照 `start_up.md` 的“极速起步”导言风格：
```markdown
# 🚀 极速起步：论文主题中文讲义（短标题）

> **导言**
> 说明本讲义面向的读者、用户已具备的前置知识、论文解决的核心问题，以及本讲义将如何用物理图像和逐步推导讲清楚。

---
```

如讲义较长可添加目录；目录必须使用 Obsidian 原生 `[[#完整章节标题]]` 链接。

**章节格式**：
```markdown
## N. 章节标题

### 物理图像：...（用生活/物理类比引入）

### 核心概念
（详细解释，包含公式推导）

### 关键点
（总结要点）
```

**注意事项**：
- `##` 标题末尾**不要加 `{#anchor-N}`**，那是 PDF 用的
- 目录链接用 `[[#完整的章节标题]]`，纯 Obsidian 原生跳转
- LaTeX 公式用 `$$ ... $$`（行间）和 `$ ... $`（行内）
- 避免直接大段引用原文
- 需要 Python 可视化时，直接插入可运行的 matplotlib 代码块（参见 vault CJK-Warning-Free 规范）

### 第五步：新知识点检测与补全提醒

**目的**：论文中引入的新概念，可能尚未被收录到 vault 中，提示用户补充。

**操作流程**：
1. 列出讲义中讲解的所有主要知识点（从各章节标题和内容提取）
2. 逐一对照「第零步」建立的已有知识索引
3. 筛选出「不在任何一个 vault 中的」新知识点
4. 对每个新知识点，做简短介绍（3-5 句物理直觉 + 核心公式/概念）
5. 给出补全建议

**输出格式**（放在讲义的末尾，`## 延伸阅读` 之后）：

```markdown
---

## 💡 新知识点补全提醒

以下概念在本次讲义中出现，但目前尚未收录到你的两个知识库中：

### 1. 新概念名称（英文）

> **简要介绍**：3-5 句话的物理直觉 + 核心公式/概念

> 📍 **建议位置**：`Rydberg atom/New-Concept-Name.md`（Quantum Computing Vault）
> 或 `Knowledge Point/分类/New-Concept-Name.md`（MathPhysCore Vault）

> 🔗 **建议链接**：[[已有概念A]]、[[已有概念B]]
```

### 第六步（可选）：PDF 生成

仅当用户明确要求「生成 pdf / 转 pdf / 发 pdf」时执行。完整流程在 `pdf-gen` skill 的 **B. 从 Obsidian 原生讲义转换** 中，包含三步：

1. **渲染 Python 代码块为图片**（如有）→ 提取、修改为 savefig、运行、替换为图片引用
2. **加锚点** → 给 `##` 标题加 `{#anchor-N}`，目录 `[[#标题]]` 换 `[标题](#anchor-N)`
3. **生成 PDF** → 用 pdf-gen 脚本，清理临时文件

> 不动原始 .md 文件。

告知用户：
- markdown 源文件路径
- 提醒目录已使用 Obsidian 原生 `[[#]]` 链接，可在 Obsidian 中直接点击跳转
- 提醒查看讲义末尾的「新知识点补全提醒」

---

## 补充流程 A：课程材料讲义

> 当用户提供**课程材料**（教材 PDF、课件、作业）而非论文时，按 **[references/course-material-flow.md](references/course-material-flow.md)** 执行。

> 用户不再使用独立的 `physics-lecture-notes` skill，此流程已合并至本技能。

## 质量检查清单

生成前自检：
- [ ] 讲义有明确的目标读者定位和前置知识说明
- [ ] 公式都有物理含义解释，不只是堆砌
- [ ] 已完成 vault 扫描（第零步）
- [ ] 对已有知识点了引用 vault 笔记（不是重复推导）
- [ ] 已列出新知识点并给出补全建议（第五步）
- [ ] 目录使用 `[[#标题]]`，没有 `{#anchor-N}` 残留
- [ ] 每个关键名词首次出现有英文标注
- [ ] Python 代码块符合 CJK-Warning-Free 规范，且写入前已用 `ast.parse` 自检
- [ ] 讲义整体达到 `Handout by AI/start_up.md` 的解释深度：物理图像先行、推导不跳步、每节回答一个清晰物理问题
- [ ] 结尾包含 `## 📐 核心公式摘要`、`## 💡 新知识点补全提醒`、`## 📝 更新记录`
- [ ] 表格中的量子态使用 `\vert ... \rangle`，没有让 `|` 破坏 Markdown 表格