'''Sum of Sales (Warm-up)
Problem

Write a function that returns total sales.
sales = [100, 200, 150, 300]'''
sales = [100, 200, 150, 300]
def total_sales(sales):
    total = 0
    for s in sales:
        total += s
    return total
print(total_sales(sales))