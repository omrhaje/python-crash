# * args     = allows you to pass multiple non-key arguments            # args = arguments
# ** kwargs  = allows you to pass multiple keyword-arguments            # kwargs = keyword-arguments
#             * unpacking operator
#             1. positional 2. default 3. keyword 4. ARBITRARY

# Example 1     *

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1497700, 502300))           # with the * you can use as many arguments
                                        # without a limit and no positional arguments needed!

# Example 2     *

                # unpacking operator then a unique parameter name
# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Dr.", "Spongebob", "Squarepants", "III")      # All of these arguments are in a tuple





# Example 1 **


# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_address(street="Fake Str. 123",                       # kwargs are in All of these arguments are in a dictionary
#               apt="12",
#               city="Hamburg",
#               state="Hamburg",
#               zip="22419")



# Example 2 * / **


# positional arguments come first then followed by keyword arguments!!!
                                            # And it won't work the other way out

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")



shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="Fake Str. 123",
               apt="#12",
               city="Hamburg",
               state="Hamburg",
               zip="22419")
