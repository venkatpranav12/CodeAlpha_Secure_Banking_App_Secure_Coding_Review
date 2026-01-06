# secure_bank.py

import getpass
import hashlib

users = {
    "venkat": {
        "password": hashlib.sha256("1234".encode()).hexdigest(),
        "balance": 5000
    }
}

def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username in users:
        if users[username]["password"] == hash_password(password):
            print("Login successful")
            return username

    print("Invalid login")
    return None

def menu(user):
    while True:
        print("\n1. Balance\n2. Deposit\n3. Withdraw\n4. Logout")
        choice = input("Choice: ")

        if choice == "1":
            print("Balance:", users[user]["balance"])

        elif choice == "2":
            amt = int(input("Amount: "))
            if amt > 0:
                users[user]["balance"] += amt
                print("Deposited")

        elif choice == "3":
            amt = int(input("Amount: "))
            if 0 < amt <= users[user]["balance"]:
                users[user]["balance"] -= amt
                print("Withdrawn")
            else:
                print("Invalid amount")

        elif choice == "4":
            break

user = login()
if user:
    menu(user)
