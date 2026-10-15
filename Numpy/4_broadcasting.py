import numpy as np
#Allows NumPy to perform operations on arrays of different shapes and sizes by automatically expanding the smaller array to match the shape of the larger array. This is known as broadcasting.

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[10, 20, 30]])
print(arr1.shape)
print(arr2.shape)
print(arr1*arr2) # Broadcasting occurs here, arr2 is expanded to match the shape of arr1