'''Nested Dictionary Creation
Problem

Store total sales and count per product.

sales = [
    {"product": "A", "amount": 200},
    {"product": "A", "amount": 300},
    {"product": "B", "amount": 400}
]'''
sales = [
    {"product": "A", "amount": 200},
    {"product": "A", "amount": 300},
    {"product": "B", "amount": 400}
]

counts = {}
total = {}

for s in sales :
    product = s["product"]
    amount = s["amount"]
    if product in total :
       total[product] += amount
       counts[product] += 1
    else :
       total[product] = amount
       counts[product] = 1
print(total)
print(counts)