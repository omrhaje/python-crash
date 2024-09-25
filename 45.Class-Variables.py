# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from all class

class Student:

    class_year = 2024                           # <-- Defined outside the constructor
    num_students = 0

    def __init__(self, name, age):              # <-- constructor
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Spongebob", 28)
student2 = Student("Patrick", 25)
student3 = Student("Squidward", 33)
student4 = Student("Sandy", 30)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

