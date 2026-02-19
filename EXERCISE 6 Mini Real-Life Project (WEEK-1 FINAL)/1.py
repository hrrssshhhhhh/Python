#Project: Customer Sales Summary

data = [
    {"customer": "A", "amount": 200},
    {"customer": "B", "amount": 300},
    {"customer": "A", "amount": 100},
    {"customer": "C", "amount": 400}
]
'''Tasks
Total spend per customer

Find highest spending customer'''

total = {}

for d in data:
     customer = d["customer"]
     amount = d["amount"]
     if customer in total:
          total[customer] += amount
     else:
          total[customer] = amount

m = max(total, key = total.get)
print(m)
print(total) 

'''max_spend = 0

for customer, spend in customer_total.items():
    if spend > max_spend:
        max_spend = spend
        max_customer = customer
        
print("Highest spender:", max_customer, "with", max_spend)'''