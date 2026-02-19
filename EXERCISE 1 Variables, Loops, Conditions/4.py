'''Find the highest temperature recorded.

temps = [32, 35, 30, 38, 36, 31]'''

temps = [32, 35, 30, 38, 36, 31]

highest_temp = temps[0]
for t in temps:
    if t > highest_temp:
        highest_temp = t
print("Highest temperature recorded:", highest_temp)
