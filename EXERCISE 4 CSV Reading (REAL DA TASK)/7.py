'''QUESTION 7 (FIRST NON-REPEATING – CLASSIC)'''
items = ["A", "B", "A", "C", "B", "D"]
count = {}


for i in items:

      if i in count:
          count[i] += 1
      else:
          count[i] = 1

for i in items:
    if count[i] == 1:
        print(i)
        break

  
