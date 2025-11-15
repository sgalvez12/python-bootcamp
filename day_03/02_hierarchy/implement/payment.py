class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def total(self):
        return self.amount


class CreditPayment:
    def __init__(self, amount, limit=10_000):
        self.amount = amount
        self.credit_limit = limit


    def total(self):
        if self.amount > self.credit_limit:
            raise ValueError("Insufficient Funds")

        return self.amount



class OnlinePayment:
    def __init__(self, amount, fee=.1):
        self.amount = amount
        self.fee = fee

    def total(self):
        return self.amount * (1+self.fee)


class DiscountedPayment:
    def __init__(self, amount, discount):
        self.amount = amount
        self.discount = discount


    def total(self):
        return self.amount - self.discount


payments = [
    CashPayment(1_000),
    CashPayment(10_000),
    CreditPayment(11000, 20000),
    OnlinePayment(1000),
    DiscountedPayment(1000, .05)
]

for payment in payments:
    print(payment.total())
