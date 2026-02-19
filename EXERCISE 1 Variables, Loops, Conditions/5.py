'''🧪 PROBLEM 4: Count Categories
Problem

Count how many orders are Online vs Store.

orders = ["Online", "Store", "Online", "Online", "Store", "Store"]'''
orders = ["Online", "Store", "Online", "Online", "Store", "Store"]
countOnline = 0
countStore = 0
for i in orders:
    if i == "Online" :
        countOnline += 1
    else:
        countStore += 1
print("Number of orders Online" ,countOnline)
print("Number of orders on store:" ,countStore)
