'''Given CSV file (sales.csv)
date,product,amount
2024-01-01,A,200
2024-01-02,B,300
2024-01-03,A,150
2024-01-04,C,400
🔹 Problem

Read the CSV

Calculate total sales per product'''
import csv
total = {}
with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for r in reader:
         product = r["product"]
         amount = int(r["amount"])

         if product in total:
               total[product] += amount
         else:
               total[product] = amount

print(total)
