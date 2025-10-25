from os import remove


def main():

    found = False

    search = input("Enter a description to search for: ")

    coffeeFile = open("coffee.txt", "r")

    for line in coffeeFile:
    
        strippedLine = line.strip()
        descr, roast, type, qty = strippedLine.split(",")

        if descr == search:
            print("Description:", descr)
            print("Roast:", roast)
            print("Type:", type)
            print("Quantity:", qty)

            found = True
    coffeeFile.close()

    if not found:
        print("That item was not found in the file.")

main()

