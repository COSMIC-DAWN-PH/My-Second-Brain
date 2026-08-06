<!-- learning-path canonical 依赖图（从 SKILL.md 拆分）。-->
# Canonical Dependency Graph（学习依赖主线）

本文件由 learning-path 的 SKILL.md 引用。以该图为主线依赖关系；正文双链只用于 cross-validation，不覆盖主线依赖。

```yaml
DEPENDENCY_GRAPH:
  Qubit-State-and-Superposition:
    prerequisites: []
    description: "Root node: qubit state, superposition, Bloch sphere"

  Pauli-Matrices:
    prerequisites: [Qubit-State-and-Superposition]
    description: "Pauli X/Y/Z matrices and Pauli gates"

  Tensor-Product:
    prerequisites: [Qubit-State-and-Superposition]
    description: "Tensor product for multi-qubit systems"

  Optical-Tweezer-Arrays:
    prerequisites: [Qubit-State-and-Superposition]
    description: "Optical dipole trap arrays for atom manipulation"

  Single-Qubit-Gates:
    prerequisites: [Qubit-State-and-Superposition, Pauli-Matrices]
    description: "Single-qubit gate operations on Bloch sphere"

  Two-Qubit-State-and-Entanglement:
    prerequisites: [Qubit-State-and-Superposition, Tensor-Product]
    description: "Bell states, entanglement, concurrence"

  Gate-Eigenstates:
    prerequisites: [Pauli-Matrices]
    description: "Eigenstates of quantum gate operators"

  Anti-Commutation:
    prerequisites: [Pauli-Matrices, Tensor-Product]
    description: "Anti-commutation relations of Pauli operators"

  Rabi-Flopping:
    prerequisites: [Single-Qubit-Gates]
    description: "Rabi oscillation as physical implementation of single-qubit gates"

  Two-Qubit-Gates:
    prerequisites: [Two-Qubit-State-and-Entanglement, Tensor-Product]
    description: "Two-qubit gate operations (CZ, CNOT, etc.)"

  Quantum-Zeno-Effect:
    prerequisites: [Single-Qubit-Gates]
    description: "Quantum Zeno effect and measurement-induced freezing"

  AC-Stark-Effect:
    prerequisites: [Optical-Tweezer-Arrays, Single-Qubit-Gates]
    description: "AC Stark shift / light shift in optical traps"

  CZ-Gate:
    prerequisites: [Two-Qubit-Gates]
    description: "Controlled-Z gate"

  Grover-Search:
    prerequisites: [Single-Qubit-Gates, Two-Qubit-Gates]
    description: "Grover's search algorithm"

  Quantum-Phase-Estimation:
    prerequisites: [Single-Qubit-Gates, Two-Qubit-Gates]
    description: "Quantum Phase Estimation algorithm"

  Rydberg-Blockade:
    prerequisites: [Rabi-Flopping, CZ-Gate]
    description: "Rydberg blockade mechanism for entangling gates"

  QEC:
    prerequisites: [Two-Qubit-Gates, CZ-Gate]
    description: "Quantum Error Correction fundamentals"

  Surface-Code:
    prerequisites: [QEC]
    description: "Surface code / toric code"

  Transversal-Gate:
    prerequisites: [QEC, Two-Qubit-Gates]
    description: "Transversal entangling gates for fault tolerance"

  Neutral_Atom_Test:
    prerequisites: [Rabi-Flopping, Rydberg-Blockade, Optical-Tweezer-Arrays]
    description: "Hub note: neutral atom array experiment overview"

  Transversal-Teleportation:
    prerequisites: [Transversal-Gate, Surface-Code]
    description: "Logical teleportation for fault-tolerant deep circuits"

  Deep-Circuit-Execution:
    prerequisites: [Transversal-Teleportation]
    description: "Constant-entropy deep circuit execution"
```
