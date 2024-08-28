# Typecasting = the process of converting a variable from one data type to another
#.              str(), int(), float(), bool()

name = "Omar Haje"
age = 18
gpa = 3.2
is_student = True

gpa = int(gpa)
print(gpa)

age = str(age)
print(age)

age = float(age)
print(age)

# Check the type of the value
print(type(gpa))

# Check the value availability
# if the user didn't type there name then it should say False otherwise True
name = bool(name)
print(name)