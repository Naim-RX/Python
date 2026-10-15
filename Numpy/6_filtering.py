import numpy as np
#Filtering is a technique used to extract specific elements from an array based on certain conditions. It allows you to create a new array that contains only the elements that meet the specified criteria.
arr = np.array([[20,13,24,22,10],[23,53,12,11,15]])
teenagers= arr[arr <18]
print(teenagers) # Output: [13 10 12 11 15]