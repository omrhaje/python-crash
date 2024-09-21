# Python Banking Program
from random import choice


def show_balance(balance):
    print("---------------------------")
    print(f"Your balance is €{balance: .2f}")
    print("---------------------------")
def deposit():
    print("---------------------------")
    amount = float(input("Enter an amount to be deposited: "))
    print("---------------------------")
    if amount < 0:
        print("---------------------------")
        print("That's not a valid amount!")
        print("---------------------------")
        return 0
    else:
        return amount

def withdraw(balance):
    print("---------------------------")
    amount = float(input("Enter the amount to be withdrawn: "))
    print("---------------------------")
    if amount > balance:
        print("---------------------------")
        print("Insufficient funds!")
        print("---------------------------")
        return 0
    elif amount < 10:
        print("---------------------------")
        print("Amount must be greater the 10€")
        print("---------------------------")
        return 0
    else:
        return amount

def main():
    balance = 0     # <-- Int/float
    is_running = True       # <-- Boolean

    while is_running:
        print("----- Banking Program -----")
        print("1. Show Balance")
        print("2. Deposit ")
        print("3. Withdraw")
        print("4. Exit")
        print("---------------------------")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("---------------------------")
            print("Your input is NOT valid")
            print("---------------------------")

    print("---------------------------")
    print("Thank you! Have a nice day!")
    print("---------------------------")
if __name__ == '__main__':
    main()