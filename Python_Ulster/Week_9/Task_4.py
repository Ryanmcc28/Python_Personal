class bank_account:
    def __init__(self,name,acc_num,open_balance,over_limit):
        self.name = name
        self.acc_num = acc_num
        self.open_balance = open_balance
        self.over_limit = over_limit
        bank_account.__str__(self)
    def __str__(self):
        print(f"Customer name is {self.name},"
              f" acccount number is {self.acc_num},"
              f" open balance is {self.open_balance}"
              f" and their overdraft limit is {self.over_limit}")
