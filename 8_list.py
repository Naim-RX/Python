# Create a list named 'li' with multiple integer values
li = [1,3,5,7,9,10,11,12,13,14,15]

# Print the data type of the variable 'li'
print(type(li))

# Check if the value 3 exists inside the list
if 3 in li:
    
    # This line executes if 3 is found in the list
    print("YES")
else:
    
    # This line executes if 3 is not found in the list
    print("NO") 

# Print all elements of the list using slicing
print(li[:])

# Print elements from index 0 to 10 with step size 2
print(li[0:11:2])

# List comprehension:
# Create a new list containing squares of numbers from 0 to 4
lsc = [i*i for i in range(5)]

# Print the new squared list
print(lsc)

# Add the value 16 at the end of the list
li.append(16)

# Find the index position of value 1 in the list
li.index(1)

# Count how many times the value 2 appears in the list
li.count(2)

# Create a copy of the list and store it in variable 'm'
m = li.copy()

# Sort the list in descending order
li.sort(reverse=True)

# Print the sorted list
print(li)

# Insert the value 100 at index position 1
li.insert(1,100)

# Create another list named 'x'
x = [100,200]

# Add all elements of list 'x' into list 'li'
li.extend(x)

# Concatenate list 'x' and list 'li' and store in variable 'k'
k = x + li

# Print the final combined list
print(k)