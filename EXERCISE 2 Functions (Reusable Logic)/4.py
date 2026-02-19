'''Q3. Average Sales (Core DA Question)
Problem

Return the average of sales.

sales = [200, 450, 300, 500, 250]'''

sales = [200, 450, 300, 500, 250]

def average_sales(sales):
   if len(sales) == 0:
        return 0
   
   total = 0
   for s in sales:
      total += s
   return total/len(sales)
print(average_sales(sales))