# Python does not have strict access modifier keywords like Java or C++; instead, it uses naming conventions with underscores to indicate intended visibility
class Student:
    def __init__(self):
        self._name = "Naim"   # Protected variable
        self.__id = "101"   # Private variable

    def show(self):
        print(self.__id)
        print(self._name)

obj = Student()

# Still accessible, but not recommended
obj.show()