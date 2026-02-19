'''Total Sales Per Customer (IMPORTANT)
Problem

Return a dictionary of customer → total spend.

data = [
    {"customer": "A", "amount": 200},
    {"customer": "B", "amount": 300},
    {"customer": "A", "amount": 150}
]'''
data = [
    {"customer": "A", "amount": 200},
    {"customer": "B", "amount": 300},
    {"customer": "A", "amount": 150}
]

def customer_totals(data):
    totals = {}   # empty dictionary creation

    for row in data:    #Loop Through Each Transaction
        name = row["customer"]   #Extract Customer Name & Amount
        amount = row["amount"]

    #Check If Customer Already Exists
    
        if name in totals: #Case 1: Customer Exists → ADD
            totals[name] += amount
        else:              #Case 2: New Customer → CREATE
            totals[name] = amount

    return totals

print(customer_totals(data))
