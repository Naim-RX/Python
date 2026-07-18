class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def show_details(self):
        print(f"Employee ID: {self.id}")
        print(f"Employee Name: {self.name}")

class Programmer(Employee):
 
    def show(self):
        print(f"Employee ID: {self.id}")
        print(f"Employee Name: {self.name}")


p1 = Programmer("Alice", 101)
p1.show()
