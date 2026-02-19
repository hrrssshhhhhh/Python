'''Average of Valid Values'''
data = [100, None, 300, None, 500]
total = 0
count = 0
for d in data:
    if d is not None:
       total += d
       count += 1
   

print(total/count)