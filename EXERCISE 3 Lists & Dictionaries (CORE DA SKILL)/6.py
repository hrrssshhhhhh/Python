'''Find Highest Category Value
Problem

Find the product with highest total sales.'''
totals = {'A': 350, 'B': 300, 'C': 400}
m = max(totals, key=totals.get)
print(m, totals[m])  