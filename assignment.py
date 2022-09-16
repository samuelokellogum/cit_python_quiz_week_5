class BankAccount:
    def __init__(self, account_number, balance, owner, type):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type

class Bank:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

class Customer:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

class Transactions:
    def __init__(self, account, amount, type):
        self.account = account
        self.amount = amount
        self.type = type