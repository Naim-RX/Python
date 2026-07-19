# The method does not need to access instance variables (self).
# The method does not need to access class variables (cls).
# The method performs a utility task related to the class.
class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


print(Temperature.celsius_to_fahrenheit(30))