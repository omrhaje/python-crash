# List comprehension = A concise way to create lists in Python
#                       Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]

# Traditional way

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

#-------

# List comprehension way

doubles = [x * 2 for x in range(1, 11) ]
triple = [y * 3 for y in range(1, 11) ]
squares = [z * z for z in range(1, 11)]

print(squares)

#-------

# strings

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)






numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 == 1]
print(odd_num)