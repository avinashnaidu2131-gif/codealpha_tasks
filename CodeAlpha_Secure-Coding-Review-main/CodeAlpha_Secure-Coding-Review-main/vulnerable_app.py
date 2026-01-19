# VULNERABLE LOGIN SYSTEM (For Security Review Practice)

users = {
    "admin": "admin123",
    "user": "password"
}

def login():
    print("=== Login System ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Login failed!")

login()
