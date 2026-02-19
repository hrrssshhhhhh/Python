'''Average Transaction Amount per Customer
Question

Calculate the average transaction amount per customer.

Input'''
data = [
    {"customer": "A", "amount": 200},
    {"customer": "A", "amount": 300},
    {"customer": "B", "amount": 400}
]
total = {}
count = {}
for d in data:
    customer = d["customer"]
    amount = d["amount"]
     
    if customer in total:
        total[customer] += amount
        count[customer] += 1
    else:
        total[customer] = amount
        count[customer] = 1

average = {}
for customer in total:
       average[customer] = total[customer] / count[customer]

print(average)
     
