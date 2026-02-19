import numpy as np

a = np.ones((2 , 3))
print(a)

b = np.full((3 , 2), 2)
print(b)

'''print(a*b) ''' # Element-wise multiplication will work only if the shapes are compatible/same.

c = np.dot(a, b) 
print(c)

#OR

d = a.dot(b)
print(d)

#OR

e = np.matmul(a, b)
print(e)


'''Find the Determinant of a matrix'''

f = np.identity(3)
f = np.linalg.det(f)
print(f)


'''## Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.Linalg.html)
# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc ...'''