from collections import Counter, defaultdict
from pathlib import Path
import re

import yaml

ROOT = Path(".")
ROADMAP = ROOT / "Learning-Roadmap.md"
TODAY = "2026-09-04"

LABELS = {
    "Qubit-State-and-Superposition": "量子比特态",
    "Pauli-Matrices": "泡利矩阵",
    "Tensor-Product": "张量积",
    "Optical-Tweezer-Arrays": "光镊阵列",
    "Single-Qubit-Gates": "单量子比特门",
    "Two-Qubit-State-and-Entanglement": "双量子比特态",
    "Gate-Eigenstates": "门算符本征态",
    "Anti-Commutation": "反对易",
    "Rabi-Flopping": "拉比振荡",
    "Two-Qubit-Gates": "两量子比特门",
    "Quantum-Zeno-Effect": "量子芝诺效应",
    "AC-Stark-Effect": "AC Stark 效应",
    "CZ-Gate": "CZ门",
    "Grover-Search": "Grover 搜索",
    "Quantum-Phase-Estimation": "量子相位估计",
    "Rydberg-Blockade": "里德堡阻塞",
    "QEC": "量子纠错码",
    "Surface-Code": "表面码",
    "Transversal-Gate": "横向纠缠门",
    "Neutral_Atom_Test": "中性原子阵列实验",
    "Transversal-Teleportation": "横向隐形传态",
    "Deep-Circuit-Execution": "深度电路执行",
    "Basis-Transformation": "基变换",
    "Color-Code": "颜色码",
    "Entangling-Gate": "纠缠门",
    "Fine-Structure": "精细结构",
    "Hyperfine-Structure": "超精细结构",
    "SU2-SO3-and-Euler-Decomposition": "SU(2) 与 SO(3)",
    "Zeeman-Effect": "Zeeman 效应",
    "Adiabatic-Elimination": "绝热消去",
}

GRAPH = {
    "Qubit-State-and-Superposition": [],
    "Pauli-Matrices": ["Qubit-State-and-Superposition"],
    "Tensor-Product": ["Qubit-State-and-Superposition"],
    "Optical-Tweezer-Arrays": ["Qubit-State-and-Superposition"],
    "Single-Qubit-Gates": ["Qubit-State-and-Superposition", "Pauli-Matrices"],
    "Two-Qubit-State-and-Entanglement": ["Qubit-State-and-Superposition", "Tensor-Product"],
    "Gate-Eigenstates": ["Pauli-Matrices"],
    "Anti-Commutation": ["Pauli-Matrices", "Tensor-Product"],
    "Rabi-Flopping": ["Single-Qubit-Gates"],
    "Two-Qubit-Gates": ["Two-Qubit-State-and-Entanglement", "Tensor-Product"],
    "Quantum-Zeno-Effect": ["Single-Qubit-Gates"],
    "AC-Stark-Effect": ["Optical-Tweezer-Arrays", "Single-Qubit-Gates"],
    "CZ-Gate": ["Two-Qubit-Gates"],
    "Grover-Search": ["Single-Qubit-Gates", "Two-Qubit-Gates"],
    "Quantum-Phase-Estimation": ["Single-Qubit-Gates", "Two-Qubit-Gates"],
    "Rydberg-Blockade": ["Rabi-Flopping", "CZ-Gate"],
    "QEC": ["Two-Qubit-Gates", "CZ-Gate"],
    "Surface-Code": ["QEC"],
    "Transversal-Gate": ["QEC", "Two-Qubit-Gates"],
    "Neutral_Atom_Test": ["Rabi-Flopping", "Rydberg-Blockade", "Optical-Tweezer-Arrays"],
    "Transversal-Teleportation": ["Transversal-Gate", "Surface-Code"],
    "Deep-Circuit-Execution": ["Transversal-Teleportation"],
}

LEVEL_LABELS = {
    "understood": "✅ 已理解",
    "getting there": "🔵 基本理解",
    "vague": "🟠 模糊理解",
    "don't understand": "🔴 还不理解",
    None: "⚪ 元数据待补全",
}
LEVEL_RANK = {
    "don't understand": 0,
    "vague": 1,
    "getting there": 2,
    "understood": 3,
}
SCORE = {
    "don't understand": 1,
    "vague": 2,
    "getting there": 3,
    "understood": 4,
}


