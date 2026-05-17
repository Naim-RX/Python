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