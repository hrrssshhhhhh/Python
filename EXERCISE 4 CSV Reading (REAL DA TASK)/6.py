'''QUESTION 6 (DATA CLEANING + AGGREGATION)
Ignore missing amounts (None) and compute totals'''
data = [
    {"product": "A", "amount": 200},
    {"product": "B", "amount": None},
    {"product": "A", "amount": 150},
    {"product": "C", "amount": 400}
]
total ={}


for d in data:
      product = d["product"]
      amount = d["amount"]

      if amount is None:
           continue

      if product in total:
          total[product] += amount
      else:
          total[product] = amount

print(total)
  

