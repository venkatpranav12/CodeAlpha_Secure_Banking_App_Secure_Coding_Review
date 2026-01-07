# insecure_bank.py
# ❌ DO NOT USE IN PRODUCTION

users = {
    "admin": "admin123",
    "user1": "password"
}

balance = 5000

def login():
    print("=== Insecure Bank Login ===")
    username = input("Username: ")
    password = input("Password: ")

    # ❌ Plaintext password comparison
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials")
        return False

def show_balance():
    # ❌ No authentication check
    print(f"Your balance is ₹{balance}")

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))

    # ❌ No proper validation
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful")
    else:
        print("Insufficient balance")

def main():
    if login():
        while True:
            print("\n1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                show_balance()
            elif choice == "2":
                deposit()
            elif choice == "3":
                withdraw()
            elif choice == "4":
                break
            else:
                print("Invalid choice")

main()
