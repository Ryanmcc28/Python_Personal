names = open("names.txt", "r")

list = []
user_name = input("Enter a name to check: ")
name_count = 0

for name in names:
    list.append(name.rstrip("\n"))
    if name.rstrip("\n").lower() == user_name.lower():
        name_count += 1

print(f"There are {len(list)} names in the list")
print(f"The name {user_name} appears {str(name_count)} times in the list")

