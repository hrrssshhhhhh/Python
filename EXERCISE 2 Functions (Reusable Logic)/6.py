'''Q.6 Clean Missing Values
Problem

Remove None values and return clean list.

sales = [200, None, 300, None, 150]'''

sales = [200, None, 300, None, 150]

def missing_vales(sales):
     for s in sales:
       if s == None:
           sales.remove(s)
     return sales
print(missing_vales(sales))


'''or we can use clean 

def clean_sales(sales):
    clean = []
    for s in sales:
        if s is not None:
            clean.append(s)
    return clean

print(clean_sales(sales))

'''