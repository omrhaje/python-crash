# Variables = A container for a value (string, integer, float, boolean)
#             A variable behaves as if it was the value it contains

# Strings Text
first_name = "Omar"
food = "burger"
email = "omarhaje@gmx.de"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"this is my email: {email}")

# Integers – Numbers
age = 18
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")


# Float – Decimal Portions
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")


# Boolean – True/False
is_student = False

if is_student:
    print("You are a student")

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")


is_online = False
if is_online:
    print("You are online")
else:
    print("You are offline")


for_sale = False
if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")
