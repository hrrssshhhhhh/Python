'''CSV QUESTION 6: Filter by Condition (BUSINESS LOGIC)
Question

Only include sales greater than 200, then calculate totals per product.'''
import csv

total = {}

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for r in reader:
        product = r["product"]
        amount = int(r["amount"])

        if amount <= 200:                                    
            continue

        if product in total:
            total[product] += amount
        else:
            total[product] = amount


    '''if amount <= 200:
            total[product] = total.get(product, 0) + amount'''
#One-line explanation (INTERVIEW READY)
#This line safely accumulates values in a dictionary by initializing missing keys to zero and adding the current amount.



print(total)