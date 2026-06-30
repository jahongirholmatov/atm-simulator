CORRECT_PIN = "1234"
INITIAL_BALANCE = 1000.00
MAX_ATTEMPTS = 3
def authenticate():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        pin = input("Enter your PIN: ")
        if pin == CORRECT_PIN:
            print("\nAccess granted. Welcome!\n")
            return True
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
            else:
                print("\nAccount locked. Too many incorrect PIN attempts.")
    return False

def check_balance(balance):
    print(f"\nYour current balance is: ${balance:.2f}\n")


def deposit(balance):
    try:
        amount = float(input("Enter deposit amount: $"))
        if amount <= 0:
            print("Deposit amount must be greater than zero.\n")
            return balance
        balance += amount
        print(f"${amount:.2f} deposited successfully.")
        print(f"New balance: ${balance:.2f}\n")
        return balance
    except ValueError:
        print("Invalid amount. Please enter a numeric value.\n")
        return balance


def withdraw(balance):
    try:
        amount = float(input("Enter withdrawal amount: $"))
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.\n")
            return balance
        if amount > balance:
            print(f"Insufficient funds. Your balance is ${balance:.2f}.\n")
            return balance
        balance -= amount
        print(f"${amount:.2f} withdrawn successfully.")
        print(f"New balance: ${balance:.2f}\n")
        return balance
    except ValueError:
        print("Invalid amount. Please enter a numeric value.\n")
        return balance


def show_menu():
    print("=" * 30)
    print("         ATM MAIN MENU")
    print("=" * 30)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("=" * 30)


def run_atm():
    print("=" * 30)
    print("     Welcome to PyBank ATM")
    print("=" * 30)

    if not authenticate():
        return

    balance = INITIAL_BALANCE

    while True:
        show_menu()
        choice = input("Select an option (1-4): ").strip()

        match choice:
            case "1":
                check_balance(balance)
            case "2":
                balance = deposit(balance)
            case "3":
                balance = withdraw(balance)
            case "4":
                print("\nThank you for using PyBank ATM. Goodbye!\n")
                break
            case _:
                print("Invalid option. Please select 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    run_atm()
