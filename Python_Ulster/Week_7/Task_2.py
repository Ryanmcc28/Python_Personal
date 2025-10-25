account = open("charge_accounts.txt", "r")

nums = []
for row in account:
    nums.append(row.strip())

print(nums)


def check(nums):
    for account in nums:
        user_num = int(input("Enter account to charge: "))
        if user_num == int(account):
            print("Success!!!")
            return True
        else:
            print("Fail!!!")
            return False

valid = check(nums)

while not valid:
    check(nums)