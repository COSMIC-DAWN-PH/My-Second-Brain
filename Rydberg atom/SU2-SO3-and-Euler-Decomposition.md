---
aliases:
  - SU2 SO3 and Euler Decomposition
  - SU(2) 与 SO(3)
  - 欧拉分解
  - Euler Decomposition
  - Single-Qubit Euler Decomposition
  - Half Angle
  - 双覆盖
tags:
  - Physics
  - Quantum
  - Mathematics
  - LinearAlgebra
  - Gates
  - BlochSphere
date: 2026-06-03
status: WIP
source: "[[Single-Qubit-Gates]]"
comprehension: "vague"
---

# SU(2)、SO(3) 与 Euler 分解

> 来源：从 [[Single-Qubit-Gates|单量子比特门]] 的 Euler 分解段落拆出的数学铺垫。目标是解释：为什么任意单比特门可以写成 $R_z R_y R_z$，为什么旋转公式里总是出现 $\theta/2$，以及这件事如何连接到 Bloch 球上的真实三维旋转。

---

## 1. 先说结论：这套数学在解决什么问题？

单比特门的数学对象是一个 $2\times2$ 酉矩阵 $U$。实验中我们更愿意把它理解成“让 Bloch 球上的量子态绕某根轴旋转”。这两种语言之间的桥梁就是：

$$
U(2) \quad \longrightarrow \quad SU(2) \quad \longrightarrow \quad SO(3).
$$

它们分别表示：

| 对象 | 直觉含义 | 在单比特门中的角色 |
|---|---|---|
| $U(2)$ | 所有 $2\times2$ 酉矩阵 | 最一般的单比特门，包含全局相位 |
| $SU(2)$ | 行列式为 $1$ 的特殊酉矩阵 | 去掉全局相位后的真正单比特操作 |
| $SO(3)$ | 三维空间中的旋转 | Bloch 球上看到的旋转 |

> [!tip] 一句话记忆
> **$U(2)$ 是量子电路里的矩阵语言；$SO(3)$ 是 Bloch 球上的几何语言；$SU(2)$ 是把两者连接起来的中间层。**

---

## 2. 数学铺垫一：为什么单比特门必须是酉矩阵？

一个 qubit 态写作

$$
\vert\psi\rangle=\alpha\vert0\rangle+\beta\vert1\rangle,
\quad |\alpha|^2+|\beta|^2=1.
$$

矩阵 $U$ 作用后得到

$$
\vert\psi'\rangle=U\vert\psi\rangle.
$$

为了让演化后仍然是合法量子态，必须保持范数：

$$
\langle\psi'\vert\psi'\rangle=\langle\psi\vert\psi\rangle.
$$

把 $\vert\psi'\rangle=U\vert\psi\rangle$ 代进去：

$$
\langle\psi'\vert\psi'\rangle
=\left(U\vert\psi\rangle\right)^\dagger\left(U\vert\psi\rangle\right)
=\langle\psi\vert U^\dagger U\vert\psi\rangle.
$$

如果对任意 $\vert\psi\rangle$ 都要保持范数，就必须有

$$
U^\dagger U=I.
$$

这就是酉矩阵的定义。

> [!info] 物理含义
> 酉性不是抽象数学限制，而是“总概率不能凭空增加或消失”的表达。单比特门之所以可逆，也是因为酉矩阵一定存在逆矩阵 $U^{-1}=U^\dagger$。

---

## 3. 数学铺垫二：全局相位为什么可以先拿掉？

任意 $U\in U(2)$ 的行列式满足

$$
|\det U|=1,
$$

所以可以写成

$$
\det U=e^{i\chi}.
$$

令

$$
\alpha=\frac{\chi}{2},
\quad
V=e^{-i\alpha}U.
$$

那么

$$
\det V=\det(e^{-i\alpha}U)=e^{-2i\alpha}\det U=e^{-i\chi}e^{i\chi}=1.
$$

于是 $V\in SU(2)$，而原来的门可以写成

$$
U=e^{i\alpha}V.
$$

这里 $e^{i\alpha}$ 是全局相位。对单个态来说，

$$
\vert\psi\rangle \quad \text{和} \quad e^{i\alpha}\vert\psi\rangle
$$

给出相同的测量概率，因为

$$
|e^{i\alpha}\alpha_0|^2=|\alpha_0|^2,
\quad
|e^{i\alpha}\alpha_1|^2=|\alpha_1|^2.
$$

