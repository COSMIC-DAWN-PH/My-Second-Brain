---
aliases: []
tags:
  - Physics
  - UCAS
  - Quantum
date: 2026-03-17
status: Draft/Evergreen
---
# 中性原子阵列实验笔记

## 1. 相互作用哈密顿量
在利用里德堡原子（Rydberg atoms）进行量子计算或[[哈密顿量模拟 (Hamiltonian Simulation)]]时，多原子系统的哈密顿量可以写作：

$$
H = \sum_i \frac{\hbar \Omega}{2} \sigma_x^i - \sum_i \hbar \Delta \sigma_{ee}^i + \sum_{i<j} V_{ij} n_i n_j
$$

其中：
- $\Omega$ 是与[[拉比振荡 (Rabi Flopping)]]相关的拉比频率（Rabi frequency）。
- $\Delta$ 是激光失谐（Detuning）。
- $V_{ij}$ 是产生[[里德堡阻塞 (Rydberg Blockade)]]的范德华相互作用，其表达式为：
$$V_{ij} = \frac{C_6}{R_{ij}^6}$$

## 2. 物理假设
1. 忽略原子的自发辐射。
2. 假设原子处于[[光镊阵列 (Optical Tweezer Arrays)]]的基态。

## 3. 核心公式汇总
- **里德堡原子阵列相互作用哈密顿量**：
  $$ H = \sum_i \frac{\hbar \Omega}{2} \sigma_x^i - \sum_i \hbar \Delta \sigma_{ee}^i + \sum_{i<j} V_{ij} n_i n_j $$
- **范德华相互作用 ($V_{ij}$)**：
  $$ V_{ij} = \frac{C_6}{R_{ij}^6} $$