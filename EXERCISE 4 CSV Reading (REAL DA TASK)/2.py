'''Count number of transactions per customer
Input'''
data = [
    {"customer": "A", "amount": 200},
    {"customer": "B", "amount": 300},
    {"customer": "A", "amount": 150},
    {"customer": "C", "amount": 400},
    {"customer": "B", "amount": 100}
]
count = {}
for d in data:
    customer = d["customer"]
    amount = d["amount"]
   
    if customer in count:
        count[customer] += 1
    else:
        count[customer] = 1

print(count)
