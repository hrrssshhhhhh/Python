'''Calculate average customer rating.

ratings = [4, 5, 3, 4, 2, 5]'''
ratings = [4, 5, 3, 4, 2, 5]
total = 0
for i in ratings:
   total += i

avg = total/len(ratings)
print(avg)
       