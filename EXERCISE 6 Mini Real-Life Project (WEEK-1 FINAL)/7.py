'''PROJECT 5: Data Quality Report (REAL COMPANY TASK)
📂 CSV: raw_data.csv
amount
200
invalid

300

🎯 Task

Count:

valid values

invalid values

missing values'''

import csv

valid = invalid = missing = 0

with open("raw_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for r in reader:
        value = r["amount"]

        if value == "":
            missing += 1
            continue

        try:
            int(value)
            valid += 1
        except:
            invalid += 1

print("Valid:", valid)
print("Invalid:", invalid)
print("Missing:", missing)

