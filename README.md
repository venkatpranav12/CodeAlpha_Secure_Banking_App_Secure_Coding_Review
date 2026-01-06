# Secure Banking Application – Secure Coding Review

## Project Overview
This project demonstrates a secure coding review of a console-based banking application.
The goal is to identify insecure coding practices and fix them using secure coding principles.

The application supports:
- User login
- Balance checking
- Deposit
- Withdrawal

An insecure version was first analyzed, followed by a secure implementation.

---

## Insecure Coding Issues Identified

1. Plain text password storage
2. Password visible during input
3. No validation for deposit or withdrawal amounts
4. Negative balance possibility
5. Lack of proper authentication checks

---

## Security Risks

- Attackers can steal passwords if code or memory is exposed
- Unauthorized users can gain access
- Financial data can be manipulated
- Application logic can be abused

---

## Secure Fixes Implemented

- Password hashing using SHA-256
- Hidden password input
- Input validation for all monetary operations
- Authentication checks before sensitive actions
- Controlled error messages to prevent information leakage

---

## Files Included

- `insecure_bank.py` – vulnerable implementation
- `secure_bank.py` – secure and improved implementation

---

## Learning Outcomes

- Understood common secure coding mistakes
- Learned how to protect authentication logic
- Applied input validation and access control
- Gained hands-on experience in secure application design

---

## Disclaimer
This project is for educational purposes only and demonstrates secure coding concepts.