def parse_notes():
    notes = {}
    for path in sorted((ROOT / "Rydberg atom").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        frontmatter = {}
        body = text
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2]
        notes[path.stem] = {
            "frontmatter": frontmatter,
            "body": body,
            "links": set(),
        }
    known = set(notes)
    for note in notes.values():
        for raw in re.findall(r"\[\[([^\]]+)\]\]", note["body"]):
            target = raw.split("|", 1)[0].replace("\\|", "|").strip()
            target = target.split("#", 1)[0].strip().replace("\\", "/")
            if "/" in target:
                target = target.rsplit("/", 1)[-1]
            if target.endswith(".md"):
                target = target[:-3]
            if target in known:
                note["links"].add(target)
    return notes


def table_link(name):
    return f"[[{name}\\|{LABELS[name]}]]"


def normal_link(name):
    return f"[[{name}|{LABELS[name]}]]"


def render_links(names):
    return ", ".join(table_link(name) for name in names) if names else "—"


def replace_section(text, heading, next_heading, replacement):
    start = text.index(heading)
    end = text.index(next_heading, start)
    return text[:start] + replacement.rstrip() + "\n\n" + text[end:]


notes = parse_notes()
levels = {name: note["frontmatter"].get("comprehension") for name, note in notes.items()}
statuses = {name: note["frontmatter"].get("status") for name, note in notes.items()}
extra_names = [name for name in notes if name not in GRAPH]
valid_names = [name for name, level in levels.items() if level in SCORE]
valid_extra_names = [name for name in extra_names if levels[name] in SCORE]
missing_names = [name for name in notes if levels[name] not in SCORE]

children = defaultdict(list)
for name, prerequisites in GRAPH.items():
    for prerequisite in prerequisites:
        children[prerequisite].append(name)

tiers = {}
while len(tiers) < len(GRAPH):
    progress = False
    for name, prerequisites in GRAPH.items():
        if name not in tiers and all(prerequisite in tiers for prerequisite in prerequisites):
            tiers[name] = 0 if not prerequisites else max(tiers[prerequisite] for prerequisite in prerequisites) + 1
            progress = True
    if not progress:
        raise RuntimeError("canonical dependency graph contains a cycle or missing node")


def downstream_count(name):
    seen = set()
    stack = list(children[name])
    while stack:
        child = stack.pop()
        if child not in seen:
            seen.add(child)
            stack.extend(children[child])
    return len(seen)


def direct_count(name):
    return len(children[name])


def sorted_tier_members(tier):
    members = [name for name in GRAPH if tiers[name] == tier]
    return sorted(
        members,
        key=lambda name: (LEVEL_RANK.get(levels[name], 99), -downstream_count(name), name),
    )


def level_label(name):
    return LEVEL_LABELS.get(levels.get(name), "⚪ 元数据待补全")


def status_label(name):
    return statuses.get(name) or "待补全"


