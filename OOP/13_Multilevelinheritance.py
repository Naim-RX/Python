class Person:

    def __init__(self):
        print("Person Constructor")


class Student(Person):

    def __init__(self):
        super().__init__()
        print("Student Constructor")


class Graduate(Student):

    def __init__(self):
        super().__init__()
        print("Graduate Constructor")


g = Graduate()