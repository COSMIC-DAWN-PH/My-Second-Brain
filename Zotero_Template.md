---
citekey: {{citeKey}}
title: "{{title}}"
authors: {{authors}}
tags: [Reference, Physics, Quantum]
year: {{date | format("YYYY")}}
status: Draft
---
# {{title}}

## 📖 摘要
{{abstractNote}}

## 🖋️ PDF 批注
{% for annotation in annotations -%}
{% if annotation.annotatedText -%}
> {{annotation.annotatedText}} [p.{{annotation.pageLabel}}](zotero://select/library/items/{{itemKey}})
{%- endif %}

{% if annotation.comment %}
**我的笔记**：{{annotation.comment}}
{%- endif %}
{%- endfor %}

---
## 💡 AI 助理建议 (physics-manager Skill)
> **Agent 任务**：请根据以上批注，完成以下结构化评述：
>
> 1. 🔬 **实验方法**：该文献采用了哪些核心实验或数值方法？
> 2. 📐 **关键公式/模型**：列出最重要的物理模型或公式，并用 LaTeX 规范格式呈现。
> 3. 💡 **创新点**：该研究在 **Rydberg Blockade / 中性原子量子计算** 领域的主要贡献是什么？
> 4. ❓ **待深入问题**：基于此文献，列出 1-2 个值得进一步探究的开放问题。
> 5. 🔗 **知识关联**：自动识别关键词并建立 `[[双链]]`（如 `[[里德堡阻塞]]`、`[[光镊阵列]]`）。