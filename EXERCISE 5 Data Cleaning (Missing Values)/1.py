'''🔹 Problem

Some sales values are missing (None).
Calculate total valid sales.
'''

sales = [200, None, 300, None, 150]
total = 0

for s in sales:
    if s is not None:
        total += s

print("Total valid sales:", total)
