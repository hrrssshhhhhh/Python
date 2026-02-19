'''Read a CSV file and calculate total sales per product.
Return the result as a dictionary.

CSV (sales.csv)
product,amount
A,200
B,300
A,150
C,400
B,100'''
import csv

total ={}

with open("sales2.csv", "r") as file:
    reader = csv.DictReader(file)

    for r in reader:
      product = r["product"]
      amount = int(r["amount"])

      if product in total:
          total[product] += amount
      else:
          total[product] = amount

print(total)
  
