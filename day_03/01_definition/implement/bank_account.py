class BankAccount:
    def __init__(self, initial_bal=0):
        self.bal = initial_bal

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        self.bal -= amount

    def print_balance(self):
        print(self.bal)

account = BankAccount()
account.deposit(1000)
account.print_balance()