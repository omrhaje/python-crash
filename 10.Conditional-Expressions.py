# conditional expression = A one-line shortcut for the if-else statement (tenary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y
#                          X is True and Y is False

num = 29
a = 6
b = 7
age = 19
temperature = 19
user_role = "admin"
perfect_age = 9

print(f"Yes" if perfect_age >= 10 else "No")
print("Positive" if num > 0 else "Negative")


result = "EVEN" if num % 2 == 0 else "ODD"          # Remainder operator, check remain, if remain => "ODD", else "EVEN"
print(result)


max_num = a if a > b else b
min_num = a if a < b else b
print(max_num, min_num)


status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 15 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)