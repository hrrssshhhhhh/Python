import numpy as np

#Repeating the array

arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)  #Repeat along rows
print("Repeating along rows:\n", r1) 
r1 = np.repeat(arr, 4, axis=1)  #Repeat along columns
print("Repeating along columns:\n", r1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
r2 = np.repeat(arr2, 2, axis=0)  #Repeat along rows
print("Repeating along rows:\n", r2)
r2 = np.repeat(arr2, 3, axis=1)  #Repeat along columns
print("Repeating along columns:\n", r2)