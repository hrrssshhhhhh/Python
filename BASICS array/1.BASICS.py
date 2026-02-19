import numpy as np

#a = np.array([1, 2, 3])  #1 Dimensional Array
a = np.array([1 , 2, 3], dtype='int16')
b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])  #2 Dimensional Array

c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])  #3 Dimensional Array

print("Array a:")
print(a)
print("Array b:")
print(b)
print("Array c:")
print(c)

#Dimensions of array
print("Dimensions of array a:", a.ndim)
print("Dimensions of array b:", b.ndim)
print("Dimensions of array c:", c.ndim)

#Shape of array
print("Shape of array a:", a.shape)
print("Shape of array b:", b.shape)
print("Shape of array c:", c.shape)

#Data type of array elements
print("Data type of array a:", a.dtype)
print("Data type of array b:", b.dtype)
print("Data type of array c:", c.dtype)

#Size of each element in bytes
print("Size of each element in array a:", a.itemsize, "bytes")
print("Size of each element in array b:", b.itemsize, "bytes")
print("Size of each element in array c:", c.itemsize, "bytes")

#Total Size of the array in bytes
print("Total size of array a:", a.nbytes, "bytes")
print("Total size of array b:", b.nbytes, "bytes")
print("Total size of array c:", c.nbytes, "bytes")

#Total number of elements in the array
print("Total number of elements in array a:", a.size)
print("Total number of elements in array b:", b.size)
print("Total number of elements in array c:", c.size)