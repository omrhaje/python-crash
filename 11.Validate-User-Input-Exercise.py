# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


username = input("Enter a username: ")

username.isalpha()          #   True for letters but False for numbers/spaces

if len(username) > 18:
    print("Your username can't be more than 12 characters!")
elif not username.find(" ") == -1:                              # Return value when failure -1, so that's why if not -1 so if not failure
    print("Your username can't contain Spaces!")
elif not username.isalpha():
    print("Your username cannot contain digits or spaces!")
else:
    print(f"Welcome {username}")

name = "moe "
print(username.isalpha())