> [!warning] 不要把全局相位和相对相位混淆
> 全局相位是整个态一起乘上 $e^{i\alpha}$；相对相位是 $\vert0\rangle$ 和 $\vert1\rangle$ 两个分量之间多出来的相位差。全局相位通常不可观测，但相对相位会影响干涉，是量子计算真正使用的资源。

---

## 4. 数学铺垫三：Pauli 矩阵为什么是旋转生成元？

三 Pauli 矩阵见 [[Pauli-Matrices]]：

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

给定单位方向

$$
\hat n=(n_x,n_y,n_z),
$$

定义

$$
\hat n\cdot\vec\sigma=n_xX+n_yY+n_zZ.
$$

由于 Pauli 矩阵满足代数关系，可以证明

$$
(\hat n\cdot\vec\sigma)^2=I.
$$

这一步非常关键。因为如果一个矩阵 $A$ 满足 $A^2=I$，那么指数函数可以直接展开：

$$
e^{-i\frac{\theta}{2}A}
=I\cos\frac{\theta}{2}-iA\sin\frac{\theta}{2}.
$$

所以定义单比特旋转门：

$$
R_{\hat n}(\theta)=e^{-i\frac{\theta}{2}(\hat n\cdot\vec\sigma)}
=I\cos\frac{\theta}{2}-i(\hat n\cdot\vec\sigma)\sin\frac{\theta}{2}.
$$

> [!tip] 直觉
> Pauli 矩阵不是“随便写出来的三个矩阵”。它们在单比特 Hilbert space 中扮演三维空间 $x,y,z$ 旋转轴的角色。绕哪根轴转，就把对应的 Pauli 矩阵放进指数里。

---

## 5. 为什么是 half-angle：$\theta/2$ 从哪里来？

Bloch 球上任意纯态可以写成

$$
\vert\psi\rangle=
\cos\frac{\theta}{2}\vert0\rangle
+e^{i\phi}\sin\frac{\theta}{2}\vert1\rangle.
$$

注意这里不是 $\cos\theta$ 和 $\sin\theta$，而是 $\cos(\theta/2)$ 和 $\sin(\theta/2)$。

从测量概率看：

$$
P(0)=\cos^2\frac{\theta}{2},
\quad
P(1)=\sin^2\frac{\theta}{2}.
$$

当 Bloch 球从北极走到南极时，几何角度是

$$
\theta:0\to\pi,
$$

但 Hilbert space 中的振幅角只走了

$$
\frac{\theta}{2}:0\to\frac{\pi}{2}.
$$

这就是 half-angle 的直接来源。

> [!example] 从 $\vert0\rangle$ 到 $\vert1\rangle$
> Bloch 球上 $\vert0\rangle$ 和 $\vert1\rangle$ 是南北两极，夹角是 $\pi$。但态矢量写法里，$\vert0\rangle$ 的系数从 $1$ 变到 $0$，$\vert1\rangle$ 的系数从 $0$ 变到 $1$，对应的是 $\cos(0)\to\cos(\pi/2)$ 与 $\sin(0)\to\sin(\pi/2)$。

下面这段 Python 图展示 $P(0)$ 和 $P(1)$ 如何随 Bloch 角 $\theta$ 改变。

```python
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, np.pi, 400)
p0 = np.cos(theta / 2) ** 2
p1 = np.sin(theta / 2) ** 2

plt.figure(figsize=(8, 4.5))
plt.plot(theta / np.pi, p0, lw=2.5, label=r'$P_0=\cos^2(\theta/2)$')
plt.plot(theta / np.pi, p1, lw=2.5, label=r'$P_1=\sin^2(\theta/2)$')
plt.axvline(0.5, color='gray', lw=1.2, ls=':', label=r'$\theta=\pi/2$')
plt.xlabel(r'Bloch Rotation Angle $\theta/\pi$')
plt.ylabel('Measurement Probability')
plt.title('Half-Angle Probability Flow on the Bloch Sphere')
plt.grid(alpha=0.3, ls=':')
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
```

---

## 6. SU(2) 到 SO(3)：为什么说它是“双覆盖”？

$SO(3)$ 描述普通三维空间中的旋转。一个 Bloch 向量可以写成

$$
\vec r=(\langle X\rangle,\langle Y\rangle,\langle Z\rangle).
$$

当态受到 $U\in SU(2)$ 作用时，Bloch 向量会按照某个 $SO(3)$ 旋转矩阵 $R$ 变化：

$$
\vec r\longrightarrow R\vec r.
$$

关键点是：

$$
U \quad \text{和} \quad -U
$$

在 Bloch 球上对应**同一个三维旋转**。

