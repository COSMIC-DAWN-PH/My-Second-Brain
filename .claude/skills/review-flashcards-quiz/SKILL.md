---
name: review-flashcards-quiz
description: "把本 vault 的中性原子量子计算笔记、论文讲义或指定复习材料整理成带闪卡、章节筛选、待复习导出和自测题的单文件 HTML；用户要求闪卡、复习卡、错题回顾或考前自测时使用。"
---

# Review Flashcards & Quiz（中性原子量子计算复习工具）

## 目标

把用户指定的复习范围转成一个放在 `Flashcards/` 下的单文件 HTML：

- **闪卡模式**：正面主动回忆、翻面看答案、章节/关键词筛选、洗牌、标记「我会了」或「再看看」。
- **出题模式**：按章节抽取计算题与概念题，显示/隐藏参考答案，自评答对/答错并统计正确率。
- **待复习导出**：把红色「再看看」卡片导出为独立 HTML，使用独立的浏览器存储命名空间。
- **物理公式**：使用 KaTeX 分隔符 `$...$` 和 `$$...$$`；模板是无后端前端工具，默认通过 CDN 加载 KaTeX。若用户明确要求完全断网使用，必须把 KaTeX 资源本地化/内嵌后再交付，不得把“无后端”误称为完全离线。

本技能只生成复习工具，不改写源知识笔记，也不代替 `literature-handout`、`zotero-notes` 或 `doc-audit` 的职责。

## 触发条件与边界

用户说“闪卡”“复习卡”“记忆卡”“做一套题”“错题回顾”“考前复习”，或要求把本 vault 的笔记/讲义/PDF 变成交互式复习工具时触发。若用户只是要求解释一篇长文或写论文讲义，不要自动使用本技能。

默认输出到 `Flashcards/`，文件名使用英文、数字和连字符，例如 `neutral-atom-qc-review-flashcards.html`；不要把生成的 HTML 放进 skill 目录，也不要创建中文文件名。

## 0. 执行前：加载上下文

1. 先读根目录 `AGENTS.md`，遵守 vault 的 UTF-8、命名、LaTeX、HTML 和安全规则。
2. 只要卡片涉及物理推导、公式或学习建议，先读 `.agents/memory/user_profile.json`，按用户实际学业阶段和已掌握前置知识调整难度；不要凭空引入超出当前学习路线的数学。
3. 用户要求“整个库”、没有明确来源，或需要选择依赖顺序时，读取 [references/vault-integration.md](references/vault-integration.md)，再动态扫描当前文件，而不是信任旧清单。
4. 不臆测外部文件路径。优先使用用户给出的路径、`<linked_note>`、编辑器选择和明确授权的目录；若只要求“整个库”，才扫描当前 vault 的规定目录。

## 1. 确定范围与来源

按以下优先级合并材料，后面的来源只用于补充和交叉核对：

1. 用户明确指定的笔记、讲义、PDF 或选中文本。
2. `Handout by AI/` 中对应的论文讲义。
3. `Rydberg atom/` 中的概念笔记（定义、推导、易错点和核心公式）。
4. `Literature Annotation/` 中的 Zotero 导入笔记；若日后出现 `Literature/`，也扫描它。
5. `Daily Notes/` 中明确记录的待解决问题、复习目标和 block reference 证据。
6. `Learning-Roadmap.md` 中的依赖层级和优先级；它只用来安排卡片顺序，不是新的物理事实来源。

当范围是整个项目时，优先按以下模块组织章节筛选，而不是把 29 篇概念笔记平铺成无意义的章节号：

1. 原子物理与 qubit 编码：`Fine-Structure`、`Hyperfine-Structure`、`Zeeman-Effect`。
2. 量子态与线性代数：`Qubit-State-and-Superposition`、`Pauli-Matrices`、`Tensor-Product`、`Basis-Transformation`、`Anti-Commutation`。
3. 单比特操控与动力学：`Single-Qubit-Gates`、`Rabi-Flopping`、`AC-Stark-Effect`、`SU2-SO3-and-Euler-Decomposition`、`Gate-Eigenstates`。
4. 双比特态与纠缠门：`Two-Qubit-State-and-Entanglement`、`Two-Qubit-Gates`、`Entangling-Gate`、`CZ-Gate`。
5. 中性原子平台：`Optical-Tweezer-Arrays`、`Rydberg-Blockade`、`Neutral_Atom_Test`、`Adiabatic-Elimination`。
6. QEC 与容错执行：`QEC`、`Surface-Code`、`Color-Code`、`Transversal-Gate`、`Transversal-Teleportation`、`Deep-Circuit-Execution`。
7. 算法入口：`Grover-Search`、`Quantum-Phase-Estimation`。
8. 文献路线与实验案例：相关 `Handout by AI/` 讲义和 `Literature Annotation/` 条目。

