'''PROBLEM 7: Count Null Values
Problem

Count how many values are missing (None).

data = [10, None, 20, None, 30, None]'''

data = [10, None, 20, None, 30, None]
missing = 0
for i in data:
   if i == None:
       missing += 1
print(missing)