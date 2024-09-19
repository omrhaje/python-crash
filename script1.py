# if __name == __main__: (this script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,
#               help with readability,
#               leaves no global variables,
#               avoid unintended execution)


#             Example library = import library for functionality
#               When running library directly, display a help page




def favorite_food(food):
    print(f"your favorite food is {food}")


def main():
    print("This is script 1")
    favorite_food("Pizza")
    print("Goodbye")

if __name__ == '__main__':          # that if statement is important because with that it will only execute in Script 1.
    main()                          # only runs the code directly