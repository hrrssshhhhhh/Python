'''Q.3 Sum Values by Category (VERY IMPORTANT)
Problem

Calculate total sales per product.'''


sales = [
    {"product": "A", "amount": 200},
    {"product": "B", "amount": 300},
    {"product": "A", "amount": 150},
    {"product": "C", "amount": 400}
]
product_total = {}

for s in sales :
     product = s["product"]
     amount = s["amount"]
     if product in product_total:
          product_total[product] += amount
     else :
          product_total[product] = amount

print(product_total)
    
     
