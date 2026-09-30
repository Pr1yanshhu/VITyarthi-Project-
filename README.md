# Bank Account Management System

A simple menu-driven bank account program written in Python. It runs in the terminal and lets you create accounts, deposit and withdraw money, check balances, and view account details.

| | |
|---|---|
| **Name** | Priyanshu Kumar |
| **Registration No.** | 26BAi10969 |

---

## Features

1. **Create Account** - enter a name and initial deposit; an account number is generated automatically (1001, 1002, ...)
2. **Deposit** - add money to an existing account
3. **Withdraw** - take money out, but not more than the balance
4. **Check Balance** - see the current balance
5. **Display Account Details** - see account number, holder name, and balance
6. **Exit** - close the program

## Requirements

- Python 3.x
- No external libraries

## How to Run

1. Save the code in a file named `code.py`.
2. Open a terminal in the folder containing the file.
3. Run:

```bash
python code.py
```

(On some systems use `python3 code.py`.)

## Sample Run

```
===== BANK ACCOUNT MANAGEMENT SYSTEM =====
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Display Account Details
6. Exit
Enter your choice (1-6): 1
Enter account holder name: Rahul Sharma
Enter initial deposit: 5000
Account created successfully!
Your account number is: 1001
Enter your choice (1-6): 3
Enter account number: 1001
Enter amount to withdraw: 10000
Insufficient balance. Your balance is: 5000
Enter your choice (1-6): 3
Enter account number: 1001
Enter amount to withdraw: 2000
Withdrawal successful. New balance: 3000
Enter your choice (1-6): 6
Thank you for using the bank system. Goodbye!
```

## Input Validation

- Name cannot be empty
- Amounts must be positive whole numbers (no negatives, letters, or decimals)
- Deposit and withdrawal amounts must be greater than 0
- The account number must exist
- Withdrawal cannot exceed the balance
- Menu choices outside 1-6 show an error message

## How It Works

- All accounts are stored in a dictionary called `accounts`, where the key is the account number and the value is a `BankAccount` object holding the name and balance.
- Each menu option has its own function: `create_account()`, `deposit()`, `withdraw()`, `check_balance()`, and `display_details()`.
- Two helper functions, `get_amount()` and `find_account()`, handle the repeated checks for a valid amount and an existing account.
- A `while True` loop shows the menu again and again until the user chooses option 6, which uses `break` to end the program.

## Project Structure

```
.
├── code.py     # complete program (single file)
├── README.md      # project overview and usage
└── statement.md   # project statement
```

## Concepts Used

Variables, `input()` / `print()`, `if / elif / else`, `while` loop, functions, dictionary, and one simple class (`BankAccount`).

## Limitations

- Data is stored only in memory, so it is lost when the program closes.
- There is no PIN or password.
- Only whole-number amounts are supported.
- There is no transaction history.

## Future Improvements

- Save accounts to a file (for example, JSON) so data is kept between runs
- Add a PIN for each account
- Add a transaction history / mini statement
- Add transfers between accounts and support for decimal amounts

## Disclaimer

This is an educational project. It does not handle real money and is not meant to be used as real banking software.
