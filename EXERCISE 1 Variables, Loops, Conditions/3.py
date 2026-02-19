'''Problem

Some values are invalid (-1).
Calculate total valid revenue.

revenue = [300, -1, 450, 600, -1, 200]'''
revenue = [300, -1, 450, 600, -1, 200]

total = 0
for i in revenue:
    if i != -1:
        total += i
print(total)
