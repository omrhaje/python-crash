# Python calculator

operator = input("Enter an operator (+ * - /):")
num1 = float(input("Enter the 1st number: "))            # without float the result will be a string
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"{operator} is not a valid operator")