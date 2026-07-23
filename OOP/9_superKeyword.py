class Person:

    def __init__(self, name):
        self.name = name
        print("Person constructor called")


class Student(Person):

    def __init__(self, name, roll):

        # Call the parent class constructor
        super().__init__(name)

        self.roll = roll
        print("Student constructor called")


s = Student("Naim", 101)

print(s.name)
print(s.roll)