ROLE = {
    "Qubit-State-and-Superposition": "量子比特态、叠加态与 Bloch sphere 的根节点",
    "Pauli-Matrices": "单量子比特算符、Pauli gate 与后续门操作的基础",
    "Tensor-Product": "多量子比特 Hilbert space 的组合规则",
    "Optical-Tweezer-Arrays": "中性原子平台中用于俘获和排列原子的核心硬件",
    "Single-Qubit-Gates": "Bloch sphere 上的单比特旋转与门操作",
    "Two-Qubit-State-and-Entanglement": "Bell state、纠缠与两比特系统的状态描述",
    "Gate-Eigenstates": "理解门算符作用与测量基的基础",
    "Anti-Commutation": "Pauli 算符代数关系中的重要结构",
    "Rabi-Flopping": "单量子比特门的物理实现图像，也是 QuTiP 动力学模拟入口",
    "Two-Qubit-Gates": "CZ、CNOT 等纠缠门的统一概念入口",
    "Quantum-Zeno-Effect": "频繁测量导致演化冻结的量子效应",
    "AC-Stark-Effect": "光场导致的能级移动，是光镊与激光操控中的常见效应",
    "CZ-Gate": "Controlled-Z 门，是里德堡纠缠门与 QEC 电路的关键门",
    "Grover-Search": "量子搜索算法与振幅放大的代表例子",
    "Quantum-Phase-Estimation": "相位估计与许多量子算法的核心子程序",
    "Rydberg-Blockade": "利用强相互作用实现中性原子纠缠门的核心机制",
    "QEC": "容错量子计算和逻辑量子比特的入口",
    "Surface-Code": "重要的二维拓扑量子纠错码",
    "Transversal-Gate": "容错计算中避免错误扩散的重要门操作形式",
    "Neutral_Atom_Test": "中性原子阵列实验平台的总览型 hub note",
    "Transversal-Teleportation": "用于 fault-tolerant deep circuits 的逻辑层 teleportation 思路",
    "Deep-Circuit-Execution": "通过逻辑操作与错误清除支持深层量子电路执行",
}

TIER_TITLES = {
    0: "基础根节点",
    1: "基础算符与硬件平台",
    2: "单/双量子比特概念层",
    3: "物理动力学与原始门",
    4: "控制门与量子算法入口",
    5: "里德堡纠缠机制与 QEC 入口",
    6: "平台总览与容错编码层",
    7: "逻辑隐形传态层",
    8: "深层电路执行层",
}

counts = Counter(levels[name] for name in valid_names)
status_counts = Counter(statuses[name] for name in notes if statuses[name] is not None)
weighted = sum(SCORE[levels[name]] for name in valid_names)
weighted_pct = round(weighted / (len(valid_names) * 4) * 100)
percentages = {level: round(counts[level] / len(valid_names) * 100) for level in SCORE}
dont_count = counts["don't understand"]
dont_pct = percentages["don't understand"]

overview = [
    "## 📊 理解程度总览",
    "",
    "| 理解程度 | 数量 | 占比 | 对应笔记 |",
    "|---|---:|---:|---|",
    f"| ✅ 已理解 | {counts['understood']} | {percentages['understood']}% | {render_links(['Qubit-State-and-Superposition'])} |",
    f"| 🔵 基本理解（getting there） | {counts['getting there']} | {percentages['getting there']}% | {render_links(['Pauli-Matrices', 'Tensor-Product', 'Single-Qubit-Gates', 'Two-Qubit-State-and-Entanglement', 'Two-Qubit-Gates', 'CZ-Gate', 'Gate-Eigenstates', 'Basis-Transformation', 'Hyperfine-Structure'])} |",
    f"| 🟠 模糊理解（vague） | {counts['vague']} | {percentages['vague']}% | {render_links(['Anti-Commutation', 'Quantum-Zeno-Effect', 'Rabi-Flopping', 'QEC', 'Neutral_Atom_Test', 'Surface-Code', 'Transversal-Gate', 'SU2-SO3-and-Euler-Decomposition', 'Entangling-Gate', 'Fine-Structure', 'Zeeman-Effect', 'Color-Code'])} |",
    f"| 🔴 还不理解（don't understand） | {dont_count} | {dont_pct}% | {render_links(['Optical-Tweezer-Arrays', 'AC-Stark-Effect', 'Grover-Search', 'Quantum-Phase-Estimation', 'Rydberg-Blockade', 'Transversal-Teleportation', 'Deep-Circuit-Execution'])} |",
    f"| ⚪ 元数据待补全 | {len(missing_names)} | — | {render_links(missing_names)}（当前为空文件） |",
    "",
    f"**加权总进度**：{weighted_pct}%（计分规则：已理解=4，基本理解=3，模糊理解=2，还不理解=1；按 {len(valid_names)} 篇有效 comprehension 计算，元数据缺失文件不计分）",
    f"**扫描到的知识笔记总数**：{len(notes)} 篇（canonical graph {len(GRAPH)} 篇、graph 外有效补充笔记 {len(valid_extra_names)} 篇、元数据待补全 {len(missing_names)} 个）",
    f"**状态分布**：Evergreen {status_counts.get('Evergreen', 0)} 篇 · WIP {status_counts.get('WIP', 0)} 篇 · Draft {status_counts.get('Draft', 0)} 篇 · 元数据待补全 {len(notes) - sum(status_counts.values())} 个",
]
overview_text = "\n".join(overview)

