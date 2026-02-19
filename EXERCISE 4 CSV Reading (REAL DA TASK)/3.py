'''QUESTION 3 (MOST ASKED)
Total sales per customer
'''
data = [
    {"customer": "A", "amount": 200},
    {"customer": "B", "amount": 300},
    {"customer": "A", "amount": 150},
    {"customer": "C", "amount": 400},
    {"customer": "B", "amount": 100}
]



totals = {}

for row in data:
    cust = row["customer"]
    amt = row["amount"]

    if cust in totals:
        totals[cust] += amt
    else:
        totals[cust] = amt

print(totals)
