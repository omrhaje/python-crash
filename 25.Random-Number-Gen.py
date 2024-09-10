import random

low = 1
high = 100
options = ("rock", "paper","scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

# number = random.randint(low, high)         # Return random integer in range [a, b], including both end points.
number = random.random()                    # .random is used for a floating number
option = random.choice(options)
random.shuffle(cards)

print(cards)