tiers_text = [
    "## 🧱 按依赖层级排列的学习路径",
    "",
    "> 每个 Tier 只按 canonical dependency graph（主线依赖图）计算；Tier 内部按“理解程度较低优先 + 下游链条较多优先”排序。",
    "> graph 外的补充笔记不强行伪造 canonical tier，统一放在本节末尾单列。",
]
for tier in range(9):
    tiers_text.extend([
        "",
        f"### Tier {tier} - {TIER_TITLES[tier]}",
        "",
        "| 笔记 | 理解程度 | 状态 | 直接支撑 | 下游总链条 | 核心作用 |",
        "|---|---|---|---:|---:|---|",
    ])
    for name in sorted_tier_members(tier):
        tiers_text.append(
            f"| {table_link(name)} | {level_label(name)} | {status_label(name)} | {direct_count(name)} 篇 | {downstream_count(name)} 篇 | {ROLE[name]} |"
        )

supplementary_info = {
    "Basis-Transformation": ("数学补充；与 Pauli、Single-Qubit-Gates、CZ 等正文相连", "巩固基变换与相似变换，不单独占 canonical tier"),
    "SU2-SO3-and-Euler-Decomposition": ("Single-Qubit-Gates 的数学补充", "补足 Bloch sphere 旋转、Euler decomposition 与 half-angle"),
    "Entangling-Gate": ("Two-Qubit-Gates 的上位概念", "整理纠缠门定义、判据与平台实现"),
    "Fine-Structure": ("原子物理基础；连接 Hyperfine-Structure 和 Zeeman-Effect", "补强 qubit 编码相关原子结构"),
    "Hyperfine-Structure": ("Fine-Structure 到钟态编码的桥梁", "巩固 F=J+I 与钟跃迁"),
    "Zeeman-Effect": ("Hyperfine-Structure 到外场敏感性的桥梁", "巩固 clock-state 与 mF=0"),
    "Color-Code": ("Surface-Code 后的 QEC 扩展；正文已直接链接 Surface-Code", "比较三着色结构、Steane code 与横向 Clifford"),
    "Adiabatic-Elimination": ("Rydberg-Blockade 相关的预留节点", "当前为 0 字节空文件，补齐内容和 frontmatter 后再评估"),
}
tiers_text.extend([
    "",
    "### graph 外补充笔记（不改变 canonical tier）",
    "",
    "| 笔记 | 理解程度 | 状态 | 与主线关系 | 当前作用 |",
    "|---|---|---|---|---|",
])
for name in ["Basis-Transformation", "SU2-SO3-and-Euler-Decomposition", "Entangling-Gate", "Fine-Structure", "Hyperfine-Structure", "Zeeman-Effect", "Color-Code", "Adiabatic-Elimination"]:
    relation, role = supplementary_info[name]
    tiers_text.append(f"| {table_link(name)} | {level_label(name)} | {status_label(name)} | {relation} | {role} |")
tiers_text = "\n".join(tiers_text)