以上只是当前 vault 的默认分组；如果用户指定了课程章节、论文章节或单个知识点，以用户范围为准，并保留可追溯的源笔记名称和章节标题。

## 2. 提取卡片和题目

### 卡片 `cards`

每张卡只测试一个可独立回忆的知识单元，使用以下字段：

```json
{
  "id": "rydberg-blockade.blockade-radius",
  "ch": 5,
  "diff": 1,
  "q": "阻塞半径的物理定义是什么？",
  "a": "要点……\n\n$$R_b = ...$$",
  "source": "Rydberg-Blockade §2.4"
}
```

- `id`：稳定、唯一的英文短 ID；不要使用会随洗牌或删卡而变化的数组下标。
- `ch`：整数章节键，必须在章节字典中存在。
- `diff`：`1` 表示核心必掌握，`0` 表示普通巩固。
- `q`：正面主动回忆问题；不要在问题里泄露答案或把整条公式直接抄出来。
- `a`：背面答案。先给物理图像，再给公式/推导/应用和易错点；必要时用换行分层。
- `source`：可选的可读来源标记，格式建议为 `File §N 标题关键词`，HTML 不把 `[[...]]` 当作 Obsidian 链接解析。

物理卡片的覆盖原则：

- 覆盖每个范围内的核心定义、变量含义、关键公式、推导关键步、边界条件、常见混淆和与中性原子平台的联系。
- 长推导拆成“前提 → 一步变形 → 物理解释 → 结论”多张卡，避免一张卡塞入整页讲义。
- 公式必须可从卡片答案独立理解；例如解释 $Δ$、$Ω$、$V$、$C_6$、$R_b$ 的物理含义和单位，不只贴最终式。
- 使用用户画像控制深度：对本科阶段优先补齐线性代数、二能级动力学、原子物理和门操作的中间步骤；不要无理由跳到高阶场论或复杂数值方法。

### 题目 `quiz`

```json
{
  "id": 501,
  "ch": 5,
  "type": "calc",
  "q": "给定……，计算阻塞半径并说明近似条件。",
  "a": "第一步……\n第二步……\n所以……",
  "source": "Rydberg-Blockade §2.4"
}
```

- `id`：唯一正整数；模板用它保存答题成绩。
- `type`：只能是 `calc`（计算/推导）或 `concept`（概念辨析）。
- 题干必须写清已知量、求解目标、单位和必要近似；答案要给关键步骤、数量级/有效数字和单位。
- 每个有数学内容的章节默认至少有 1 道计算题和 1 道概念题；若材料没有可靠数值，不要编造实验参数，可出符号推导或机制辨析题。
- 题目应覆盖应用能力，不要把卡片答案原句换个问号就当作题目。

### 真实性与理解进度

- `comprehension` 可以读取来决定哪些章节需要更多基础卡、更多自测题，但**绝不修改、升级、推测后回写**该字段，也不把它伪装成“已掌握”标记。
- 初始 HTML 不自动把任何卡片标成绿色或红色；“我会了/再看看”只由用户在浏览器中操作。
- 不能从 `status`、日记或 AI 推测替用户宣称某知识点已经学会。文献中的实验数字、公式和结论必须能回溯到源笔记；不确定处标成待核对，而不是编造。

## 3. 生成 HTML

模板位于 [assets/template.html](assets/template.html)，构建脚本位于 [scripts/build_flashcards.py](scripts/build_flashcards.py)。推荐把章节、卡片和题目先写成临时 UTF-8 JSON，再运行：

