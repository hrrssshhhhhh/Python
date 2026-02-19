import numpy as np
'''output
1 1 1 1 1 1
1 0 0 0 0 1
1 0 9 0 0 1
1 0 0 0 0 1
1 1 1 1 1 1 '''

output = np.ones((5, 5), dtype=int)
print(output)

z = np.zeros((3, 3), dtype=int)
z[1, 1] = 9

output[1:-1, 1:-1] = z #OR output[1:4, 1:4] = z
print(output)