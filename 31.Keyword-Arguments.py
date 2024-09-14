# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary


def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr.", first="Hesam", last="Younesi")         # positional arguments come before keyword arguments

# ------

for x in range(1, 11):
    print(x, end=" ")               # end= is a keyword already found in the print function

# ------

print("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", sep="–")      # sep= is a keyword already found in the print function

# ------

def get_phone(country, area, first, last):
    return f"{country}{area}{first}{last}"


phone_num = get_phone(country=+49, area=177, first=3612, last=459)              # argument preceded by an identifier that
                                                                                # matches the name of a functions parameters

print(phone_num)
