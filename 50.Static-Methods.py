# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"         # Instance method

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]         # This static method belongs to the class "Employee" and not the other codes
        return position in valid_positions

employee1 = Employee("Mr.Crabs", "Manager")
employee2 = Employee("Spongebob", "Cook")
employee3 = Employee("Squidward", "Cashier")



print(Employee.is_valid_position("Cashier"))
print(employee1.get_info())                         # For an Instance method you access an object then call the instance method
print(employee2.get_info())                         # and with a static method you only need to access that class
print(employee3.get_info())