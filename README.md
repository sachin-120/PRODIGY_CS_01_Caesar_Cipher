# 🛡️ Task-01: Caesar Cipher Encryption & Decryption Tool

![Prodigy InfoTech Cybersecurity Internship - Task-01 Banner](assets/task_banner.png)

*Note: Please refer to the [Screenshots & Assets](#-screenshots--assets) section below for details on placing the internship task banner image.*

---

[![Language: Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)](LICENSE)
[![Internship: Prodigy InfoTech](https://img.shields.io/badge/Internship-Prodigy%20InfoTech-orange?style=for-the-badge&logo=securityscorecard&logoColor=white)](https://prodigyinfotech.dev/)
[![Focus: Cybersecurity](https://img.shields.io/badge/Focus-Cryptography-blueviolet?style=for-the-badge)](https://en.wikipedia.org/wiki/Cryptography)

This repository contains a professional, production-grade Python implementation of the classic **Caesar Cipher** cryptographic algorithm. Developed as **Task-01** during my **Cybersecurity Internship at Prodigy InfoTech**, this application features a sleek, interactive, ANSI-colored Command Line Interface (CLI) and is backed by a robust suite of unit tests.

---

## 📋 Table of Contents
1. [🎓 Internship Context](#-internship-context)
2. [🎯 Task Objective & Statement](#-task-objective--statement)
3. [✨ Features](#-features)
4. [📂 Folder Structure](#-folder-structure)
5. [⚙️ Technologies Used](#%EF%B8%8F-technologies-used)
6. [🧮 How the Algorithm Works](#-how-the-algorithm-works)
7. [📈 Algorithmic Complexity](#-algorithmic-complexity)
8. [📥 Installation Guide](#-installation-guide)
9. [🚀 Usage Instructions](#-usage-instructions)
10. [🧪 Unit Testing](#-unit-testing)
11. [💻 Sample Input & Output](#-sample-input--output)
12. [🖼️ Screenshots & Assets](#-screenshots--assets)
13. [🚀 GitHub Portfolio Deployment Guide](#-github-portfolio-deployment-guide)
14. [🔮 Future Improvements](#-future-improvements)
15. [👤 Author](#-author)
16. [📄 License](#-license)

---

## 🎓 Internship Context

- **Organization:** Prodigy InfoTech
- **Domain:** Cybersecurity
- **Role:** Cybersecurity Intern
- **Task ID:** Task-01
- **Task Title:** Caesar Cipher Encryption & Decryption Tool

---

## 🎯 Task Objective & Statement

### Task Objective
Implement the fundamental principles of symmetric-key cryptography by building a robust command-line utility capable of enciphering (encrypting) and deciphering (decrypting) textual messages using the classic Caesar Cipher algorithm.

### Official Problem Statement
> **Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.**

---

## ✨ Features

- **Interactive CLI:** An elegant, menu-driven terminal interface featuring structured choices and custom ANSI color palettes (cyan, green, yellow, red, magenta) for a premium user experience.
- **Bi-directional Processing:** Easily encrypt plaintext to ciphertext and decrypt ciphertext back to plaintext.
- **Case Preservation:** Maintains uppercase (`A-Z`) and lowercase (`a-z`) formatting without converting or corrupting character casings.
- **Character Safety:** Ensures non-alphabetic elements (numbers, spaces, punctuation marks, and special symbols) remain completely untouched and secure in their original positions.
- **User-Defined Shift Values:** Supports arbitrary shift values (keys) inputted by the user, including negative shifts and shifts larger than the standard 26-letter alphabet (wrapping around gracefully).
- **Zero Dependencies:** Engineered purely using the Python Standard Library, requiring no external packages for core cryptographic and CLI execution.
- **Unit Tested:** Integrated with a thorough automated test suite mapping key edge cases, mathematical boundaries, and character sanitization.
- **Efficient $O(n)$ Implementation:** Built with optimized string join structures, guaranteeing linear time complexity execution.

---

## 📂 Folder Structure

```text
PRODIGY_CS_01/
├── assets/
│   └── task_banner.png      # Internship Task-01 banner image
├── .gitignore              # Git clean paths configuration
├── caesar_cipher.py        # Core cryptographic module (encrypt/decrypt logic)
├── LICENSE                 # MIT License details
├── main.py                 # Main CLI application driver script
├── requirements.txt        # Developer configuration dependencies (pytest)
└── test_caesar_cipher.py   # Automated unit tests suite