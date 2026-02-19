'''Write a function that counts days where sales ≥ 250.

sales = [100, 300, 200, 400, 250]'''
sales = [100, 300, 200, 400, 250]

def count_high_days(sales):
    count = 0
    for s in sales:
        if s >= 250:
            count += 1
    return count

print(count_high_days(sales))
