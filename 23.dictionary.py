# dictionary = a collection of {key/value} pairs
#              ordered and changeable. NO duplicates

capitals = {"USA": "Washington D.C.",
            "Germany": "Berlin",
            "Italy": "Rom",
            "Sweden": "Stockholm"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Germany"))                  # get the value of the key .get

# if capitals.get("Germany"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist!")

# capitals.update({"China": "Beijing"})           # .update can be used for adding a key and value or update an existing key/value
# capitals.update({"USA": "Beijing"})
# capitals.pop("Sweden")                          # .pop can be used to remove a key/value pair from the dictionary
# capitals.popitem()                              # .popitem will remove the latest Item in the dictionary
# capitals.clear()
# keys = capitals.keys()                            # to get all the keys used in the dictionary use .keys
# values = capitals.values()                        # to get all the values used in the dictionary use .values
# print(keys)


# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")