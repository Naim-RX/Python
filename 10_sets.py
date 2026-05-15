# Create a set named s1
# Duplicate values are automatically removed in sets
s1 = {2,4,6,8,2}

# Create another set named s2
s2 = {1,3,5,6}

# Print the elements of s1
print(s1)

# Create an empty set
# {} creates an empty dictionary, so set() is used for an empty set
naim = set()

# Return a new set containing all unique elements from both sets
print(s1.union(s2))

# Return a new set containing common elements of both sets
print(s1.intersection(s2))

# Update s1 with only common elements
# This method changes s1 directly and returns None
print(s1.intersection_update(s2))

# Add all elements of s2 into s1
# This method also changes s1 directly and returns None
print(s1.update(s2))

# Return elements that exist in s1 but not in s2
print(s1.difference(s2))

# Check whether s1 and s2 have no common elements
# Returns True if they are completely different
print(s1.isdisjoint(s2))

# Add element 50 to s1
s1.add(50)

# Remove element 2 from s1
# Gives an error if the element does not exist
s1.remove(2)

# Remove element 33 if it exists
# Does not give an error if the element is missing
s1.discard(33)

# Delete the entire set s1
# del s1

# Remove all elements from s2 and make it empty
# s2.clear()