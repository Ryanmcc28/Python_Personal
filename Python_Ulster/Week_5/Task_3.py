def fahrenheit(temp):
    #convert centigrade to fahrenheit
    #using standard formula
    result = temp*1.8 +32
    return result
# end of fahrenheit function

def centigrade(temp):
    #convert fahrenheit to centigrade
    #using standard formula
    result = (temp-32)* (5/9)
    return result
# end of centigrade function

choice = input("do you want to calculate celcius(C) or fahrenheit(F): ").lower()

if choice == "c":
    temp = int(input("Enter Temp: "))
    print(centigrade(temp))
elif choice == "f":
    temp = int(input("Enter Temp: "))
    print(fahrenheit(temp))
