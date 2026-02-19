'''Q.8 Count Missing Values
Problem

Return number of missing (None) values.

data = [10, None, 20, None, None, 30]'''

data = [10, None, 20, None, None, 30]

def missing_values(data):
    total_missing = 0
    for d in data:
       if d is None:
        total_missing += 1
    return total_missing

print(missing_values(data))