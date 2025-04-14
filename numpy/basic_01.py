import numpy as np

' numpy array '
# np.array(data[sequential|Iterative], dtype= object, ndim)

# data = range(1,10)
# arr = np.array(data, dtype=complex)
# print(arr)

# lst = [1,2,3,4,5,6,7,8,9]
# arr = np.array(lst) #ndmin= 0
# print(arr)
# print('Dimension:', arr.ndim)
# print('Shape:',arr.shape)
# arr.shape = 3,3 #element should be validate shape
# print(arr)

' arange(start, stop, step) '
# data = np.arange(1,10, 0.5)
# print(data)

' linspace(start, stop, number of sample) '
# data = np.linspace(1,2,1000)
# print(data)

' min, max, around '
# arr = np.array([2.5, 3.99, 4.5464, 7.89])
# print(np.max(arr))
# print(np.min(arr))
# print(np.around(arr))

' MATRIX '
m1 = [[1,2,3], [4,5,6]]
m2 = [[4,5,6], [1,2,3]]
arr1 = np.array(m1)
arr2 = np.array(m2)

if arr1.shape == arr2.shape:
    res = np.add(arr1, arr2)
    print('\nMatrix 1:')
    print(arr1)
    print('\nMatrix 2:')
    print(arr2)
    print('\nAddition:')
    print(res)
else:
    print('Not valid Dimensions for addition')