target_specs = [
    ("Rabi-Flopping", "⚡ **研究主线**；当前为模糊理解。先把已有二能级 Hamiltonian 推到可运行的共振/失谐动力学，作为 QuTiP 入口。", ["Single-Qubit-Gates"]),
    ("CZ-Gate", "⚡ **研究主线**；当前为基本理解。已有逻辑定义和 Rydberg 实现章节，下一步核对脉冲序列、相位与数值模型的对应关系。", ["Two-Qubit-Gates"]),
    ("Rydberg-Blockade", "⚡ **研究主线**；当前还不理解。完成 Rabi/CZ 的衔接后，补阻塞条件、阻塞半径和两原子 Hamiltonian。", ["Rabi-Flopping", "CZ-Gate"]),
    ("Optical-Tweezer-Arrays", "平台地基；当前还不理解。先建立陷阱势、原子间距和阵列构型的物理图像。", ["Qubit-State-and-Superposition"]),
    ("AC-Stark-Effect", "控制补充；当前还不理解。理解失谐驱动导致的 light shift，以及它如何进入 Rz/相位控制。", ["Optical-Tweezer-Arrays", "Single-Qubit-Gates"]),
    ("QEC", "结构主线；当前为模糊理解。两量子比特门和 CZ 已达到可进入状态，可以开始稳定子、综合测量与逻辑比特。", ["Two-Qubit-Gates", "CZ-Gate"]),
    ("Surface-Code", "QEC 后续；当前为模糊理解。先把 syndrome、码距和逻辑算符在二维格点上的对应关系讲清。", ["QEC"]),
    ("Transversal-Gate", "容错门补充；当前为模糊理解。以 QEC 和两量子比特门为前置，理解为何能抑制错误扩散。", ["QEC", "Two-Qubit-Gates"]),
    ("Neutral_Atom_Test", "平台总览；当前为模糊理解。待 Optical-Tweezer-Arrays 与 Rydberg-Blockade 的物理图像稳定后再整合。", ["Rabi-Flopping", "Rydberg-Blockade", "Optical-Tweezer-Arrays"]),
    ("Fine-Structure", "原子物理补强；当前为模糊理解。它是 Hyperfine/clock-state 讨论的桥梁，但不阻塞当前 QuTiP 主线。", []),
    ("Hyperfine-Structure", "原子物理补强；当前为基本理解。把 F=J+I、钟跃迁和 qubit 编码关系巩固到能独立复述。", ["Fine-Structure"]),
    ("Zeeman-Effect", "原子物理补强；当前为模糊理解。继续连接 mF=0 一阶不敏感与长相干时间。", ["Hyperfine-Structure"]),
    ("Color-Code", "graph 外 QEC 扩展；当前为模糊理解。放在 Surface-Code 之后比较，不改变 canonical 主线。", ["Surface-Code"]),
    ("Grover-Search", "算法练习；当前还不理解。前置门操作已基本具备，可作为振幅放大的完整例子。", ["Single-Qubit-Gates", "Two-Qubit-Gates"]),
    ("Quantum-Phase-Estimation", "算法练习；当前还不理解。前置门操作已基本具备，适合作为后续重要子程序。", ["Single-Qubit-Gates", "Two-Qubit-Gates"]),
]
targets_text = [
    "## 🎯 下一步学习建议",
    "",
    "> 推荐规则：优先选择前置知识至少达到基本理解的薄弱节点；研究主线可在不改变依赖关系的前提下提前。",
    "> 🔬 **本次更新**：延续 QuTiP 物理模拟方向，把“可写 Hamiltonian、可解释脉冲序列、可运行数值模型”放在算法练习之前。",
    "",
    "| 优先级 | 笔记 | 为什么现在学 | 前置知识 |",
    "|---:|---|---|---|",
]
for priority, (name, reason, prerequisites) in enumerate(target_specs, start=1):
    targets_text.append(f"| {priority} | {table_link(name)} | {reason} | {render_links(prerequisites)} |")
targets_text.extend([
    "",
    f"**次级巩固**：{render_links(['Anti-Commutation', 'Quantum-Zeno-Effect', 'Entangling-Gate', 'SU2-SO3-and-Euler-Decomposition'])}；它们对当前主线的 canonical 下游链条较短，可穿插复习。",
])
targets_text = "\n".join(targets_text)

