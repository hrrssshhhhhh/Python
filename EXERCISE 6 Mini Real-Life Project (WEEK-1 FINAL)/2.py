'''MINI PROJECT 1: Daily Revenue Summary (MOST COMMON)
📂 CSV: daily_sales.csv
date,product,amount
2024-01-01,A,200
2024-01-01,B,300
2024-01-01,A,invalid
2024-01-02,A,150
2024-01-02,C,400

🎯 Task

Ignore invalid amounts

Calculate total revenue per day'''

import csv

total = {}

with open("daily_sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for r in reader:
        date = r["date"]
        amount = r["amount"]

        try:
            amount = int(amount)
        except:
            continue
        if date in total:
                total[date] += amount
        else:
                total[date] = amount


      #  total[date] = total.get(date, 0) + amount

print(total)
