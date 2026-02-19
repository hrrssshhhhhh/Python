'''Q.7 Total Sales After Cleaning
Problem

Combine cleaning + summing.

sales = [200, None, 300, None, 150]'''

sales = [200, None, 300, None, 150]

def total_clean_sales(sales):
    total = 0
    for s in sales:
        if s is not None:
            total += s
    return total

print(total_clean_sales(sales))
