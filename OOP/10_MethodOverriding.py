class Employee:
    def work(self):
        print("Employee is working")


class Manager(Employee):
    def work(self):
        print("Manager is managing the team")


class Developer(Employee):
    def work(self):
        super().work()
        print("Developer is writing code")


e = Employee()
m = Manager()
d = Developer()

e.work()
m.work()
d.work()