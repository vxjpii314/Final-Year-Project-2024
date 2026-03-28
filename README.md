# Final Year Project 2024: Investigating The Dynamics & Decoherence of Jaynes-Cummings Model (JCM).

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 📌 Overview
This repository contains the complete documentation and implementation of my Final Year Project (FYP) completed in 2024. The project focuses on investigation ofthe dynamics of a two-level atom interacting with a quantized field within the Jaynes-Cummings Model (JCM). Besides, quantum phenomena including avoided crossings, damped oscillations and collapse-and-revival effects are also analyzed under both unitary and dissipative conditions.By implementing the Lindblad master equation, the study evaluates the impact of spontaneous emission ($\gamma$) and cavity decay ($\kappa$) on the population dynamics and coherence of the atom-field density matrix. Finally, numerical simulations are conducted to validate theoretical predictions regarding these dissipation mechanisms.


---

## 📂 Repository Structure

| Folder/File | Description |
| :--- | :--- |
| `/code` | Python implementation, including simulation code in python. |
| `/thesis` | The complete final thesis PDF and LaTeX source files. |
| `/slides` | Presentation slides used for the final viva/defense. |
| `requirements.txt` | Python dependencies required to run the simulations. |

---

## 💻 Code & Implementation
The core of this project involves solving complex [e.g., Quantum Master Equations / Magnetic Field Eigenvalues] using numerical and symbolic Python libraries.

### Key Features
* **Symbolic Modeling:** Uses `SymPy` for Laplace transforms and analytical derivations.
* **Numerical Simulation:** Uses `NumPy` and `SciPy` for high-performance matrix operations.
* **Data Visualization:** Custom `Matplotlib` scripts for plotting eigenvalue evolution and time-domain responses.

