# Project Statement

## Bank Account Management System

| | |
|---|---|
| **Student Name** | Priyanshu Kumar |
| **Registration No.** | 26BAi10969 |
| **Project Type** | Python console application (mini project) |

---

## 1. Problem Statement

Managing bank accounts by hand (on paper or in scattered notes) is slow and error-prone. Account numbers can be duplicated, balances can be miscalculated, and it is easy to allow a withdrawal that is larger than the money actually available.

This project solves that problem on a small scale with a simple Python program. It lets a user create accounts, deposit money, withdraw money, and view balances and account details from a menu in the terminal, while automatically checking every input so that invalid actions are not allowed.

## 2. Objectives

- Build a menu-driven program that behaves like a basic bank counter.
- Generate a unique account number automatically for each new account.
- Prevent invalid transactions (negative amounts, non-numeric input, unknown accounts, and withdrawals above the balance).
- Apply core Python concepts: variables, functions, loops, conditionals, dictionaries, and a simple class.
- Keep the code short, readable, and well commented.

## 3. Scope

### In scope

- Creating an account with the holder's name and an initial deposit
- Depositing money into an existing account
- Withdrawing money from an existing account (only if the balance is enough)
- Checking the balance of an account
- Displaying account number, holder name, and balance
- Basic input validation and clear error messages
- Running repeatedly through a `while True` menu until the user exits

### Out of scope

- Saving data to a file or database (data exists only while the program runs)
- User login, PIN, or password protection
- Decimal amounts (only whole numbers are accepted)
- Transaction history, transfers between accounts, and interest calculation
- Graphical or web interface

## 4. Target Users

- Students learning Python who want to see how a small real-world system is built
- Teachers and evaluators who need a simple demonstration of basic programming concepts

## 5. Functional Requirements

| No. | Feature | Description |
|-----|---------|-------------|
| 1 | Create Account | Takes name and initial deposit; auto-generates account number (starts at 1001) |
| 2 | Deposit | Adds a valid amount to an existing account |
| 3 | Withdraw | Subtracts a valid amount if the balance is sufficient |
| 4 | Check Balance | Shows the current balance |
| 5 | Display Account Details | Shows account number, holder name, and balance |
| 6 | Exit | Ends the program with a goodbye message |

## 6. Validation Rules

- The account holder's name must not be empty.
- Amounts must be whole numbers; negative numbers, letters, and decimals are rejected.
- Deposit and withdrawal amounts must be greater than 0.
- The account number must exist before any operation on it.
- A withdrawal cannot be more than the current balance.
- Any menu choice other than 1 to 6 shows an "Invalid choice" message.

## 7. Technical Constraints

- **Language:** Python 3
- **Structure:** Single file, about 120 lines
- **Storage:** In-memory dictionary (`accounts`)
- **Concepts used:** functions, one simple class (`BankAccount`), dictionary, `if/elif/else`, `while` loop
- **Not used:** external libraries, database, file handling, inheritance, or decorators

## 8. Expected Outcome

A working terminal program in which a user can create accounts and perform deposits and withdrawals safely, with the correct balance always shown and every invalid input handled by a clear message instead of a crash.

## 9. Disclaimer

This is an educational project. It does not handle real money and is not intended for use as real banking software.
