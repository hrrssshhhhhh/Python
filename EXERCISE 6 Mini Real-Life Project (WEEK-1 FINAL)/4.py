'''PROJECT 2: Daily Revenue Summary (VERY COMMON)
📂 CSV: daily_sales.csv
date,amount
2024-01-01,200
2024-01-01,invalid
2024-01-02,300
2024-01-02,150

🎯 Task

Ignore invalid values

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

        if amount in total:
          total[date] += amount
        else:
          total[date] = amount

print("Total Revenue Per Day is:", total)