# Secure Banking Application – Secure Coding Review

## Project Overview
This project demonstrates a secure coding review of a console-based banking application.
An insecure version of the application was analyzed and then fixed using secure coding practices.

## Features
- User authentication
- Balance checking
- Deposit and withdrawal

## Insecure Issues Found
- Plain text password storage
- No input validation
- No protection against negative balances

## Secure Fixes Applied
- Password hashing
- Hidden password input
- Input validation for transactions

## Files
- insecure_bank.py
- secure_bank.py

## Disclaimer
For educational purposes only.
