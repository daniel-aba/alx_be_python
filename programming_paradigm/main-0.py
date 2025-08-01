import sys
from bank_account import BankAccount

def main():
    # This check needs to be the very first thing you do
    # before trying to access sys.argv[1].
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Now that we know sys.argv[1] exists, we can safely access it.
    command_and_params = sys.argv[1].split(':')
    command = command_and_params[0]
    
    amount = None
    if len(command_and_params) > 1:
        try:
            amount = float(command_and_params[1])
        except ValueError:
            print("Invalid amount format. Please use a number.")
            sys.exit(1)

    account = BankAccount(100) # Example starting balance

    if command == "deposit" and amount is not None:
        if account.deposit(amount):
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")


if __name__ == "__main__":
    main()