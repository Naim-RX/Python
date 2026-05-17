# Import only sqrt and pi from the math module
from math import sqrt, pi
# Import everything (*) from the math module
from math import *
# Import a custom Python file/module named naim
import naim

# Import the complete math module
import math
# Print all functions, variables, and attributes available in math module
print(dir(math))

# Calculate the square root of 9 and store it in result
result = sqrt(9)

# Call the welcome() function from naim module and print its return value
print(naim.welcome())