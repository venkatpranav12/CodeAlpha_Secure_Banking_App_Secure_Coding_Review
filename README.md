# 🏦 Secure Bank Application – Python  
### Secure Coding Review Project

> A hands-on cybersecurity project demonstrating how insecure coding practices can expose financial applications—and how secure coding fixes them.

---

## 🚀 Project Overview

This project focuses on performing a **Secure Coding Review** on a Python-based banking application. It includes two implementations:

- ❌ **Insecure Bank Application** – intentionally vulnerable
- ✅ **Secure Bank Application** – hardened using industry best practices

The objective is to identify security flaws, understand real-world risks, and apply secure coding techniques aligned with **OWASP Secure Coding Guidelines**.

---

## 🎯 Objectives

- Perform a manual secure code review
- Identify common security vulnerabilities
- Implement secure authentication mechanisms
- Enforce strict input validation
- Apply session-based access control
- Document findings in a professional format

---

## 🗂️ Project Structure

secure-bank-app/
│
├── insecure_bank.py # Vulnerable implementation (for learning purposes)
├── secure_bank.py # Secure implementation (best practices applied)
├── bank.log # Audit log file (generated at runtime)
└── README.md # Project documentation

---

## 🔍 Insecure Application Overview (`insecure_bank.py`)

The insecure version simulates common beginner-level and real-world mistakes that lead to serious security vulnerabilities.

### ❌ Identified Issues

- Plaintext password storage and comparison
- Visible password input
- Lack of input validation
- No authentication checks for sensitive operations
- No error handling
- No logging or monitoring
- Use of global variables for sensitive data

⚠️ This version is strictly for learning and analysis purposes.

---

## 🛡️ Secure Application Overview (`secure_bank.py`)

The secure version addresses all vulnerabilities and follows secure-by-design principles.

### ✅ Implemented Security Controls

- Password protection using **SHA-256 hashing**
- Hidden password input using `getpass`
- Strict validation for deposit and withdrawal inputs
- Controlled session management using authenticated user state
- Audit logging for user actions and transactions
- Robust error handling using try–except blocks

---

## 📊 Security Comparison Summary

| Area | Insecure Version | Secure Version |
|----|----|----|
Authentication | Plaintext | SHA-256 hashing |
Password Input | Visible | Hidden (`getpass`) |
Input Validation | None | Strict validation |
Logging | ❌ | ✅ Audit logs |
Error Handling | ❌ | ✅ Try–Except |
Session Control | ❌ | ✅ Controlled user state |

---

## 🧠 Tools & Methodologies Used

- **Manual Code Review** – Line-by-line inspection to detect insecure logic
- **Bandit (Python Static Analyzer)** – Automated detection of security issues
- **OWASP Secure Coding Guidelines** – Reference for secure development standards

---

## ▶️ How to Run the Project

### Prerequisites
- Python 3.x installed

### Run the Insecure Version
```bash
python insecure_bank.py
python secure_bank.py

---
## 👨‍💻 Author

**Venkat Pranav**  
B.E. Computer Science & Cybersecurity  
Secure Coding | Application Security | Python

