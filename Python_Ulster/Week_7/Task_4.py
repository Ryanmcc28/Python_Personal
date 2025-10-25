item1 = input("Enter item 1: ")
item2 = input("Enter item 2: ")
item3 = input("Enter item 3: ")
item4 = input("Enter item 4: ")


item_list = [item1, item2, item3, item4]

for item in item_list[:]:
    if  item == "":
        item_list.remove(item)


def format(item_list):
    if  len(item_list) == 1:
        return str(item_list[0])
    elif len(item_list) == 2:
        return str(f"{item_list[0]} and {item_list[1]}")
    elif len(item_list) == 3:
        return str(f"{item_list[0]}, {item_list[1]} and {item_list[2]}")
    elif len(item_list) == 4:
        return str(f"{item_list[0]}, {item_list[1]}, {item_list[2]} and {item_list[3]}")

print(format(item_list))