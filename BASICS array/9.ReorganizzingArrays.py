import numpy as np

before = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print("Before:\n", before)

after = before.reshape((8, 1)) # Reshape to 8 rows and 1 column
print("After:\n", after)


