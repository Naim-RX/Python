# ------------------ MAP ------------------

# Function that takes a number and returns its double
def cube(x):
    return x + x   # Same as x * 2

# List of numbers
marks = [2, 4, 5, 23, 4, 2]

# map() applies the cube() function to every element in the list
newl = list(map(cube, marks))

# Print the modified list
print(newl)


# ------------------ FILTER ------------------

# Function that returns True if the number is greater than 4
def filter_func(x):
    return x > 4

# filter() keeps only the elements for which filter_func() returns True
newf = list(filter(filter_func, marks))

# Print the filtered list
print(newf)


# ------------------ REDUCE ------------------

# Import reduce from functools
from functools import reduce

# Function that adds two numbers
def sum(x, y):
    return x + y

# List of numbers
numbers = [1, 2, 3, 4, 5]

# reduce() repeatedly applies the sum() function
# Calculation:
# (((1 + 2) + 3) + 4) + 5 = 15
s = reduce(sum, numbers)

# Print the final result
print(s)