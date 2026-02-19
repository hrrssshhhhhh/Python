#📌 Pattern: conditional filtering
#📌 Used in: threshold reporting

'''Filter Dictionary Based on Condition
Problem

Keep only products with total sales ≥ 350.

totals = {'A': 350, 'B': 300, 'C': 400}'''
totals = {'A': 350, 'B': 300, 'C': 400}
filtered = {}
for product, value in totals.items():
    if value >= 350:
        filtered[product] = value

print(filtered)  