class BankAcc:
    def __init__(self, name, money):
        self.name = name
        self.__balance = money #__balance is a private field and cannot be accessed outside the class
    def deposit(self, money):
        self.__balance += money
        return self.__balance
    def withdrow(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money 
        else:
            return "Sorry " +self.name+ ", you have insufficient balance!"
    def checkbalance(self):
        return self.__balance
    
cx1 = BankAcc('Mark', 5400);
print(cx1.name);
print(cx1.checkbalance());
print(cx1.withdrow(6000));
print(cx1.deposit(3000));
print(cx1.withdrow(800));
print(cx1.checkbalance());

print(cx1.__balance)
