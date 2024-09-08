# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (enter to quit): ")
    if food.lower() == "":
        break
    else:
        price = float(input(f"Enter the price of {food}: €"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price         # Plus with itsself

print()

print(f"Your total is {total}€ ")