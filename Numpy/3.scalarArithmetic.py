import numpy as np

array = np.array([1,2,3])
print(array+1)
print(array-2)
print(array*3)
print(array/2)
print(array**2)

#vectorized math function
print(np.sqrt(array))
print(np.round(array))
print(np.pi)

#Element wise arithmetic
array1 = np.array([1,2,3])
array2 = np.array([3,4,5])

print(array1 + array2)
print(array2 - array1)

#Comparison operator
scores = np.array([91,23,82,72])
print(scores >59)