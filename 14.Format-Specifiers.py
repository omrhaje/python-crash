# format specifiers = {value:flags} format a value based on what
#                              flags are inserted (+, -, ,, ., >, <, ^)

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1: .2f}")       # the name of : is colon
print(f"Price 2 is ${price2: .2f}")
print(f"Price 3 is ${price3: .2f}")