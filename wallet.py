# wallet.py

class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):    
        test = self.balance - amount
        if test < 0:
            raise InsufficientAmount
        else:
            self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount