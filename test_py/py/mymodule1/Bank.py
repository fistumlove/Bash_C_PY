class BankAccount:
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money #.__balance is a private data field 
    def deposit(self, money):
        self.__balance += money
    def withdrow(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return 'Insuffisunet fund!' 
    def checkbalance(self):
        return self.__balance
    
b1 = BankAccount('Abebe', 1000)
print(b1.withdrow(1100))
b1.deposit(3000)
print(b1.withdrow(800))
print(b1.checkbalance())
print(b1.deposit(45000))
print(b1.withdrow(50000))
print(b1.checkbalance())
    