'''Clean the Data
data = [200, None, 300, None, 150]'''
data = [200, None, 300, None, 150]
cleaned = []
for d in data:
    if d is not None:
        cleaned.append(d)

print("Cleaned data count:", cleaned)