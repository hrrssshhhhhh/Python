'''FINAL CHALLENGE (INTERVIEW LEVEL)
Problem

Write ONE function that:

Removes None

Returns average of valid values

sales = [100, None, 300, None, 500]'''

sales = [100, None, 300, None, 500]

def average_valid_values(sales):
    count = 0
    total = 0
    for s in sales :
       if s is not None:
          total += s
          count += 1

    if count == 0:
        return 0
    
    return total / count

print(average_valid_values(sales))