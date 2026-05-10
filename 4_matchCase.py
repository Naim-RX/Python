# Assign the value 4 to variable x
x = 4;

# Start the match-case statement
match x:
    
    # Check if x is equal to 0
    case 0:
        
        # Print this message if x is 0
        print("X is zero")

    # Check if x is equal to 4
    case 4:
        
        # Print this message if x is 4
        print("X is four")

    # Check this condition if previous cases do not match
    case _ if x != 90:
        
        # Print this message if x is not 90
        print("x is not 90")

    # Default case runs if no other case matches
    case _:
        
        # Print the default message
        print("Default")