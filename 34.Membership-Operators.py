# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

letter = input("Guess a letter in a secret word: ")

if letter in word:                          # The in membership operator will test to see if the valur or a variable is found within the sequence,
    print(f"There is a {letter}")           # if it is, it is True if not it returns False
else:
    print(f"{letter} was not found")


#-------

# Set

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter a name of a student: ")

if student.capitalize() not in students:
    print(f"{student} is not a student")
 else:
     print(f"{student} is a student")


#-------


# Dictionary

 grades = {"Sandy": "A",
           "Spongebob": "C",
           "Squidward": "B",
           "Patrick": "F"}

 student = input("Enter the name of a student: ")

 if student in grades:
     print(f"{student}'s grade is {grades[student]}")
 else:
     print(f"{student} was not found")


#-------


email = "omrhaje@gmx.de"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")