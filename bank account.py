import datetime
import pytz


class Account:
    ''' Simple account class with balance '''

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))

    def withdraw(self, amount):
        if self.balance >= amount:  # to avoid being a millionaire...
            self.balance -= amount
        else:
            print("The amount must be <= than the current balance, which is: {}".format(self.balance))

    def show_balance(self):
        print("Balance is: {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


chaim = Account("Chaim", 0)
chaim.deposit(100)
chaim.show_transactions()
