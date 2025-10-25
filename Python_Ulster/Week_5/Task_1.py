
# This program demonstrates a function that accepts
# two arguments.

def main():
    print(f'{num1} divided by {num2} is')
    show_division(num1, num2)

# The show_division function accepts two arguments
# and displays their ratio .
def show_division(num1, num2):
    result = num1 / num2
    print(result)

# Call the main function.

num1 = int(input("insert first number: "))
num2 = int(input("insert second number: "))
main()

