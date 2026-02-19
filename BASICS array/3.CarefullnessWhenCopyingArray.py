import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = a
b[0] = 100
print(b)
print(a)  # a is also changed because b is just a reference to a
c = np.array([1, 2, 3, 4, 5])
d = c.copy()
d[1] = 200
print(d) # c is changed
print(c)  # c remains unchanged because d is a copy of c