# Python Slot Machine

import random


def spin_row():
    symbols = ['🍒','🍉','🔔','🍋','🌟']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 6
        elif row[0] == '🍋':
            return bet * 7
        elif row[0] == '🌟':
            return bet * 100
    return 0

def main():
    balance = 100
    print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
    print("Welcome to Py Slots! ")
    print("Symbols: 🍒 🍉 🔔 🍋 🌟")
    print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")

    while balance > 0:
        print(f"Current balance: €{balance}")

        print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
        bet = input("Place your bet amount:")


        if not bet.isdigit():
            print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
            print("Please enter a valid number")
            print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
            continue

        bet = int(bet)

        if bet > balance:
            print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
            print("Insufficient funds!")
            print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
            continue

        if bet < 5:
            print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
            print("Bet must be greater than 5€")
            print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won €{payout}")
        else:
            print("You lose!")

        balance += payout

        play_again = input("Do you want to spin again (Y/N): ").upper()

        if play_again == 'Y':
            continue
        else:
            break


    print(f"Gamer over! Your final balance is €{balance}")

if __name__ == '__main__':
    main()