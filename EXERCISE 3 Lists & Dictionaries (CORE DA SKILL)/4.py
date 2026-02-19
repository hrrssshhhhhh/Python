'''Count Records Per Category
Problem

Count number of transactions per product.'''
sales = [
    {"product": "A", "amount": 200},
    {"product": "B", "amount": 300},
    {"product": "A", "amount": 150}
]
counts = {}
for s in sales:
      product = s["product"]
      amount = s["amount"]
      if product in counts:
        counts[product] += 1
      else:
        counts[product] = 1

print(counts)

