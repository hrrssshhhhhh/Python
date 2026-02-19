'''You are given a list of items.
Find the first element that appears only once.
'''
items = ["A", "B", "A", "C", "B", "D"]
counts = {}

for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
for item in items:
    if counts[item] == 1:
        print(item)
        break
 
