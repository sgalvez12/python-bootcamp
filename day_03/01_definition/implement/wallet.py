class Wallet:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

wallet1 = Wallet(200)
print(wallet1.amount)

wallet2 =Wallet(300)
print(wallet2.amount)