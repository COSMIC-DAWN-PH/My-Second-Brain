# Better Harness Task-Loop Report

## At a Glance

- Loop Effectiveness: 47/100 (changes only after comparable later task outcomes)
- Asset Health / Repair Progress: 0/100 (0 verified, 0 partial, 5 pending)
- Demonstrated autonomy radius: not observed (not observed; not observed confidence)
- Strongest loop: Not enough evidence difference to name one.
- Largest observed leak: Use the priority moves; no single loop is uniquely weakest.
- Top expected gain: No priority benefit is available in this evidence boundary.

## What You Can Rely On Today

- No reliable user outcome has been demonstrated in this evidence boundary yet.

## What You Gain Next

- No priority Harness move is available in this evidence boundary.



### Why these moves matter

### 绘图管线缺少自动化验证与依赖关卡
- Priority: Medium · Evidence: not observed in this boundary
- Reason: 项目中包含为笔记和讲义生成图表的 Python 脚本，但本次扫描显示 0 个测试文件、0 个 CI 配置、没有 requirements.txt 也没有 pyproject.toml。doc-audit skill 仅提供手动检查清单，因此脚本损坏、依赖缺失或 YAML frontmatter 格式错误都可能被静默提交。代理工作流只能依赖人工触发 skill 和肉眼检查。
- Expected Output:
  1. 一个可一键安装的依赖清单。
  2. 一个当绘图脚本无法运行即失败的聚焦测试。
  3. 一个下一位代理可执行的验证命令。

### 资源生成脚本修改工作区后缺少重置与校验
- Priority: Medium · Evidence: not observed in this boundary
- Reason: Handout by AI/generate_assets.py 与 Rydberg atom/attachments/*.py 会按硬编码路径向仓库写入 PNG。运行这些脚本即改变工作区，且没有任何检查来确认已提交的 PNG 与生成它们的脚本保持一致。代理可能在重新生成资源后提交，导致仓库中残留陈旧或无关的图片。
- Expected Output:
  1. 一个可确定性重新生成全部仓库资源的命令。
  2. 一个当提交 PNG 与当前脚本不一致即失败的命令。
  3. 项目规则中注明：修改绘图代码后需运行 verify-assets。

### Skill 文件命名与项目自身约定不一致
- Priority: Low · Evidence: not observed in this boundary
- Reason: AGENTS.md 与 CLAUDE.md 规定 skill 文件应命名为 SKILL.md（大写）。然而 daily-research skill 在 .claude/skills/daily-research/ 和 .agents/skills/daily-research/ 中均以 skill.md（小写）存在。此外，literature_handout skill 的文件夹名称与其 YAML frontmatter 中声明的 skill 名称 literature-handout 不一致。这些不一致在区分大小写的文件系统上可能破坏 skill 发现，也使规则集自相矛盾。
- Expected Output:
  1. 每个 skill 文件均命名为 SKILL.md。
  2. 每个 skill 文件夹与 YAML name 字段完全一致。
  3. sync-config 报告 .claude/ 与 .agents/ 之间无漂移。

### 双份规则文件依赖手动同步
- Priority: Low · Evidence: not observed in this boundary
- Reason: CLAUDE.md 与 AGENTS.md 自称为仓库规则的两份同步副本，sync-config skill 负责维护二者一致。这种手动双文件模式存在漂移风险：若只更新其中一个文件，不同代理或会话将读到相互矛盾的指令。目前没有自动化检查能阻止这种分歧。
- Expected Output:
  1. 一份权威规则文件，或一份带文档化构建步骤的生成文件。
  2. 当两份文件不同步时即失败的检查。

### 长 skill 缺少渐进式引用拆分
- Priority: Low · Evidence: not observed in this boundary
- Reason: lint 包标记 doc-audit（503 行）、learning-path（263 行）、literature_handout（314 行）、sync-config（351 行）和 zotero-notes（250 行）均没有本地 Markdown 引用。单文件 skill 长度过大会增加维护负担，也不利于高效加载到上下文。其中 doc-audit 尤其超过硬上限阈值，是整个 lint 包中唯一的 warning。
- Expected Output:
  1. 每个 SKILL.md 控制在 200 行以内。
  2. 详细流程放在同目录下的兄弟 .md 文件中，并从 SKILL.md 引用。
  3. Skill 触发条件与预期产物仍然清晰可发现。

## Five Lifecycle Dimensions

| Dimension | What the evidence proves | Evidence boundary | Summary | Boundary / blocker |
| --- | --- | --- | --- | --- |
| 任务理解 | Not observed yet | not observed in this boundary | AGENTS.md 与 CLAUDE.md 给出了清晰的仓库规范，但双文件同步规则以及 skill 名称/文件名不一致，造成了权威来源的歧义。 | not observed |
| 可控执行 | Not observed yet | not observed in this boundary | 资源脚本存在，但缺少依赖清单、doctor 命令或文档化的重置路径；同时 skill 目录存在大小写不一致。 | not observed |
| 改动验证 | Not observed yet | not observed in this boundary | doc-audit skill 提供了详尽的手动检查清单，但没有自动化测试、CI 或受影响检查路由来验证编辑。 | not observed |
| 可靠交付 | Not observed yet | not observed in this boundary | Git 历史存在且工作区干净，但缺少 PR/合并工作流或自动化恢复路径。 | not observed |
| 经验沉淀 | Not observed yet | not observed in this boundary | Skill 已配置，但缺少会话证据表明它们被调用、验证或在后续任务中提升了结果。 | not observed |

## The 15 Small Checks

| Dimension | Small check | What the evidence proves | Evidence boundary |
| --- | --- | --- | --- |


## Evidence and Boundaries

- Episode coverage: 0 episodes, 0 edited, 0 closed, 0 repaired-and-passed
- Model: agent-work-loop-v4
- Session selection: not observed; 0 sessions analyzed of 0 eligible sessions; not observed confidence
- Delivery grades observed: not observed
- Source gaps: not observed
- Learning comparison: Not observed; 0 declared intervention(s)
