# Math calcs

friends = 10
# additions   +
friends = friends + 1
friends += 1

# subtraction   -
friends = friends - 2
friends -= 2

# multiplication   *
friends = friends * 3
friends *= 3

# division   /
friends = friends / 3
friends /= 3

# exponential **
friends = friends ** 2
friends **= 2

# modulus
remainder = friends % 3

print(remainder)

x = 4.391
y = 9.11231
z = 5

result = round(x)
result = abs(y)               # TO LOOK UP
result = pow(4, 5)            # Calc the power of a base and an exponential
result = max(x, y, z)         # The highest value
result = min(x, y, z)         # The lowest value
print(result)

omar = 'ki'
# --------------------------------------------------------------

import math

x = 9.9

print(math.pi)
print(math.e)

# square route function
result = math.sqrt(x)

# .ceil will round up
result = math.ceil(x)
# .floor will round down
result = math.floor(x)
print(result)


# Math exercise (radius)
import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")

# --------------------------------------------------------------


# Math exercise (area)
import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 3)}cm^2")


# --------------------------------------------------------------


import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")