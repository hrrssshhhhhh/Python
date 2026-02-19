'''PROJECT 3: Product Filter + Aggregation (BUSINESS LOGIC)
📂 CSV: products.csv
product,amount
A,100
B,300
A,250
C,400

🎯 Task

Only include amounts > 200 after aggregation

Calculate total per product'''

import csv
total = {}
include = {}
with open("products.csv", "r") as file:
      reader = csv.DictReader(file)

      for r in reader:
          product = r["product"]
          amount = r["amount"]

          try:
                amount = int(amount)
          except:
                continue

         
          if product in total:
                    total[product] += amount
          else:
                    total[product] = amount

          if amount > 200:
                include[product] = total[product]
          else:
                include[product] = 0                 


print(total)

          
# without aggregation
'''   if amount > 200:
                total[product] += amount
      else:
                total[product] += 0'''