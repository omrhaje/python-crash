# input() = A function that prompts the user to enter data
#.         Returns the entered data as a float, int

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")

price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}")
print(f"Your Total is: €{total}")