```powershell
python .agents/skills/review-flashcards-quiz/scripts/build_flashcards.py `
  --topic "Neutral Atom Quantum Computing" `
  --source "Rydberg atom/; Handout by AI/; Learning-Roadmap.md" `
  --chapters chapters.json `
  --cards cards.json `
  --quiz quiz.json `
  --output "Flashcards/neutral-atom-qc-review-flashcards.html" `
  --namespace "neutral-atom-qc"
```

脚本会安全地把 JSON 编码成 JavaScript 数据，创建输出父目录，并默认拒绝覆盖已有文件；只有用户明确要更新旧 deck 时才使用 `--force`。也可以手动复制模板，但必须替换 `DECK` 数据块的全部占位符：`TOPIC_NAME_JSON`、`SOURCE_NOTE_JSON`、`STORAGE_NAMESPACE_JSON`、`CHAPTERS_JSON`、`CARDS_JSON`、`QUIZ_JSON`。

生成时保持以下不变量：

- 每个 deck 使用独立的 `namespace`，不能让不同课程共享 localStorage 进度。
- 导出的待复习 HTML 必须重新注入数据、保留 `<!DOCTYPE html>`，并使用 `<namespace>::review` 隔离进度。
- 不能把 HTML 放在 `.agents/skills/...` 或 `.claude/skills/...`；这些目录只保存 skill 和模板。
- 模板的 `<meta charset="UTF-8">`、英文/ASCII 的脆弱符号写法和 KaTeX 分隔符不能被删除。数据中的反斜杠由脚本 JSON 编码处理，不要手动把 `\\epsilon` 变成裸 `\epsilon`。

## 4. 交付前验证

先做静态验证：

```powershell
python .agents/skills/review-flashcards-quiz/scripts/validate_flashcards.py `
  "Flashcards/neutral-atom-qc-review-flashcards.html"
```

然后在浏览器中打开最终 HTML（可用 in-app Browser、系统浏览器或 Playwright），至少检查：

- 闪卡可翻面，空格与方向键工作，章节筛选/搜索/洗牌工作。
- 「我会了」「再看看」会刷新统计；「仅待复习」只显示红标卡片。
- 无红标时导出会提示；有红标时导出的文件只含红标卡片，标题含数量，且能独立保存进度。
- 出题模式支持抽 10/20 道、显示/隐藏答案、自评、正确率和重置。
- KaTeX 已渲染，没有裸露 `$...$`、`$$...$$`、`\\epsilon` 或乱码模式；导出文件含 `<!DOCTYPE html>`。
- 刷新页面后进度仍在，深色模式下文本和公式可读。

浏览器检查不得污染用户已有 deck 的进度；必要时用临时文件名或临时浏览器 profile。若没有可用浏览器，只能报告“已完成静态验证，未完成交互验证”，不能声称全部通过。

## 5. 与 vault 的协作边界

- 只写 `Flashcards/` 下用户要求的 HTML，以及构建过程中明确要求保留的输入 JSON；默认不改 `Rydberg atom/`、`Handout by AI/`、`Literature Annotation/`、`Daily Notes/` 或 `Learning-Roadmap.md`。
- 不为生成闪卡而新增知识笔记、修改 `comprehension`、伪造 block reference 或更新学习路线图。
- 若用户随后要求把错题反馈写回知识库，另行确认目标笔记和修改范围；那是一次新的笔记编辑任务。
- 修改本 skill、模板或脚本时，同时更新 `.agents/skills/review-flashcards-quiz/` 与 `.claude/skills/review-flashcards-quiz/`，保持文件内容一致；如需变更规则索引，也同步更新 `AGENTS.md` 和 `CLAUDE.md`。

## 参考资源

- [references/vault-integration.md](references/vault-integration.md)：当前 vault 的目录映射、概念模块和复习优先级读取方式。
- [assets/template.html](assets/template.html)：通用单文件 HTML 模板，只填充 `DECK` 数据。
- [scripts/build_flashcards.py](scripts/build_flashcards.py)：从 UTF-8 JSON 构建 deck，避免手写 JavaScript 转义错误。
- [scripts/validate_flashcards.py](scripts/validate_flashcards.py)：检查 HTML、占位符、数据结构、DOCTYPE、编码和 JavaScript 语法。