bottleneck_specs = [
    ("Rabi-Flopping", "⚡ **紧急**：将现有 Hamiltonian 推导落实为共振/失谐数值实验；这是 QuTiP 模拟的第一道门。"),
    ("CZ-Gate", "⚡ **紧急**：理解逻辑 CZ 与 Rydberg 脉冲实现的接口，形成可编码的门模型。"),
    ("Rydberg-Blockade", "⚡ **紧急**：补齐阻塞条件、V=C6/R6 与两原子 Hamiltonian，解除 CZ 物理实现瓶颈。"),
    ("QEC", "QEC 的直接下游有 Surface-Code、Transversal-Gate 等；先用 CZ/两量子比特门建立 syndrome 测量图像。"),
    ("Optical-Tweezer-Arrays", "当前还不理解，但直接支撑 AC-Stark-Effect 和 Neutral_Atom_Test；先补平台物理图像。"),
    ("Two-Qubit-Gates", "直接支撑 5 个节点、下游总链条 10 个；建议把 Tensor-Product、entanglement、CZ/CNOT 串成一条线。"),
    ("Tensor-Product", "下游总链条最多（13 个）；继续巩固复合 Hilbert space、算符张量积与两原子模型。"),
    ("Two-Qubit-State-and-Entanglement", "下游总链条 11 个；补强 Bell state、纠缠判据和参数化状态，服务两比特门理解。"),
    ("Single-Qubit-Gates", "直接支撑 5 个节点、下游总链条 7 个；继续巩固 Bloch sphere 旋转与 Rabi 对应。"),
    ("Surface-Code", "直接支撑逻辑隐形传态、下游总链条 2 个；需要先把 QEC 基本概念稳定下来。"),
    ("Transversal-Gate", "直接支撑逻辑隐形传态、下游总链条 2 个；需要先连接 QEC 与两量子比特门。"),
]
bottleneck_text = [
    "## ⚠️ 瓶颈分析",
    "",
    "> 下表把“理解程度较低”且“影响较多下游概念”的节点排在前面；研究主线的紧急项会优先于单纯按链条计数的排序。",
    "",
    "| 笔记 | 理解程度 | 直接支撑 | 下游总链条 | 解锁条件/建议 |",
    "|---|---|---:|---:|---|",
]
for name, advice in bottleneck_specs:
    bottleneck_text.append(f"| {table_link(name)} | {level_label(name)} | {direct_count(name)} | {downstream_count(name)} | {advice} |")
bottleneck_text.extend([
    "",
    f"**graph 外提醒**：{table_link('Color-Code')} 是 Surface-Code 后的扩展，不计入 canonical 瓶颈；{table_link('Adiabatic-Elimination')} 当前为空文件，也不计入进度分数。",
])
bottleneck_text = "\n".join(bottleneck_text)

cross_order = list(GRAPH) + [name for name in ["Basis-Transformation", "Color-Code", "Entangling-Gate", "Fine-Structure", "Hyperfine-Structure", "SU2-SO3-and-Euler-Decomposition", "Zeeman-Effect", "Adiabatic-Elimination"] if name in notes]
cross_text = [
    "## 🔎 依赖关系交叉检查",
    "",
    "> canonical graph（主线依赖图）是学习依赖主线；正文双链只用于辅助检查。下表列出正文中额外出现的相关链接，以及 canonical 前置但正文未直接链接的节点。",
    "",
    "| 笔记 | 正文中额外出现的相关双链 | 主线前置但正文未直接链接 |",
    "|---|---|---|",
]
for name in cross_order:
    outgoing = sorted(notes[name]["links"])
    if name in GRAPH:
        extra = sorted(set(outgoing) - set(GRAPH[name]))
        missing = sorted(set(GRAPH[name]) - set(outgoing))
        missing_cell = render_links(missing)
    else:
        extra = outgoing
        missing_cell = "—（graph 外；无 canonical 前置）"
    cross_text.append(f"| {table_link(name)} | {render_links(extra)} | {missing_cell} |")
cross_text = "\n".join(cross_text)

progress_text = "\n".join([
    "## 📈 进度可视化",
    "",
    "> 当前图表包含 29 篇有有效 comprehension 的笔记；Adiabatic-Elimination 是空文件，因此不计入分数。图表内部标签按 vault 规范使用英文，以避免 matplotlib 的 CJK 字符警告。",
    "![[learning-progress-2026-09-04.png]]",
    "",
    "> 历史快照（2026-06-10）保留如下，便于比较路线变化：",
    "![[learning-progress-2026-06-10.png]]",
])

