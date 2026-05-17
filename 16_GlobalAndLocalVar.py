x = 75   # Global variable

def myFunc():
    # x = x + 1 tries to modify x
    # Python thinks x is a local variable here
    # But it has no value assigned before using it
    # So this causes an error
    #x = x + 1

    # 'global x' tells Python to use the global variable x
    global x
    # Increase the value of x by 1
    x = x + 1
    # Print updated value inside the function
    print(x)

# Call the function
myFunc()

# Print global variable
print(x)