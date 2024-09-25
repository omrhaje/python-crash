
# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal:                       #  <-- Grandparent

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):                 # <-- Parent
    def flee(self):
        print(f"{self.name} is fleeing!")

class Predator(Animal):             # <-- Parent
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):             # <-- Children
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

hawk.sleep()