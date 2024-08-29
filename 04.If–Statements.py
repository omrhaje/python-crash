# if = Do some code only IF some condition is True
#      Else do something else

# IF STATEMENTS

# example 1

age = int(input("Enter your age:"))

if age >= 100:
    print("You are too old to be on this website! ")
elif age >= 18:
    print("You are now signed up! ")
elif age < 0:
    print("You haven't been born yet! ")
else:
    print("You cannot sign up because your underage! ")


# example 2

response = input("Would you like to have some food? (Y/N) : ")

if response == "Y":
    print("Here you go enjoy! ")
elif response == "y":
    print("Here you go enjoy! ")
else:
    print("alright then")


# example 3

name = input("Enter your name: ")

if name == "":
    print("You didn't enter anything!?!?")
else:
    print(f"Hello {name} nice to meet you! ")


# example 4

online = True

if online:
   print("You are online! ")
else:
   print("You are offline")