# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):          # It's better to write the code ones then reuse it to avoid mistakes.
        super().__init__(color, is_filled)                 # If a child shares a similar method with a parent, you'll use the child's method
        self.radius = radius                               # and not the parents. this is method overwriting

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)                 # To extend the functionality method from a parent you can use the super() function
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("red", True, 5)
square = Square("blue", False, 5)
triangle = Triangle("green", True, 5, 10)

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")