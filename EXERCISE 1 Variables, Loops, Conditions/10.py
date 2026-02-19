'''Count even and odd transactions.

transactions = [101, 202, 303, 404, 505]'''
transactions = [101, 202, 303, 404, 505]
oddTransaction = 0
evenTransaction = 0
for number in transactions:
    if number % 2 == 0:
         evenTransaction += 1
    else :
         oddTransaction += 1

print("number of oddT :" ,oddTransaction)
print("number of event:" ,evenTransaction)
