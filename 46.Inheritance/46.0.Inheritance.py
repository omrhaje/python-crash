# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek")

dog = Dog("skibidi")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()