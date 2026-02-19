import numpy as np
a = np.array([[1, 2 ,3 ,4 ,5 ,6], [7, 8, 9, 10, 11, 12]])

#All 0s matrix
zeros_array = np.zeros(5)
print("Zeros Array:\n", zeros_array)
print(np.zeros((2, 3)))  #2D array of shape 2x3

#All 1s matrix
ones_array = np.ones((3, 4))
print("Ones Array:\n", ones_array)
print(np.ones((4, 2, 2)))  #3D array of shape 4x2x2

#Any other number
full_array = np.full((2, 3), 7) #2D array of shape 2x3 filled with 7s
print("Full Array with 7s:\n", full_array) 
print(np.full((3, 2, 2), 99))  #3D array of shape 3x2x2 filled with 99s

'''Identity Matrix'''
identity_matrix = np.eye(4) #4x4 Identity matrix
print("Identity Matrix:\n", identity_matrix)
print(np.identity(3))  #3x3 Identity matrix

#Number of terms as a but value is ours 
print(np.full_like( a, 10)) #Create an array with same shape as 'a' filled with 10s
print(np.full(a.shape, 4)) #Create an array with same shape as 'a' filled with 4s

#Random decimal numbers between 0 and 1
random_array = np.random.rand(2, 3) #2D array of shape 2x3 with random decimals
print("Random Array:\n", random_array)
print(np.random.random_sample(a.shape)) #Random array with same shape as 'a'

#Random integers between a given range
random_integers = np.random.randint(1, 10, size=(3, 4)) #3x4 array with random integers from 1 to 9
print("Random Integers Array:\n", random_integers)
print(np.random.randint(5, size=a.shape)) #Random integers from 0 to 4 with same shape as 'a'