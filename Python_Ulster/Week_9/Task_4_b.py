from Week_9.Task_4 import bank_account

name = input("Enter username: ")
account_num = input("Enter account num: ")
opening_bal = input("Enter opening balance: ")
overdraft_limit = input("Enter overdraft limit: ")

user_account = bank_account(name, account_num, opening_bal, overdraft_limit)