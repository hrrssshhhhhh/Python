'''FULL REAL-LIFE EXAMPLE using dirty.csv'''
import csv
total = {}

with open("dirty.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for r in reader:
        product = r["product"]
        amount = r["amount"]

        try:
            amount = int(amount)
        except:
            continue

        total[product] = total.get(product, 0) + amount

print(total)
