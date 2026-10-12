import numpy as np

#2D array
array = np.array([   
    [[1,2,3], [2,3,4]],
    [[4,5,6],[2,3,4]]])
word = array[0,0,0] + array[1,1,0]
print(word)
