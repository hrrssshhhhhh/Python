'''You are given daily sales.
Count how many days had sales ≥ 500.

sales = [450, 600, 700, 300, 520, 480, 900]'''

sales = [450, 600, 700, 300, 520, 480, 900]
count = 0
for sale in sales:
    if (sale >= 500):
       count +=1
print("Number of Days sale is greater than equal to 500:", count)

  


        
        