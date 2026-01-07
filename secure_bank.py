# secure_bank.py
# ✅ Secure version following best practices

import hashlib
import getpass
import logging

# Logging configuration
logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# User database (hashed passwords)
users = {
    "admin": hashlib.sha256("Admin@123".encode()).hexdigest(),
    "user1": hashlib.sha256("User@123".encode()).hexdigest()
}

accounts = {
    "admin": 10000,
    "user1": 5000
}

current_user = None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    global current_user
    print("=== Secure Bank Login ===")

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    hashed = hash_password(password)

    if username in users and users[username] == hashed:
        current_user = username
        logging.info(f"User {username} logged in successfully")
        print("Login successful!")
        return True
    else:
        logging.warning("Failed login attempt")
        print("Authentication failed")
        return False

def show_balance():
    print(f"Your balance is ₹{accounts[current_user]}")

def deposit():
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            raise ValueError

        accounts[current_user] += amount
        logging.info(f"{current_user} deposited ₹{amount}")
        print("Deposit successful")

    except ValueError:
        print("Invalid amount")

def withdraw():
    try:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            raise ValueError

        if amount > accounts[current_user]:
            print("Insufficient balance")
            logging.warning(f"{current_user} attempted overdraft")
            return

        accounts[current_user] -= amount
        logging.info(f"{current_user} withdrew ₹{amount}")
        print("Withdrawal successful")

    except ValueError:
        print("Invalid amount")

def logout():
    global current_user
    logging.info(f"User {current_user} logged out")
    current_user = None
    print("Logged out securely")

def main():
    if not login():
        return

    while True:
        print("\n1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

        choice = input("Choose option: ").strip()

        if choice == "1":
            show_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            logout()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