因为态矢量整体多一个负号只是全局相位 $e^{i\pi}$，不会改变 Bloch 向量和测量概率。所以从 $SU(2)$ 到 $SO(3)$ 的映射是二对一的：

$$
SU(2)\to SO(3) \quad \text{is a double cover}. 
$$

> [!warning] 重要反直觉点
> 自旋 $1/2$ 系统转 $2\pi$ 后，态矢量会变成 $-\vert\psi\rangle$；要转 $4\pi$ 才回到完全相同的态矢量。Bloch 球上看起来 $2\pi$ 已经回来了，但 Hilbert space 里还差一个全局负号。

---

## 7. Euler 分解的完整形式

现在回到单比特门。去掉全局相位后，任意 $V\in SU(2)$ 都可以写成

$$
V=R_z(\beta)R_y(\gamma)R_z(\delta).
$$

因此任意 $U\in U(2)$ 都可以写成

$$
U=e^{i\alpha}R_z(\beta)R_y(\gamma)R_z(\delta).
$$

这就是单比特门的 Euler 分解。

> [!tip] 物理图像
> $R_z$ 改变相位方向，$R_y$ 改变 Bloch 球纬度，最后一个 $R_z$ 修正最终相位。三步组合起来，就能覆盖所有可能的单比特旋转。

---

## 8. 逐步推导：为什么 $R_zR_yR_z$ 能覆盖任意 $SU(2)$？

先写出两个基本旋转：

$$
R_z(\theta)=
\begin{pmatrix}
e^{-i\theta/2}&0\\
0&e^{i\theta/2}
\end{pmatrix},
$$

$$
R_y(\theta)=
\begin{pmatrix}
\cos\frac{\theta}{2}&-\sin\frac{\theta}{2}\\
\sin\frac{\theta}{2}&\cos\frac{\theta}{2}
\end{pmatrix}.
$$

计算乘积：

$$
R_z(\beta)R_y(\gamma)R_z(\delta)
=
\begin{pmatrix}
\cos\frac{\gamma}{2}e^{-i(\beta+\delta)/2}
&
-\sin\frac{\gamma}{2}e^{-i(\beta-\delta)/2}
\\
\sin\frac{\gamma}{2}e^{i(\beta-\delta)/2}
&
\cos\frac{\gamma}{2}e^{i(\beta+\delta)/2}
\end{pmatrix}.
$$

另一方面，任意 $SU(2)$ 矩阵都可以写成

$$
V=
\begin{pmatrix}
a&b\\
-b^*&a^*
\end{pmatrix},
\quad
|a|^2+|b|^2=1.
$$

比较两者：

$$
|a|=\cos\frac{\gamma}{2},
\quad
|b|=\sin\frac{\gamma}{2}.
$$

因此可以先确定

$$
\gamma=2\arctan2(|b|,|a|).
$$

再用 $a$ 和 $b$ 的复相位确定 $\beta$ 与 $\delta$。这说明三个角度 $\beta,\gamma,\delta$ 足以覆盖任意 $SU(2)$ 矩阵。

> [!info] 为什么自由度刚好对上？
> 一个一般 $2\times2$ 复矩阵有 $8$ 个实参数。酉条件 $U^\dagger U=I$ 施加 $4$ 个实约束，所以 $U(2)$ 剩 $4$ 个自由度。去掉全局相位后，$SU(2)$ 剩 $3$ 个自由度，刚好由三个 Euler angles 表示。

---

## 9. 从矩阵反推出 Euler angles 的实用步骤

如果你手里有一个目标门 $U$，想把它拆成 $R_zR_yR_z$，可以按下面做：

1. **先去掉全局相位**  
   计算 $\det U=e^{i\chi}$，取 $\alpha=\chi/2$，令
   $$
   V=e^{-i\alpha}U.
   $$

2. **把 $V$ 写成标准 $SU(2)$ 形式**  
   $$
   V=\begin{pmatrix}a&b\\-b^*&a^*\end{pmatrix}.
   $$

3. **由模长确定中间角**  
   $$
   \gamma=2\arctan2(|b|,|a|).
   $$

4. **由复相位确定前后两个 $z$ 旋转**  
   若 $a$ 和 $b$ 都不为零，令
   $$
   p=\arg(a),\quad q=\arg(-b),
   $$
   则可以取
   $$
   \beta=-(p+q),\quad \delta=q-p,
   $$
   角度按 $2\pi$ 周期理解。

> [!warning] 退化情况
> 当 $\gamma=0$ 或 $\gamma=\pi$ 时，某些相位信息会合并，Euler angles 不唯一。这不是物理问题，而是坐标参数化本身的“极点退化”，类似地球南北极处经度不唯一。

