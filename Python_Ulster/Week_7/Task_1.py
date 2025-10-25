Jan = int(input("Enter Rainfall for January: "))
Feb = int(input("Enter Rainfall for Febuary: "))
Mar = int(input("Enter Rainfall for March: "))
Apr = int(input("Enter Rainfall for April: "))
May = int(input("Enter Rainfall for May: "))
Jun = int(input("Enter Rainfall for June: "))
Jul = int(input("Enter Rainfall for July: "))
Aug = int(input("Enter Rainfall for August: "))
Sep = int(input("Enter Rainfall for September: "))
Oct = int(input("Enter Rainfall for October: "))
Nov = int(input("Enter Rainfall for November: "))
Dec = int(input("Enter Rainfall for December: "))

rainfall = [Jan, Feb, Mar, Apr, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

total_rainfall = 0

for month in rainfall:
    total_rainfall += int(month)
print(total_rainfall)

avg = sum(rainfall) / len(rainfall)
print(avg)



print(f"The wettest month is {str(rainfall.index(max(rainfall)) + 1)}")
print(f"The driest month is {str(rainfall.index(min(rainfall)) + 1)}")