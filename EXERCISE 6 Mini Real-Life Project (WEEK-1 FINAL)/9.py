'''Multi-Key Aggregation (ADVANCED WEEK-1)
📂 CSV: orders.csv
customer,product,amount
A,X,200
A,X,150
B,Y,300
A,Y,100

🎯 Task

Calculate total amount per (customer, product) pair.'''

import csv

total = {}

with open("orders1.csv", "r") as file:
     reader = csv.DictReader(file)

     for r in reader:
         customer = r["customer"]
         product = r["product"]
         amount = r["amount"]

         key = (customer, product)
    
         try:
                amount = int(amount)
         except:
                continue
    
         if key in total:
                total[key] += amount
         else:
                total[key] = amount

#The other way to do the same task is:
'''import csv

total = {}

with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    for r in reader:
        key = (r["customer"], r["product"])
        amount = int(r["amount"])

        total[key] = total.get(key, 0) + amount

print(total)'''

print(total)
            
