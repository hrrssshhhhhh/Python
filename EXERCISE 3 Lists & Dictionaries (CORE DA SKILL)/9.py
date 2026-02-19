'''Q.9 Merge Two Dictionaries (REAL TASK)
Problem

Merge online & store sales.
'''
online = {"A": 200, "B": 300}
store = {"A": 150, "C": 400}

combined = {}
for k, v in online.items():  # k stands for key and v stands for value k = A, v = 200
    combined[k] = v

for k, v in store.items():
    if k in combined:
         combined[k] += v   
    else:
         combined[k] = v

print(combined)
         