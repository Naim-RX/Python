# Store the string "Naim" in the variable name
name = "Naim"

# Loop through each character in the string
for i in name : 
    
    # Print each character
    print(i)
    
    # Check if the character is "N"
    if(i == "N"):
        
        # Print this message if the condition is True
        print("This is first letter")


# Create a list of colors
colors = ["Red","Green","Blue"]

# Loop through each item in the colors list
for color in colors:
    
    # Print each color
    print(color)


# Loop through numbers from 1 to 9
for k in range(1,10):
    
    # Print the value of k
    print(k)


# Initialize variable i with value 0
i = 0

# Run the loop while i is less than 3
while(i < 3):
    
    # Print the current value of i
    print(i)
    
    # Increase the value of i by 1
    i = i + 1
    

# Execute this block after the while loop ends normally
else : 
    
    # Print this message after exiting the loop
    print("Outside whileLoop")