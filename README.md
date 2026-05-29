# 🛡️ Cybersecurity Portfolio Task-01: Production-Grade Caesar Cipher Cryptotool

![Prodigy InfoTech Cybersecurity Internship - Task-01 Banner](https://raw.githubusercontent.com/sachin-120/PRODIGY_CS_01_Caesar_Cipher/main/assets/task_banner.png)

---

[![Language: Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)](LICENSE)
[![Internship: Prodigy InfoTech](https://img.shields.io/badge/Internship-Prodigy%20InfoTech-orange?style=for-the-badge&logo=securityscorecard&logoColor=white)](https://prodigyinfotech.dev/)
[![Focus: Cryptography](https://img.shields.io/badge/Focus-Cryptography-blueviolet?style=for-the-badge)](https://en.wikipedia.org/wiki/Cryptography)
[![Testing: Unittest](https://img.shields.io/badge/Testing-Unittest%20%26%20Pytest-brightgreen?style=for-the-badge&logo=pytest&logoColor=white)](test_caesar_cipher.py)

Welcome to the official repository for **Task-01** of my **Cybersecurity Internship at Prodigy InfoTech**. This project features a highly polished, production-ready implementation of the classic **Caesar Cipher** cryptographic algorithm. Engineered strictly in Python 3, it offers an interactive, ANSI-colored Command Line Interface (CLI) for secure, bidirectional text encryption and decryption, supported by a 100% compliant unit test suite.

---

## 📋 Table of Contents

1. [🎓 Internship Profile](#-internship-profile)
2. [🎯 Project Overview & Mission](#-project-overview--mission)
3. [🔐 Cryptographic Foundation & Theory](#-cryptographic-foundation--theory)
   - [Mathematical Definition](#mathematical-definition)
   - [Visual Cipher Mechanics](#visual-cipher-mechanics)
   - [Cryptanalysis & Vulnerabilities](#cryptanalysis--vulnerabilities)
4. [🛠️ Technical Architecture & Module Design](#%EF%B8%8F-technical-architecture--module-design)
   - [Directory Layout](#directory-layout)
   - [Module Interactions](#module-interactions)
5. [✨ Production Features in Detail](#-production-features-in-detail)
6. [🖥️ Interactive Command Line Interface (CLI) Walkthrough](#%EF%B8%8F-interactive-command-line-interface-cli-walkthrough)
7. [📥 Production Installation & Setup](#-production-installation--setup)
8. [🧪 Robust Test Harness & Verification](#-robust-test-harness--verification)
9. [📊 Performance & Complexity Analysis](#-performance--complexity-analysis)
10. [📝 Professional Git Version Control Workflow](#-professional-git-version-control-workflow)
11. [🔮 Security Engineering Roadmap](#-security-engineering-roadmap)
12. [📚 Academic References & Standards](#-academic-references--standards)
13. [👤 Professional Author Profile](#-professional-author-profile)
14. [📄 License](#-license)

---

## 🎓 Internship Profile

* **Company:** Prodigy InfoTech
* **Role:** Cybersecurity Intern
* **Specialization:** Applied Cryptography & Information Security
* **Task Identifier:** Task-01
* **Project Deliverable:** Secure Caesar Cipher Encryption & Decryption System

---

## 🎯 Project Overview & Mission

The primary goal of this project is to implement symmetric key cryptography principles using a command-line tool. While the Caesar Cipher is a historical algorithm, writing it to production standards involves addressing challenges common to modern security applications:
* **Zero Dependencies:** Minimizing the supply-chain attack vector by using only the Python standard library.
* **Input Validation & Sanitization:** Preventing buffer issues, parsing exceptions, and shell escape bugs.
* **Data Integrity:** Ensuring casing preservation and leaving non-alphabetic metadata (formatting, spacing, symbols) intact.
* **High Test Coverage:** Validating cryptographic boundaries (negative keys, overflow keys) via unit tests.

---

## 🔐 Cryptographic Foundation & Theory

### Mathematical Definition
The Caesar Cipher is a monoalphabetic substitution cipher where each character in a message is replaced by another character shifted a fixed number of positions down the alphabet. 

Let the English alphabet be mapped to integer values in the range $\mathbb{Z}_{26} = \{0, 1, 2, \dots, 25\}$, where $A \mapsto 0$, $B \mapsto 1$, $\dots$, $Z \mapsto 25$.

#### 1. Encryption Formula
For a plaintext character $p \in \mathbb{Z}_{26}$ and a shift key $k \in \mathbb{Z}$:
$$E_k(p) = (p + k) \pmod{26}$$

#### 2. Decryption Formula
For a ciphertext character $c \in \mathbb{Z}_{26}$ and a shift key $k \in \mathbb{Z}$:
$$D_k(c) = (c - k) \pmod{26}$$

In Python, the modulo operator (`%`) natively handles negative values according to modular arithmetic rules, meaning $D_k(c) = E_{-k}(c)$ holds true without requiring manual bounds-checking loops.

---

### Visual Cipher Mechanics
Below is a conceptual representation of how a single letter is shifted under a key of $k = 3$:

```text
Alphabet Ring:
  [A] ──► [B] ──► [C] ──► [D] ──► [E] ... ──► [Z]
   0       1       2       3       4           25

Shift Execution (Key = 3):
  Plaintext:  H  E  L  L  O
              │  │  │  │  │   (Convert to Z_26: H=7, E=4, L=11, L=11, O=14)
              ▼  ▼  ▼  ▼  ▼
  Formula:   (x + 3) mod 26
              │  │  │  │  │   (7+3=10, 4+3=7, 11+3=14, 11+3=14, 14+3=17)
              ▼  ▼  ▼  ▼  ▼
  Ciphertext: K  H  O  O  R   (Map back to Letters: K=10, H=7, O=14, O=14, R=17)