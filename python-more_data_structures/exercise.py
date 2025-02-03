class Account:
    def __init__(self, owner, balance = 0):
        self.__owner = owner
        self.__balance = balance
    @property
    def owner(self):
        return self.__owner
    @property
    def balance(self):
        return self.__balance
    def deposit(self, amount):
        if not isinstance(amount,(int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Added amount must be >= 0.")
        self.__balance += amount
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount > self.balance:
            raise ValueError(f"You cannot withdraw more than {self.balance}")
        self.__balance -= amount
    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposit(amount)
    def __str__(self):
        return f"Account Owner: {self.owner}, Balance: ${self.balance}"
    def __dict__(self):
        return{
            "Owner" : self.owner,
            "Balance" : self.balance
        }
acc1 = Account("Alice", 500)
acc2 = Account("Bob", 200)
acc1.transfer(acc2, 200)
print(acc1.__dict__())
print(acc2)
