import numpy as np

a = np.array([[1, 2 ,3 ,4 ,5 ,6], [7, 8, 9, 10, 11, 12]])

#Get a specific element [row, column]
print("Element at row 1, column 2:", a[1, 2])  # Output: 9
print("Element at row 0, column 4:", a[0, -1])  # Output: 6

#Get a specific row
print("Row 0:", a[0, :])  # Output: [1 2 3 4 5 6
print("Row 1:", a[1, :])  # Output: [ 7  8  9 10 11 12]

#Get a specific column
print("Column 2:", a[:, 2])  # Output: [3 9]
print("Column 4:", a[:, 4])  # Output: [ 5 11]

#Slicing Getting a sub-array little fancy
print(a[0, 1: 5: 2]) # Output: [2 4]
print(a[1, 0: 6: 3]) # Output: [ 7 10]

#Change value of specific element
a[1, 2] = 20 #Change 9 to 20
print("Modified array:\n", a) # Output: [[ 1  2  3  4  5  6], [ 7  8 20 10 11 12]]
a[: , 2] = 5  #Change entire 3rd column to 50
print("Modified array after changing 3rd column:\n", a) # Output: [[ 1  2  5  4  5  6], [ 7  8  5 10 11 12]]
a[:, 2] = [1, 2]  #Change multiple values in 1st row, 3rd column 
print(a) # Output: [[ 1  2  1  4  5  6], [ 7  8  2 10 11 12]]

'''3dimensional array indexing'''
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)

#Get a specific element (work outside in)
print("Element at [0, 1, 1]:", b[0, 1, 1])  # Output: 4
print("Element at [1, 0, 0]:", b[:, 1, :])  # Output: [[3 4], [7 8]]
print("Element at [1, 0, 0]:", b[1, 0, 0])  # Output: 5
print("Element at [1, :, 1]:", b[:, 0, :])  # Output: [[1 2], [5 6]]

#Replace values
b[:, 1, :] = [[9, 9], [8, 8]]  #Change all values in 2nd row to 9 and 8
print("Modified 3D array:\n", b)  # Output: [[[1 2] [9 9]] [[5 6] [8 8]]]