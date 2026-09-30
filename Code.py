# Mini Bank Account Management System
#Project for VITyarthi Python project!

accounts = {}


class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance


def get_amount(message):
    text = input(message)
    if text.isdigit():
        return int(text)
    print("Invalid amount. Please enter a positive whole number.")
    return -1


def find_account():
    text = input("Enter account number: ")
    if text.isdigit() and int(text) in accounts:
        return accounts[int(text)]
    print("Account not found.")
    return None


def create_account():
    name = input("Enter account holder name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    balance = get_amount("Enter initial deposit: ")
    if balance < 0:
        return
    acc_no = 1001 + len(accounts)
    accounts[acc_no] = BankAccount(acc_no, name, balance)
    print("Account created successfully!")
    print("Your account number is:", acc_no)


def deposit():
    acc = find_account()
    if acc is None:
        return
    amount = get_amount("Enter amount to deposit: ")
    if amount < 0:
        return
    if amount == 0:
        print("Amount must be greater than 0.")
    else:
        acc.balance = acc.balance + amount
        print("Deposit successful. New balance:", acc.balance)


def withdraw():
    acc = find_account()
    if acc is None:
        return
    amount = get_amount("Enter amount to withdraw: ")
    if amount < 0:
        return
    if amount == 0:
        print("Amount must be greater than 0.")
    elif amount > acc.balance:
        print("Insufficient balance. Your balance is:", acc.balance)
    else:
        acc.balance = acc.balance - amount
        print("Withdrawal successful. New balance:", acc.balance)


def check_balance():
    acc = find_account()
    if acc is not None:
        print("Current balance:", acc.balance)


def display_details():
    acc = find_account()
    if acc is not None:
        print("----- Account Details -----")
        print("Account Number:", acc.acc_no)
        print("Holder Name   :", acc.name)
        print("Balance       :", acc.balance)


while True:
    print("\n===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        display_details()
    elif choice == "6":
        print("Thank you for using the bank system. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
