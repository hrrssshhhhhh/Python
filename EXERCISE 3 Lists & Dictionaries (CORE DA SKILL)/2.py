'''Count Occurrences (Warm-up)
Problem

Count how many times each product appears.

products = ["A", "B", "A", "C", "B", "A"]'''

products = ["A", "B", "A", "C", "B", "A"]
'''
total_A = 0
total_B = 0
total_C = 0

for p in products :
     if p == "A":
       total_A += 1
     
     elif p == "B"  :
       total_B += 1

     else :
       total_C += 1

    

print(total_A)
print(total_B)
print(total_C)
'''
counts = {}
for p in products :
    if p in counts :
       counts[p] += 1
    else :
       counts[p] = 1
      
print(counts)