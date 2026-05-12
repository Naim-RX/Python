# Define a function named gmean with two parameters: a and b
def gmean(a,b):
    
    # Calculate the mean value using the formula
    mean = (a*b)/(a+b)
    
    # Print the calculated mean
    print(mean)

# Call the gmean function with values 2 and 5
gmean(2,5)


# Define a function named func with parameters a and b
def func(a,b):
    
    # pass means the function is empty for now
    pass


# Define a function named average that accepts multiple arguments
def average(*numbers):
    
    # Print the data type of numbers (it will be a tuple)
    print(type(numbers))
    
    # Initialize sum variable with 0
    sum = 0
    
    # Loop through each number in numbers
    for i in numbers:
        
        # Add each number to sum
        sum = sum + i
    
    # Print the average of all numbers
    print(sum / len(numbers))

# Call the average function with three values
average(5,10,5)


# Define a function named name that accepts keyword arguments
def name(**name):
    
    # Print the data type of name (it will be a dictionary)
    print(type(name))
    
    # Print the value of the key "fname"
    print(name["fname"])

# Call the function using keyword arguments
name(lname="Naim", mname="Asraful", fname="Golam")