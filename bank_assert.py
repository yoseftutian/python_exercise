class bank_account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        assert amount > 0, "Deposit amount must be greater than zero."
        assert self.balance + amount <= 5000, "Cannot deposit more than 5000 a day."
        self.balance += amount

    def withdraw(self, amount):
        assert amount > 0, "Withdrawal amount must be greater than zero."
        assert self.balance - amount >= 0, "Insufficient funds for withdrawal."
        assert amount <= 5000, "Cannot withdraw more than 5000 a day."
        self.balance -= amount


yosef = bank_account()
eyal = bank_account()
yosef.deposit(2000)
#account.deposit(4000)
eyal.deposit(300)
print(f"Current balance: {yosef.balance}")
print(f"Current balance: {eyal.balance}")
