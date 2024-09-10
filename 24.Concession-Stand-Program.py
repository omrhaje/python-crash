# Concession stand program          dictionary = a collection of {key/value} pairs Example

menu = {"pizza": 5.99,
        "burger": 4.99,
        "popcorn": 9.99,
        "fries": 1.99,
        "lemonade": 4.99,
        "chips": 1.50,
        "soda(any kind)": 2.99}
cart = []
total = 0

print("--------- OUR MENU ---------")
for key, value in menu.items():
    print(f"{key:20}: {value: .2f}€")
print("----------------------------")
while True:
    food = input("Select an item (press enter to quit): ")
    if food == "":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------- YOUR CART ---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your Total is: {total: .2f}€")