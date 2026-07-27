"""
Day 04 Mini Project
Bank Management System
"""

balance = 1000.0


def show_menu():
    """Display the available banking operations."""

    print("\n" + "=" * 40)
    print("         BANK MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("=" * 40)


def check_balance():
    """Display the current account balance."""

    print(f"Current Balance: £{balance:.2f}")


def deposit_money():
    """Deposit money and return the updated balance."""

    global balance

    amount = float(input("Enter deposit amount: £"))

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return

    balance += amount

    print(f"£{amount:.2f} deposited successfully.")
    print(f"New Balance: £{balance:.2f}")


def withdraw_money():
    """Withdraw money if sufficient balance is available."""

    global balance

    amount = float(input("Enter withdrawal amount: £"))

    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance -= amount

        print(f"£{amount:.2f} withdrawn successfully.")
        print(f"Remaining Balance: £{balance:.2f}")


def run_bank():
    """Run the bank application."""

    while True:

        show_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit_money()

        elif choice == "3":
            withdraw_money()

        elif choice == "4":
            print("Thank you for using our bank.")
            break

        else:
            print("Invalid choice. Please select 1-4.")


run_bank()
