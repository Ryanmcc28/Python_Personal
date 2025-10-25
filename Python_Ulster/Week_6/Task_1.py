groceries = open("grocery_list.txt", "r")

list = []

item_1 = input("Add new item 1: ")
item_2 = input("Add new item 2: ")
item_3 = input("Add new item 3: ")
item_4 = input("Add new item 4: ")
item_5 = input("Add new item 5: ")

for line in groceries:
    list.append(line.rstrip("\n"))
list.append(item_1)
list.append(item_2)
list.append(item_3)
list.append(item_4)
list.append(item_5)

for line in list:
    print(line)