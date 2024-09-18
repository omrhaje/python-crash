# ----------------- main.py -----------------
# module = a file containing code you want to include in your program
#          use 'import' to include a module (built_-in or your own)
#          useful to break up a large program reusable separate files

print(help("modules"))

pi = 3.14159            # put your module in a file then call it from another file using the 'import' function

def square(x):
    return x ** 2
#                                   this code is used for being called from other files
def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius ** 2