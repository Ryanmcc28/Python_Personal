print('Would you like to search or add')
choice = input("s for search, a for add: ").lower()

if  choice == 's':
    import search_coffee_records
if choice == 'a':
    import add_coffee_record
