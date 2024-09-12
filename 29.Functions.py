# function = A block of reusable code
#            place () after the function name to invoke it

# Function

# - Define a new function with 'def'
# - A function contains a block of reusable code
# - A function has a name
# - Between the ( ), there could be parameters defined. These parameters could be used in the function locally

# - A function could do the task locally without throwing a result back.
# OR 'return' could be added to SEND a result back and END the function


# happy_birthday is a function and (name, age) are the parameters


def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age}!")
    print("Happy birthday to you!")
    print()

happy_birthday("key", 17)
happy_birthday("san", 11)
happy_birthday("jona", 29)



def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of €{amount:.2f} is due: {due_date}")

display_invoice("omrhaje", 53.99, "20.09.2024")




# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))





def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("HamM", "OpPs")

print(full_name)