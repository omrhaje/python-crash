# Shopping cart program my version 😄

games = []
prices = []
total = 0

while True:
    game = input("Enter the name of the game would like to buy (press enter to quit): ")
    if game == "":
        break
    else:
        price = float(input(f"Enter the price of the {game}: € "))
        games.append(game)
        prices.append(price)

print("------ YOUR CART ------")

for game in games:
    print(game, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: {total}€")