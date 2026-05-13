# Define a multi-line string using triple quotes (can include apostrophes easily)
str = '''Can't do this thing'''
print(str)  # Print the string

# Define a string variable with a full name
name = "Asraful Naim"

# Print characters from index 8 to 11 (12 is excluded)
print(name[8:12])

# Print characters from index 0 to (length-3), excluding last 3 characters
print(name[0:-3])

# Print characters from index -4 to -3 (negative indexing from end)
print(name[-4:-2])

# Print the total length of the string (including space)
print(len(name))

# Convert the string to uppercase and print
print(name.upper())

# Convert the string to lowercase and print
print(name.lower())

# Define another string with extra '?' characters
str1 = "Naim???"

# Remove trailing '?' characters from the right side
print(str1.rstrip("?"))

# Replace "Naim???" with "Naim"
print(str1.replace("Naim???","Naim"))

# Split the string into a list using space as separator
print(name.split(" "))

# Define a lowercase string
str3 = "bangladesh"

# Capitalize the first letter of the string
print(str3.capitalize())

# Count how many times "Naim" appears in the string
print(name.count("Naim"))

# Check if the string ends with "Naim"
print(name.endswith("Naim"))

# Find the starting index of "Naim" (returns -1 if not found)
print(name.find("Naim"))

# Find the starting index of "Naim" (raises error if not found)
print(name.index("Naim"))

# Check if all characters in the string are lowercase
print(name.islower())

# Check if all characters in the string are uppercase
print(name.isupper())

# Check if the string contains only whitespace characters
print(name.isspace())

# Swap uppercase to lowercase and lowercase to uppercase
print(name.swapcase())

#f-string

name = "Naim"
country = "Bangladesh"

# Create an f-string by inserting variables inside the string
letter = f"Hey my name is {name} and i am from {country}"

# Print the formatted string
print(letter)


price = 49.0999
# Print the price rounded to 2 decimal places using f-string formatting
print(f"Price is {price:.2f}")


#doc string
# Define a function named square that takes one parameter n
def square(n):
    # Docstring: describes what the function does
    '''Takes a number , returns the square of n'''
    # Return the square of n
    return n**2

# Print the docstring of the function
print(square.__doc__)

# Call the function with value 5 and print the result
print(square(5))