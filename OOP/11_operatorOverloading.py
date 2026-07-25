class Book:

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


book1 = Book(200)
book2 = Book(150)

print(book1 + book2)


class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name: {self.name}"


s = Student("Naim")
print(s)

