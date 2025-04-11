import numpy as np

#numpy array
''' np.array(data[sequential|Iterative], dtype= object, ndim) '''

# data = range(1,10)
# arr = np.array(data, dtype=complex)
# print(arr)

lst = [[1,2,3,4,5]]
arr = np.array(lst) #ndmin= 0
print(arr)
print('Dimension:', arr.ndim)
print('Shape:',arr.shape)