text = ROADMAP.read_text(encoding="utf-8")
text = re.sub(r"(?m)^> 最后更新：.*$", f"> 最后更新：{TODAY}（增补）", text)
text = replace_section(text, "## 📊 理解程度总览", "## 🧱 按依赖层级排列的学习路径", overview_text)
text = replace_section(text, "## 🧱 按依赖层级排列的学习路径", "## 🎯 下一步学习建议", tiers_text)
text = replace_section(text, "## 🎯 下一步学习建议", "## ⚠️ 瓶颈分析", targets_text)
text = replace_section(text, "## ⚠️ 瓶颈分析", "## 🔎 依赖关系交叉检查", bottleneck_text)
text = replace_section(text, "## 🔎 依赖关系交叉检查", "## 📈 进度可视化", cross_text)
text = replace_section(text, "## 📈 进度可视化", "## 🧩 本次增补观察", progress_text)

dont_count = counts["don't understand"]
observation = "\n".join([
    f"> [!info] {TODAY} 增补",
    "> 本次重新扫描 Rydberg atom/ 下的全部 Markdown 知识笔记，并按 canonical dependency graph 重算 Tier、下游链条、下一步目标与瓶颈。仅更新路线图和进度图，未修改任何知识笔记的 comprehension 字段。",
    "",
    "**本次变化摘要：**",
    f"- 扫描到 {len(notes)} 个 Markdown 文件：{len(GRAPH)} 个 canonical 节点、{len(valid_extra_names)} 个 graph 外有效补充笔记，以及 {len(missing_names)} 个元数据不完整文件。",
    f"- 有效 comprehension 分布为：已理解 {counts['understood']}、基本理解 {counts['getting there']}、模糊理解 {counts['vague']}、还不理解 {dont_count}；加权进度为 {weighted_pct}%。",
    f"- 新纳入路线图的 graph 外笔记是 {normal_link('Color-Code')}；它与 {normal_link('Surface-Code')} 构成 QEC 扩展关系，但暂不改动 canonical graph。",
    f"- {normal_link('Adiabatic-Elimination')} 当前为 0 字节空文件，缺少 YAML/frontmatter 和正文；已在补充笔记、交叉检查和瓶颈提醒中标注，并排除在进度分数之外。",
    f"- {normal_link('Rabi-Flopping')} 的笔记更新记录已补充 Hamiltonian 作用、共振/失谐动力学和双光子有效拉比频率，但其 comprehension 仍为 vague，因此路线图不代替用户自动升级理解等级。",
    "",
    "**对当前研究方向的影响：**",
    f"- 延续 QuTiP 物理模拟主线：{normal_link('Rabi-Flopping')} → {normal_link('CZ-Gate')} → {normal_link('Rydberg-Blockade')} 仍是最高优先级。",
    "- 先完成能写出并解释 Hamiltonian 的最小闭环，再扩展到阻塞条件、脉冲序列和两原子数值模型；Grover/QPE 保留为后续算法练习。",
])
if f"> [!info] {TODAY} 增补" not in text:
    marker = "## 🧩 本次增补观察\n"
    text = text.replace(marker, marker + "\n" + observation + "\n\n### 历史增补：2026-06-10\n", 1)

log_line = f"- {TODAY}: 增补扫描 {len(notes)} 个知识 Markdown；有效 comprehension {len(valid_names)} 篇，分布为 1/9/12/7，加权进度 {weighted_pct}%。重算 canonical Tier 与瓶颈，新增 {normal_link('Color-Code')} graph 外补充条目，标记 {normal_link('Adiabatic-Elimination')} 空文件，并生成 [[learning-progress-{TODAY}.png]]。"
log_heading = "## 📝 更新记录\n"
if log_line not in text:
    text = text.replace(log_heading, log_heading + "\n" + log_line, 1)

ROADMAP.write_text(text.rstrip() + "\n", encoding="utf-8")
print(f"Updated roadmap: {len(notes)} notes scanned; {len(valid_names)} scored; weighted progress {weighted_pct}%")
