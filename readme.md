# 🌌 中性原子量子物理科研笔记库 (Quantum Computing Research Vault)

> **欢迎来到你的“第二大脑”（My Second Brain）！**
> 本仓库是一个专为**中性原子量子计算与里德伯原子体系（Neutral-Atom Rydberg Platform）**研究而设计的专业化 Obsidian 笔记库。
> 它融合了 Zotero 文献管理、Obsidian 知识图谱双向链接、基于 Python 的交互式动力学仿真，以及高度智能的 AI 助理（Agent）自适应工作流。

---

## 📂 仓库目录架构图与职责分工

| 文件夹/文件 | 核心职责与用途 | 包含的关键要素 |
| :--- | :--- | :--- |
| **`Literature/`** | Zotero 导入文献笔记区 | 存放论文的摘要、Zotero Better Notes 深度解读、PDF 批注以及 AI 自动提取的衍生知识索引表。 |
| **`Rydberg atom/`** | 中性原子物理核心知识库 | 存放原子物理、量子信息、里德伯阻塞、CZ 门等概念笔记，文件统一采用 `English-Name.md` 命名，内部采用双语双链管理。 |
| **`Daily Notes/`** | 日度科研进展与随笔日记 | 记录你每天的实验想法、文献学习进度，同时是 AI **科研总结技能（research-summary）** 自动追加或更新写入的目的地。 |
| **`Handout by AI/`** | AI 辅助研读学术讲义区 | 存放 AI 为你量身定制的顶级论文导读讲义（如 [start_up.md](file:///C:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/Handout%20by%20AI/start_up.md)）及与其配套的 200 DPI 科学仿真插图。 |
| **`tools/`** | 模板与本地脚本工具区 | 包含 `Zotero_Template.md`（Zotero 导入排版标准模板）和用于提取 PDF 批注的底层可执行程序。 |
| **`.agents/skills/`** | 针对本笔记库的**私有 AI 技能库** | 包含 [zotero-notes](file:///c:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/.agents/skills/zotero-notes/SKILL.md) 与 [research-summary](file:///c:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/.agents/skills/research-summary/SKILL.md) 技能。 |
| **`AGENTS.md`** | **AI 助理的行为法则与笔记规范宪章** | 任何进入本仓库的 AI 编码助手必须阅读的第一文件，规定了文件命名、LaTeX 语法、双链书写以及 Python 绘图的防报错规则。 |
| **`readme.md`** | 仓库主页与使用指南（当前文件） | 仓库的整体导航与协作指引。 |

---

## 🤖 AI 智能协同工作流（Agent Collaboration）

本笔记库的灵魂在于其与 AI 助理（如 Antigravity）的无缝协作。通过根目录的 `AGENTS.md` 和 `.agents/skills/`，AI 助理拥有两个专门针对本笔记库定制的专属技能：

1. **Zotero 文献笔记处理 (`/zotero-notes`)**：
   - 当你从 Zotero 导入新论文时，激活此技能。
   - 它能自动扫描你的批注，提炼物理概念并在 `Rydberg atom/` 文件夹下生成知识笔记，并在原文献笔记中回填 `[[双向链接]]`。
   
2. **弹性科研进度追踪者 (`/research-summary`)**：
   - 只要你对 AI 说：*“总结我今天干了啥”*、*“总结过去 3 天”*、*“总结我这周干了啥”* 或 *“总结 2026-06-01 到 2026-06-03”*，AI 就会按指定时间范围扫描 `Literature/` 和 `Rydberg atom/` 文件夹中的新建/修改记录。
   - 它会自动在当天的 `Daily Notes/YYYY-MM-DD.md` 中追加或更新一份结构化科研汇报，分析你的阅读状态、新建/更新笔记、双链情况以及通过 LLM 深度解析的核心物理问题。

---

## 📐 顶级学术仿真：Python 实时图表

为了获得比静态图片和 Mermaid 流程图更好的科研体验，本笔记库全面采用 **Python + matplotlib** 代码块。
- 你可以直接在 Obsidian 笔记（如 `start_up.md`）中，点击由 `Obsidian Execute Code` 插件提供的一键运行按钮，在笔记内部实时渲染动力学曲线！
- **图表规范**：所有绘图均已通过 `AGENTS.md` 规范化为**纯英文学术图表**，彻底规避了 CJK 字体在沙盒中缺失而产生的乱码和 glyph warnings，且完美预防了 LaTeX 大括号在 f-string 中的插值 NameError 冲突。