---

## 10. 和中性原子单比特门的关系

在中性原子平台中，单比特门通常来自两能级系统的受驱演化。有效哈密顿量常写成

$$
H_{\text{eff}}=\frac{1}{2}\left(\Omega_x X+\Omega_y Y+\Delta Z\right),
$$

于是时间演化为

$$
U(t)=e^{-iH_{\text{eff}}t}.
$$

如果把

$$
\vec\Omega=(\Omega_x,\Omega_y,\Delta),
\quad
\Omega_{\text{tot}}=|\vec\Omega|,
\quad
\hat n=\frac{\vec\Omega}{\Omega_{\text{tot}}},
$$

则

$$
U(t)=e^{-i\frac{\Omega_{\text{tot}}t}{2}(\hat n\cdot\vec\sigma)}=R_{\hat n}(\Omega_{\text{tot}}t).
$$

这把实验参数直接翻译成旋转门：

| 实验参数 | 数学角色 | 物理效果 |
|---|---|---|
| 脉冲时长 $t$ | 控制 $\theta=\Omega_{\text{tot}}t$ | 决定转多少角度 |
| 驱动相位 | 控制 $x$-$y$ 平面旋转轴 | 决定做 $R_x$、$R_y$ 或它们的组合 |
| 失谐 $\Delta$ | 引入 $Z$ 分量 | 产生相位旋转或 AC Stark shift |

因此 Euler 分解不是纸面数学，而是硬件编译规则：

$$
\text{desired unitary}
\to
\text{Euler angles}
\to
\text{pulse sequence}.
$$

---

## 11. 常见误区

> [!danger] 误区一：把 $SU(2)$ 和 $SO(3)$ 当成完全一样
> 它们不是同一个群。$SU(2)$ 是量子态矢量上的操作，$SO(3)$ 是 Bloch 向量上的旋转。两者通过二对一映射联系起来，所以会出现 half-angle 和 $2\pi$ 转动变号。

> [!warning] 误区二：认为全局相位永远可以随便丢
> 在单个封闭量子态的测量概率中，全局相位不可观测。但在受控操作、路径干涉、或把某个子空间嵌入更大 Hilbert space 时，原本看似“全局”的相位可能变成相对相位。做电路等价变换时要看清上下文。

> [!warning] 误区三：把 Euler 分解理解成唯一实验方案
> $R_zR_yR_z$ 只是一种常用坐标选择。也可以用 $R_xR_zR_x$、$R_zR_xR_z$ 等形式。真正重要的是：少数基本旋转可以生成全部单比特门。

---

## 12. 和其他笔记的连接

- [[Single-Qubit-Gates]]：本笔记服务的主线笔记，解释单比特门的物理直觉与标准门。
- [[Pauli-Matrices]]：理解 $X,Y,Z$ 为什么是旋转生成元的必要前置。
- [[Qubit-State-and-Superposition]]：理解 Bloch 球参数化、相位因子和 half-angle 的前置。
- [[Rabi-Flopping]]：把旋转角 $\theta=\Omega t$ 与实验脉冲联系起来。
- [[AC-Stark-Effect]]：理解失谐和光移如何产生有效 $Z$ 相位旋转。

---

## 📐 核心公式摘要

| 公式 | 含义 |
|---|---|
| $U^\dagger U=I$ | 单比特门必须保持概率归一化 |
| $U=e^{i\alpha}V,\;V\in SU(2)$ | 任意单比特门 = 全局相位 × 特殊酉矩阵 |
| $R_{\hat n}(\theta)=e^{-i\frac{\theta}{2}(\hat n\cdot\vec\sigma)}$ | 绕 $\hat n$ 轴的单比特旋转 |
| $R_{\hat n}(\theta)=I\cos\frac{\theta}{2}-i(\hat n\cdot\vec\sigma)\sin\frac{\theta}{2}$ | 利用 $(\hat n\cdot\vec\sigma)^2=I$ 展开的旋转公式 |
| $\vert\psi\rangle=\cos\frac{\theta}{2}\vert0\rangle+e^{i\phi}\sin\frac{\theta}{2}\vert1\rangle$ | Bloch 球纯态参数化 |
| $U=e^{i\alpha}R_z(\beta)R_y(\gamma)R_z(\delta)$ | 任意单比特门的 Euler 分解 |

---

## 📝 更新记录

- 2026-06-03: 初始创建，作为 [[Single-Qubit-Gates]] 中 Euler 分解段落的数学铺垫。
