'''Question

Ignore rows where amount is missing or invalid and calculate total sales per product.'''
import csv

total = {}
with open("sales_dirty.csv", "r") as file:
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

print(total)
