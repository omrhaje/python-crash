# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop


numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):                # Return a reverse iterator over the values of the given sequence.
    print(number, end=" ")

#-------

fruits = {"apple", "orange", "banana", "kiwi"}          # Sets are irreversible so NO

for fruit in fruits:
    print(fruit)

#-------

name = "Bro"

for character in name:
    print(character, end="")
print()

#-------

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.items():
    print(key, value)