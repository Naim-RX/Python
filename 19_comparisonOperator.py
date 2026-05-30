# String value
a = "4"

# Integer value
b = 4

# Another integer value
c = 4

# 'is' checks whether both variables refer to the same object in memory
# a is a string and b is an integer, so they are different objects
print(a is b)      # False

# b and c both refer to the integer 4
# Small integers are usually cached by Python, so they often point to the same object
print(b is c)      # True

# '==' checks whether the values are equal
# "4" (string) and 4 (integer) have different types and values
print(a == b)      # False