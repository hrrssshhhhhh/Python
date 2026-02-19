'''CSV QUESTION 7: Multi-Column Aggregation (ADVANCED DA TASK)
CSV (orders.csv)
customer,product,amount
A,X,200
B,Y,300
A,X,150
A,Y,100
C,X,400
Question:
Calculate total amount per (customer, product) pair.'''
import csv
total = {}

with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for r in reader:
      key = (r["customer"], r["product"])
      amount = int(r["amount"])

      total[key] = total.get(key,0) + amount

print(total)

    
