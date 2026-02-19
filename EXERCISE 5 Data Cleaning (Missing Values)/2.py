'''Count Missing Values'''
data = [10, None, 20, None, 30]
missing = 0

for d in data:
   if d is None:
      missing += 1

print(missing)