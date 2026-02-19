'''PROJECT 4: Count Transactions Per Customer (INTERVIEW FAVORITE)
📂 CSV: transactions.csv
customer,product
A,X
B,Y
A,Y
A,X
C,Z

🎯 Task

Count how many transactions each customer made.'''
import csv
count = {}
with open("transactions.csv", "r") as file:
      reader = csv.DictReader(file)

      for r in reader:
          customer = r["customer"]
        

          if customer in count:
            count[customer] += 1
          else:
            count[customer] = 1


print(count)
