# Take age input from the user and convert it to an integer
a = int(input("Enter your age:"))

# Check if the age is 18 or more
if(a >= 18): 
    
    # Print this message if the condition is True
    print("You can drive")

# Check if the age is 0
elif(a == 0): 
    
    # Print this message if age is invalid
    print("Invalid age")

# Run this block if none of the above conditions are True
else: 
    
    # Print this message if the user is under 18
    print("You can't drive")