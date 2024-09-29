# Magic methods = Dunder methods ( underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self,title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):                                        # other means the other book. (eq stands for equals). self is the book1 and other is the book2
        return self.title == other.title and self.author == other.author                        # This is for checking if the books are the same

    def __lt__(self, other):                    # lt stands for less than
        return self.num_pages < other.num_pages

    def __gt__(self, other):                    # gt stands for greater than
        return self.num_pages > other.num_pages

    def __add__(self, other):                   # Addition
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):           # Look to see if it contains what you are searching for
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):             # Accessing Book attributes by indexing
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("THE END", "Max Phone", 351)
book2 = Book("The active cherry", "Safari key", 178)
book3 = Book("POWER", "Mustermann", 637)

print(book1 ['audio'])