'''Problem 1 :
You are given daily website visits.
Count how many days had more than 100 visits.

visits = [120, 80, 150, 90, 200, 60]'''

visits = [120, 80, 150, 90, 200, 60]

count = 0
for visit in visits:
    if visit > 100:
        count += 1
print("Number of days with more than 100 visits:", count)
