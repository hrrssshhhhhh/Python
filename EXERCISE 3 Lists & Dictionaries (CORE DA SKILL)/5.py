#📌 Pattern: multi-dictionary aggregation
#📌 Interview favorite
'''Average Per Category (INTERVIEW LEVEL)
Problem

Calculate average sales per product.

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
total = {}
counts = {}

for s in sales:
      product = s["product"]
      amount = s["amount"]
      if product in total:
       total[product] += amount
       counts[product] += 1
      else:
       total[product] = amount
       counts[product] = 1

average = {}    # to store average sales per product

for product in total :  # iterate through products in total dictionary
       average[product] = total[product] / counts[product]


print(average)