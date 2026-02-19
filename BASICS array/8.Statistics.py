import numpy as np

stats = np.array([[1, 2, 3], [4, 5, 6]])
print(stats)

print("Mean:", np.mean(stats))              # Mean of all elements
print("Mean of columns:", np.mean(stats, axis=0))  # Mean of each column
print("Mean of rows:", np.mean(stats, axis=1))     # Mean of each row

print("Median:", np.median(stats))          # Median of all elements
print("Median of columns:", np.median(stats, axis=0))  # Median of each column
print("Median of rows:", np.median(stats, axis=1))     # Median of each row

print("Standard Deviation:", np.std(stats))   # Standard deviation of all elements
print("Standard Deviation of columns:", np.std(stats, axis=0))  # Std dev of each column
print("Standard Deviation of rows:", np.std(stats, axis=1))     # Std dev of each row

print("Variance:", np.var(stats))          # Variance of all elements
print("Variance of columns:", np.var(stats, axis=0))  # Variance of each column
print("Variance of rows:", np.var(stats, axis=1))     # Variance of each row

print("Minimum:", np.min(stats))          # Minimum of all elements
print("Minimum of columns:", np.min(stats, axis=0))  # Minimum of each column
print("Minimum of rows:", np.min(stats, axis=1))     # Minimum of each row

print("Maximum:", np.max(stats))          # Maximum of all elements
print("Maximum of columns:", np.max(stats, axis=0))  # Maximum of each column
print("Maximum of rows:", np.max(stats, axis=1))     # Maximum of each row

print("Sum:", np.sum(stats))              # Sum of all elements
print("Sum of columns:", np.sum(stats, axis=0))  # Sum of each column
print("Sum of rows:", np.sum(stats, axis=1))     # Sum of each row

