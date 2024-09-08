# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable.  Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "kiwi"]

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print(fruits[3])

# Methods that can be used for tuple
print(fruits.index("apple"))
print(fruits.count("apple"))

# methods that can be used for Set
fruits.add("pineapple")
fruits.remove("apple")              # remove for Set
fruits.pop()                        # wll remove the first value, and it's random
fruits.clear()


# methods that can be used for List
fruits[0] = "strawberry"            # replace function [] use: for x in container then print
fruits.append("coconut")            # use container.append to add a value
fruits.remove("apple")              # use container.remove to remove a value
fruits.insert(0, "pineapple")       # insert a value
fruits.sort()                       # for alphabetical order
fruits.reverse()                    # reverse on how you ordered the values not alphabetical. Use .sort too if alphabetical order is needed
# fruits.clear()                      # clear the values
print(fruits.index("kiwi"))

print(fruits)