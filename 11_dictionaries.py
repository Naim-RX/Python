# Creating a dictionary with key-value pairs
dic = {
    "Key": "Value",
    "Toyota": "Crown"
}

# Prints all values of the dictionary
print(dic.values())

# Prints the whole dictionary
print(dic)

# This would cause an error because dictionaries are not called like functions
# print(dic('BMW'))

# Safely tries to get the value of key 'BMW'
# Returns None because 'BMW' does not exist
print(dic.get('BMW'))

# Loop through all keys in the dictionary
for key in dic.keys():
    # Print value using the key
    print(dic[key])

# Loop through both keys and values together
for key, value in dic.items():
    # Print only the value
    print(value)

# Creating first dictionary
ep1 = {
    122: 45,
    123: 47,
    124: 34,
    125: 56
}

# Creating second dictionary
ep2 = {
    222: 33
}

# Adds all items from ep2 into ep1
ep1.update(ep2)

# Removes all items from ep1
# ep1.clear()

# Creates an empty dictionary
empt = {}

# Removes key 122 from ep1
# ep1.pop(122)

# Removes the last inserted item from ep1
# ep1.popitem()

# Deletes key 122 from ep1
del ep1[122]