class Student:

    university = "DIU"

    def __init__(self, name):
        self.name = name

    # Instance method
    def show_name(self):
        print(self.name)

    # Class method
    @classmethod
    def show_university(cls):
        print(cls.university)

    # Static method
    @staticmethod
    def greet():
        print("Welcome to Python")

s = Student("Naim")

# Instance method
s.show_name()

# Class method
Student.show_university()

# Static method
Student.greet()