# this is a bank

class Bank:

    def __init__(self):
        self.accounts = { }

    def withdraw(self, account, amount):
        self.accounts[account] = self.accounts[account] - amount

    def deposit(self, account, amount):
        self.accounts[account] = self.accounts[account] + amount

    def check_balance(self, account):
        return self.accounts[account]

    def create_account(self, account):
        self.accounts[account] = 0

    def transfer(self, account_from, account_to, amount):
        self.accounts[account_to] = self.accounts[account_to] + amount
        self.accounts[account_from] = self.accounts[account_from] - amount

