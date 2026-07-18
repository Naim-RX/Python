
class Myclass:
    def __init__(self, value):
        # _value is a protected attribute (by convention)
        self.value = value

    # Method to display the current value
    def show(self):
        print(f"Value is {self.value}")

    # Getter method using the @property decorator
    # Allows ten_value to be accessed like an attribute
    @property
    def ten_value(self):
        # Return 10 times the stored value
        return 10 * self.value

    # Setter method for the ten_value property
    # Allows assignment to ten_value like an attribute
    @ten_value.setter
    def ten_value(self, new_value):
        # Store one-tenth of the assigned value in _value
        self.value = new_value / 10



obj = Myclass(20)

# Set the property ten_value to 10
# Internally, _value becomes 10 / 10 = 1.0
obj.ten_value = 10

# Print the property value
# Returns 10 * 1.0 = 10.0
print(obj.ten_value)

# Display the actual stored value
obj.show()