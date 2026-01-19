# SECURE LOGIN SYSTEM (Improved Version)

import getpass
import hashlib

users = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "user": hashlib.sha256("password".encode()).hexdigest()
}

def login():
    print("=== Secure Login System ===")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    hashed_input = hashlib.sha256(password.encode()).hexdigest()

    if username in users and users[username] == hashed_input:
        print("Login successful!")
    else:
        print("Login failed!")

login()
