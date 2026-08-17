class Account:

    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = balance

    def deposit(self, value_deposit):
        self.balance += value_deposit

    def withdraw(self, value_sake):
        self.balance -= value_sake

    def __str__(self):
        return f"name: {self.name} | account: {self.account} | balance: {self.balance}"