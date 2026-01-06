# insecure_bank.py

users = {
    "venkat": {"password": "1234", "balance": 5000}
}

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login success")
        return username
    else:
        print("Login failed")
        return None

def menu(user):
    while True:
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

        choice = input("Choice: ")

        if choice == "1":
            print("Balance:", users[user]["balance"])
        elif choice == "2":
            amt = int(input("Amount: "))
            users[user]["balance"] += amt
        elif choice == "3":
            amt = int(input("Amount: "))
            users[user]["balance"] -= amt
        elif choice == "4":
            break

user = login()
if user:
    menu(user)
