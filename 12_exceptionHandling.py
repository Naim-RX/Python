#Exception handling in Python is used to handle runtime errors gracefully so the program does not crash unexpectedly.
#try:
    # Code that may cause an error
#except:
    # Code to handle the error

# Try block:
# Code inside try may generate an exception/error
try:
    
    # Taking input from user and converting it to integer
    num = int(input("Enter a number: "))
    
    # Dividing 10 by the entered number
    result = 10 / num
    
    # Printing the result
    print(result)

# Executes if user enters non-integer value
except ValueError:
    print("Please enter a valid integer")

# Executes if user enters 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# Using else block

# Try block for checking valid input
try:
    
    # Taking integer input from user
    x = int(input("Enter number: "))
    
    # Printing the entered number
    print(x)

# Executes if input is not an integer
except ValueError:
    print("Invalid input")

# Else block runs only if no exception occurs
else:
    print("Program executed successfully")


# | Exception           | Meaning                     |
# | ------------------- | --------------------------- |
# | `ValueError`        | Invalid value               |
# | `TypeError`         | Wrong data type             |
# | `IndexError`        | Invalid list index          |
# | `KeyError`          | Key not found in dictionary |
# | `ZeroDivisionError` | Division by zero            |
# | `FileNotFoundError` | File does not exist         |
# | `ImportError`       | Module import failed        |


#The finally block always executes whether an exception occurs or not.
try:
    file = open("data.txt")

# Executes if the specified file is not found
except FileNotFoundError:
    
    # Print error message
    print("File not found")
except:
    print("something")

# Finally block:
# This block always executes whether an error occurs or not
finally:
    
    # Print completion message
    print("Execution completed")


#Raising Exceptions
age = int(input("Enter age: "))

if age < 18:
    raise ValueError("Age must be 18 or above")

print("Eligible")


#Custom Exception
class InvalidAgeError(Exception):
    pass

age = 15

if age < 18:
    raise InvalidAgeError("Invalid age")

print("Access granted")