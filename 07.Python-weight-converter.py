# Python weight converter

weight = float(input("Enter your weight:"))
unit = input("Kilograms or Pounds? (K or L):")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")         # f is for variables {}. Without it, it will be a string
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"unit was not valid")

