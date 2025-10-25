COMMISSION_RATE = 0.02
NUM_SHARES = 1000
PURCHASE_PRICE = 32.87
SELLING_PRICE = 33.92
profit_made = False

amount_paid_for_stock = NUM_SHARES * PURCHASE_PRICE
purchase_commision = amount_paid_for_stock * COMMISSION_RATE
total_paid = amount_paid_for_stock + purchase_commision
stock_sold_for = 33.92 * 1000
selling_commision = stock_sold_for * COMMISSION_RATE
total_recieved = purchase_commision - selling_commision
if  total_recieved > 0:
    profit_made = True

print("Joe paid " + str(amount_paid_for_stock))
print("Joe paid in commision " + str(purchase_commision))
print("Joe sold for " + str(stock_sold_for))
print("Joe paid in sales commision " + str(selling_commision))
print("Joe earned " + str(total_recieved))
if  profit_made == True:
    print("Joe made a profit")

else:
    print("Joe lost money")

