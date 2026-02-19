'''You are given daily profits.
Count profitable days
Count loss days
profits = [200, -50, 300, -100, 400, 0]'''
profits = [200, -50, 300, -100, 400, 0]
profitDay = 0
lossDay = 0
nonProfitNonLossDay = 0
for i in profits:
    if i > 0:
      profitDay += 1
    elif i == 0:
      nonProfitNonLossDay += 1
    else:
      lossDay += 1
print("Number of Profit Days :" ,profitDay)
print("Number of Loss Days:" ,lossDay)
print("Number of Non-Profit Non-Loss Days:" ,nonProfitNonLossDay)
