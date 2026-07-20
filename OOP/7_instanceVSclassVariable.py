class Student:

    # Class variable
    university = "DIU"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age


s1 = Student("Naim", 22)
s2 = Student("Rahim", 21)

print("Before changing:")
print(s1.name, s1.university)
print(s2.name, s2.university)

# Change class variable
Student.university = "BUET"

# Change only s1's instance variable
s1.name = "Asraful"

print("\nAfter changing:")
print(s1.name, s1.university)
print(s2.name, s2.university)