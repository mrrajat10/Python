class account_info:
    def __init__(self, balance, account):
        self.bal = balance
        self.account = account

    def debit(self, amount):
        self.bal -= amount
        print(f"Your {amount} is debited!")
        print(f" your total balance is {self.get_total()}")

    def credit(self, amount):
        self.bal += amount
        print(f"Your {amount} is debited!")
        print(f" your total balance is {self.get_total()}")

    def get_total(self):
        return self.bal


a = account_info(122322, 993223)
a.debit(2203)
a.credit(23234)
