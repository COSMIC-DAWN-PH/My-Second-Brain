---
aliases:
  - 导师进度汇报 2026-08 至 2026-10
  - Progress Report Aug-Oct 2026
tags:
  - Meta
  - Report
  - AdvisorMeeting
date: 2026-10-09
status: Draft
type: report
---

# 📑 学习进度汇报（2026.08 – 2026.10）

> 主线任务：精读 Dolev Bluvstein 博士论文 *Error-corrected quantum processing with neutral atoms* (2025)，边读边补基础、边做数值模拟复现论文中的关键物理。
>
> **目前进度：论文主体已读完约 3/4**——平台、纠缠门、可重构阵列部分已完整读完并做了配套模拟；纠错实验部分读完了逻辑比特编码与横向逻辑门，正在读深度电路执行章节。
>
> 所有模拟代码见 `Advisor-Report/code/`（Python + QuTiP，均可直接运行）。

---

## 一、8 月（上）：论文第 1–2 章 —— 中性原子平台与量子比特操控

**读的内容：**

- 中性原子量子计算总览：为什么中性原子平台适合规模化（天然全同、易扩展、可重构）
- ⁸⁷Rb 的能级结构：精细结构、超精细结构，用超精细基态钟态（clock states）$|F=1,m_F=0\rangle$、$|F=2,m_F=0\rangle$ 编码量子比特，一阶磁场不敏感、相干时间秒级
- 光镊俘获与 AC Stark 效应：偶极力正比于 $I/\Delta$
- 单比特操控：微波/拉曼双光子跃迁驱动 Rabi 振荡；失谐情形的广义 Rabi 频率 $\Omega_{\rm eff}=\sqrt{\Omega^2+\Delta^2}$

**补的基础：** 量子比特与 Bloch 球、Pauli 矩阵、张量积、单/双比特门语言（[[Qubit-State-and-Superposition]]、[[Pauli-Matrices]]、[[Tensor-Product]]、[[Single-Qubit-Gates]]）；原子物理三件套（[[Fine-Structure]]、[[Hyperfine-Structure]]、[[Zeeman-Effect]]）

**配套代码：**

- `code/rabi_oscillations.py` — 共振/失谐 Rabi 振荡复现
- `code/rabi_freq_vs_intensity.py` — $\Omega\propto\sqrt{I}$ 标定曲线与 $\pi$ 脉冲时长

---

## 二、8 月（下）：论文第 3 章 —— 里德堡纠缠门

**读的内容：**

- 里德堡阻塞机制：$V(R)=C_6/R^6$，$C_6\propto n^{11}$，阻塞条件 $V\gg\Omega$，阻塞半径 $R_b=(C_6/\Omega)^{1/6}$
- CZ 门的脉冲实现：$\pi$–$2\pi$–$\pi$ 序列的分步物理图像，$|11\rangle$ 积累 $\pi$ 相位的来源
- 时间最优单脉冲门与暗态选择（dark branch selection）：更短门时间、更高鲁棒性（配合研读了 [[2023-parallel-gates-handout]] 讲义）
- 门保真度现状 ~99.5%，误差来源分解：里德堡态衰减、激光失谐/强度噪声、阻塞不完全

**配套代码（本阶段核心成果）：**

| 文件 | 内容 | 关键结果 |
|---|---|---|
| `code/qutip_rydberg_cz.py` | QuTiP 双原子 CZ 门全程模拟（$V/\Omega=40$） | $\vert 11\rangle$ 布居完整回归 1.0000，$\vert rr\rangle$ 泄漏峰值仅 $6\times10^{-4}$ |
| `code/blockade_potential.py` | 阻塞势与阻塞半径可视化 | 图示 blockaded region |
| `code/blockade_suppression_scan.py` | 扫 $V/\Omega$ 验证双激发抑制 | 数值确认 $P_{rr}\sim(\Omega/V)^2$ 标度 |
| `code/fidelity_noise_scan.py` | 门误差预算三项对比（失谐/衰减/阻塞） | 判断各噪声主导区间 |

---

## 三、9 月：论文第 4 章 —— 可重构原子阵列架构

**读的内容：**

- SLM 生成静态任意几何阵列 + AOD 动态移动行列；装载随机性（~50%）与重排（rearrangement）算法
- 分区架构：存储区 / 纠缠区 / 读出区分离，原子在区间穿梭完成电路
- 中途测量（mid-circuit measurement）与实时反馈（feedforward）：读出辅助比特而不干扰数据比特
- 核心认识：**可重构性 = 连接性不受近邻限制**，这是中性原子做纠错相对超导平台的根本优势

---

## 四、9 月下旬 – 10 月初：论文第 5 章（前半）—— 逻辑量子比特与横向门

**读的内容：**

- QEC 框架：逻辑比特、稳定子测量、错误症候、码距 $d$ 与可纠正错误数 $t=\lfloor(d-1)/2\rfloor$
- 表面码 vs 色码：[[7,1,3]] Steane/色码的全部 Clifford 门可横向实现
- 横向门容错原理 + Eastin-Knill 定理的限制
- 论文标志性实验：百原子阵列上编码 48 个逻辑比特、用原子移动实现逻辑比特间横向纠缠门、逻辑线路保真度超越物理线路——"纠错的净收益"

**目前读到：** 逻辑比特实验章节末，正进入**深度电路执行**章节（逻辑隐形传态、逐层纠错循环）。

---

## 五、代码成果总览

| 代码 | 论文章节 | 物理内容 |
|---|---|---|
| `code/rabi_oscillations.py` | Ch.2 | 共振/失谐 Rabi 振荡 |
| `code/rabi_freq_vs_intensity.py` | Ch.2 | $\Omega\propto\sqrt{I}$ 标定 |
| `code/blockade_potential.py` | Ch.3 | 阻塞势与阻塞半径 |
| `code/qutip_rydberg_cz.py` | Ch.3 | CZ 门 QuTiP 全程模拟 |
| `code/blockade_suppression_scan.py` | Ch.3 | 阻塞抑制标度验证 |
| `code/fidelity_noise_scan.py` | Ch.3 | 门误差预算分析 |

Python 3 + NumPy/Matplotlib/QuTiP，全部运行验证通过。

---

## 六、下一步计划摘要

继续读完论文剩余 1/4（深度电路执行 + 展望），同时把 CZ 模拟从幺正演化升级到含耗散的主方程层面，定量复现"保真度 vs 衰减率"曲线。详见 [[Next-Week-Plan-2026-10-12]]。

## 📝 更新记录

- 2026-10-09: 初始创建
