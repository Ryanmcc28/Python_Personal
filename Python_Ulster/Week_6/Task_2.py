from numpy.ma.extras import average

contents = open("stock.txt", "r")

stocks = []

for row in contents:
    stocks.append(float(row.rstrip("\n")))
print(len(stocks))
print(max(stocks))
print(min(stocks))
print(f"{average(stocks):.2f}")