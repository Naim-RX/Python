class Student:

    university = "DIU"

    def __init__(self, name,id):
        self.name = name
        self.id = id

    # Instance method
    def show_name(self):
        print(self.name)

    # Class method
    @classmethod
    def show_university(cls):
        print(cls.university)

    #Class method as alternative constructor
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

    # Static method
    @staticmethod
    def greet():
        print("Welcome to Python")

s = Student("Naim",101)

# Instance method
s.show_name()

# Class method
Student.show_university()

#Class method as alternative constructor
str = "Naim-101"
s1 = Student.fromstr(str)
print(s1.name)
print(s1.id)

# Static method
Student.greet()