# -------------------- Reading a File --------------------

# Open the file 'myFile.txt' in read mode ('r')
f = open('myFile.txt', 'r')

# Read all the contents of the file and store it in the variable 'text'
text = f.read()

# Print the file contents
print(text)

# Close the file after reading
f.close()


# -------------------- Writing to a File --------------------

# Open the file in write mode ('w')
# This will overwrite all previous contents of the file
w = open('myFile.txt', 'w')

# Open the same file in append mode ('a')
# Append mode adds new text at the end without deleting old content
a = open('myFile.txt', 'a')

# Write "Hello" into the file
w.write("Hello")

# Append " Hallo" at the end of the file
a.write(" Hallo")

# Close both files after writing
w.close()
a.close()


# -------------------- Using 'with open' --------------------

# Open the file in append mode using 'with'
# 'with' automatically closes the file after the block ends
with open('myFile.txt', 'a') as f:
    
    # Add more text to the file
    f.write(" My name is Naim")


# -------------------- Reading the Updated File --------------------

# Open the file again in read mode
with open('myFile.txt', 'r') as f:
    
    # Read and print the updated contents of the file
    print(f.read())


# Open the file in read mode
f = open('myFile.txt', 'r')

# Infinite loop to read the file line by line
while True:
    
    # Read one line from the file
    line = f.readline()
    
    # Print the current line
    print(line)
    
    # If the line is empty, it means end of file is reached
    if not line:
        
        # Print the empty line and its data type
        print(line, type(line))
        
        # Exit the loop
        break


# Initialize counter variable
i = 0

# Another infinite loop
while True:
    
    # Increase counter by 1
    i = i + 1
    
    # Check if line is empty
    if not line:
        break
    
    # ERROR:
    # line is a string, and strings do not have readline() method
    # This line will cause an error
    line = line.readline()
    
    # Split the line using comma (,)
    # Take first value
    x1 = line.split(',')[0]
    
    # Take second value
    x2 = line.split(',')[1]
    
    # Print formatted output
    print(f'Marks are {x1} {x2}')