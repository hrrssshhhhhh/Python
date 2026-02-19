'''PROJECT 1: Total Revenue Per Customer (CORE)
📂 CSV: orders.csv
customer,amount
A,200
B,300
A,invalid
C,400
B,100

🎯 Task

Ignore invalid amounts

Calculate total revenue per customer'''

import csv
total = {}

with open("orders.csv", "r") as file:
      reader = csv.DictReader(file)

      for r in reader:
          customer = r["customer"]
          amount = r["amount"]

          try:
                amount = int(amount)
          except:
                continue

          if customer in total:
               total[customer] += amount
          else:
               total[customer] = amount

print(total)
