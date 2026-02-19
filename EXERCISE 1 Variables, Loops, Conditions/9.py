'''Find the first day sales crossed 1000.

sales = [400, 600, 900, 1100, 1300]'''
sales = [400, 600, 900, 1100, 1300]
day = 0
for i in sales:
   day += 1
   if i > 1000:
      print("Crossed on Day:", day)
      break
