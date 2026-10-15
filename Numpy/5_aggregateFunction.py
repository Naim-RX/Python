import numpy as np

#Aggregate functions are used to perform a computation on a set of values and return a single value. Numpy provides several aggregate functions that can be used to perform operations on arrays.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr))  # Sum of all elements
print(np.mean(arr))  # Mean of all elements
print(np.std(arr))  # Standard deviation of all elements
print(np.min(arr))  # Minimum value
print(np.max(arr))  # Maximum value
print(np.median(arr))  # Median value
print(np.prod(arr))  # Product of all elements
print(np.var(arr))  # Variance of all elements
print(np.percentile(arr, 50))  # 50th percentile (median)
print(np.percentile(arr, 25))  # 25th percentile
print(np.argmax(arr))  # Index of the maximum value
print(np.sum(arr, axis=0))  # Sum along columns
