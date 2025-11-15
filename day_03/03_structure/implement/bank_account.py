class WithdrawError(ValueError):
    pass

class WithdrawError2(ArithmeticError):
    pass

class DepositError(KeyError):
    pass


class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise DepositError("Deposit amount cannot be less than 0")
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise WithdrawError("Enter positive amount")
        if amount > self._balance:
            raise WithdrawError2("Insufficient funds")
        self._balance -= amount

    def print_balance(self):
        print(self._balance)


bank_account = BankAccount(200)
bank_account.deposit(100)
bank_account.withdraw(-1)
bank_account.print_balance()