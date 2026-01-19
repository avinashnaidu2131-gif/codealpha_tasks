# Secure Coding Review — Findings Report

## Application Reviewed
Python-based Login System

---

## Vulnerabilities Identified

### 1. Plaintext Password Storage
**Issue:**  
Passwords are stored directly in source code in readable format.

**Risk:**  
Anyone with access to the code can see user credentials.

**Remediation:**  
Store hashed passwords using secure hashing algorithms like SHA-256 or bcrypt.

---

### 2. Password Visible During Input
**Issue:**  
Password input is visible on the screen.

**Risk:**  
Shoulder surfing and screen recording attacks.

**Remediation:**  
Use masked input with Python's `getpass` module.

---

### 3. No Brute Force Protection
**Issue:**  
Unlimited login attempts allowed.

**Risk:**  
Attackers can guess passwords using brute force.

**Remediation:**  
Implement attempt limits and lockout mechanisms.

---

### 4. Hardcoded Credentials
**Issue:**  
User data is embedded in source code.

**Risk:**  
Difficult to manage securely and unsafe for production.

**Remediation:**  
Store credentials in a secure database or environment variables.

---

## Summary
The secure version improves confidentiality by hashing passwords and hiding password input. Further improvements should include logging, account lockout, and secure storage systems.
