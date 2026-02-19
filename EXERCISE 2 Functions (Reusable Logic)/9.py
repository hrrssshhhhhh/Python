'''Categorize Performance
Problem

Return "LOW", "MEDIUM", "HIGH" based on value.

Rules:

< 200 → LOW

200 - 399 → MEDIUM

≥ 400 → HIGH

sales = 350'''

sales = 350

def return_value(sales):
   
     if sales < 200:
        print("LOW")
     elif sales > 200 and sales < 399 :
        print("MEDIUM")
     else :
        print("HIGH")
     return sales

print(return_value(sales))