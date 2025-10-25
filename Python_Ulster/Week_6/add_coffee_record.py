# This program adds coffee inventory records to
# the coffee.txt file.

def main():
    # Create a variable to control the loop.
    another = 'y'

    # Open the coffee.txt file in append mode.
    coffee_file = open('coffee.txt', 'a')

    # Add records to the file.
    while another == 'y':
        # Get the coffee record data.
        print('Enter the following coffee data:')
        desc = input('Description: ')
        roast = input('Roast:')
        type = input('Type:')
        qty = int(input('Quantity (in kg): '))

        # Append the data to the file.

        coffee_file.write(f"{str(desc) + ','}{str(roast) + ','}{str(type) + ','}{str(qty) + '\n'}")

        # Determine whether the user wants to add
        # another record to the file.
        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ').lower()

    # Close the file.
    coffee_file.close()
    print('Data appended to coffee.txt.')

# Call the main function.
main()



        
