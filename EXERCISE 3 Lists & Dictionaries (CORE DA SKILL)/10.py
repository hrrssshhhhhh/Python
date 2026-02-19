'''Q.10 FINAL CHALLENGE (MUST DO)
Problem

From transaction data:
Total sales per customer
Number of transactions per customer
Highest spending customer
'''
data = [
    {"customer": "A", "amount": 200},
    {"customer": "B", "amount": 300},
    {"customer": "A", "amount": 150},
    {"customer": "C", "amount": 400},
    {"customer": "B", "amount": 100}
]
total = {}
count = {}
for d in data:
  customer = d['customer']
  amount = d['amount']

  if customer in total:
       total[customer] += amount
       count[customer] += 1
  else:
       total[customer] = amount
       count[customer] = 1
   
print(total)
print(count)
highest_spender = max(total, key=total.get)
print(f'Highest spending customer: {highest_spender} with amount {total[highest_spender]}')


