'''Write a function that returns the average sales.'''
sales = [200, 450, 300, 500, 250]

def average_sales(sales):
      total = 0
      for s in sales:
            total += s
      return total / len(sales)
print(average_sales(sales))
