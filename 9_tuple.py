# Create a tuple named 'tup' with four integer values
tup = (1,2,3,4)

# Print the data type of 'tup' and the tuple itself
print(type(tup),tup)

# Print the total number of elements in the tuple
print(len(tup))

# Slice the tuple from index 1 to index 2
# (index 3 is excluded)
tup2 = tup[1:3]

# Print the sliced tuple
print(tup2)

# Convert the tuple into a list and store it in 'temp'
# because tuples are immutable (cannot be changed directly)
temp = list(tup)

# Add the value 5 to the list
temp.append(5)

# Convert the modified list back into a tuple
tup = tuple(temp)

# Print the updated tuple
print(tup)

# Find the index position of value 3
# Search starts from index 1 and ends before index 4
res = tup.index(3 , 1 , 4)

# Print the index result
print(res)