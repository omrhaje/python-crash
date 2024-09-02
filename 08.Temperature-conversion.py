unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    calc = (9 * temp) / 5 + 32
    temp = round(calc, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    calc = (temp - 32) * 5 / 9
    temp = round(calc, 1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")