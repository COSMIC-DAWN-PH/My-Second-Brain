---
citekey: {{citeKey}}
title: "{{title}}"
authors: {{authors}}
tags: [Reference, Physics, Quantum]
year: {{date | format("YYYY")}}
---

# {{title}}

## 📖 摘要
{{abstractNote}}

{% if notes.length > 0 -%}
## 📝 Zotero 笔记 (Better Notes)
{% for note in notes -%}
{{note.note}}
{%- endfor %}
{%- endif %}

## 🖋️ PDF 批注
{% for annotation in annotations -%}
{% if annotation.annotatedText -%}
> {{annotation.annotatedText}} [p.{{annotation.pageLabel}}](zotero://select/library/items/{{itemKey}})
{%- endif %}

{% if annotation.comment %}
**我的评价**：{{annotation.comment}}
{%- endif %}
{%- endfor %}