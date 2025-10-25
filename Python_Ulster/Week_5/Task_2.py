
# This program simulates 25 tosses of a coin.
import random

tosses = int(input("Enter number of tosses: "))


def main():
    coin(tosses)
#end of main function    

def coin(tosses):
    heads = 0
    tails = 0
    for toss in range(tosses):
        # Simulate the coin toss.
        if random.randint(1, 2) == 1:
            print('Heads')
            heads += 1
            
        else:
            print('Tails')
            tails += 1
    print(f"Number of heads = {heads}")
    print(f"Number of tails = {tails}")

        # end of if statement
     #end of for loop   
#end of coin function

            
# Call the main function.
main()


