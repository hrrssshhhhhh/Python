'''You are given customer purchases.
Find total spend per customer.

transactions = [
    {"customer": "A", "amount": 200},
    {"customer": "B", "amount": 300},
    {"customer": "A", "amount": 150},
    {"customer": "C", "amount": 400},
    {"customer": "B", "amount": 100}
]'''

transactions = [
    {"customer": "A", "amount": 200},
    {"customer": "B", "amount": 300},
    {"customer": "A", "amount": 150},
    {"customer": "C", "amount": 400},
    {"customer": "B", "amount": 100}
]


customer_total = {}
 
for t in transactions :
    name = t["customer"]
    amount = t["amount"]

    if name in customer_total:
        customer_total[name] += amount
    else:
        customer_total[name] = amount

print(customer_total)
