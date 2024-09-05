
name = input("What's your name: ")
phone_num = input("Enter your phone number: ")


result = len(name)                    #   len will tell you the length that the user typed in
result = name.find("o")               #   will search for the letter but first place doesn't count
result = name.rfind("o")              #   the r stands for reversed
name = name.capitalize()              #   first letter will be written upper case
name = name.upper()                   #   everything will be written upper case
name = name.lower()                   #   everything will be written lower case
result = name.isdigit()               #   boolean, always False if the value is not digit/integer otherwise True
result = name.isalpha()               #   True for letters but False for numbers/spaces
result = phone_num.count("-")         #   count how many strings

phone_num = phone_num.replace("-", " ")           # replace
print(phone_num)



# for the string methods use print(help(str)
print(help(str))