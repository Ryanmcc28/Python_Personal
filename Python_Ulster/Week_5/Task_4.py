def is_even(number):
    # determine whether number is even
    #if so return True, otherwise return False

    if (number % 2) == 0:
        status = True
    else:
        status = False
    # end of if statement
    
    return status
#end of function is_even

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def is_too_big(number):
    if number > 100:
        return True
    else:
        return False
    


def main():
    userNumber = int(input("Enter number to be tested: "))

    if is_even(userNumber):
        print("This is an even number")
    else:
        print("This is an odd number")

    if is_negative(userNumber):
        print("This number is negative")
    else:
        print("This number is positive")
    
    if is_too_big(userNumber):
        print("This number is greater than 100")
    else:
        print("This number is less than 100")

main()
    
