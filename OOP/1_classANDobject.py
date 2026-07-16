# Define a class named Person
class Person:

    # Constructor method that runs automatically when an object is created
    def __init__(self, n, u):
        # Store the name in the object's name attribute
        self.name = n

        # Store the university in the object's university attribute
        self.uni = u

    # Method to display the person's information
    def info(self):
        print(f"Name = {self.name} , University = {self.uni}")


# Create an object 'a' of the Person class
# "Naim" is passed as the name and "Daffodil" as the university
a = Person("Naim", "Daffodil")

# Call the info() method to print the object's information
a.info()