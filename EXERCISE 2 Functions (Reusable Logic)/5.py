'''Q.5 Max Sales Day
Problem

Return the maximum sale value.

sales = [120, 340, 560, 230]'''

sales = [120, 340, 560, 230]

def max_value(sales):
     max = sales[0]
     for s in sales:
        if s > max:
            max = s 
     return max

print(max_value(sales))