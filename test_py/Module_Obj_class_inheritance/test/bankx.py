class Bankx:
    def __init__(self, name, money):
        self.name = name
        self.__balance = money
    def deposit(self, money):
        self.__balance += money
        return self.__balance
    def withdrow(self, money):
        if self.__balance < money:
            return "Hello "+self.name+"! Sorry, you have insufficient balance!"
        else:
            self.__balance -= money
            return money
            
    def checkBalance(self):
        return self.__balance
    
x = Bankx('Mr X', 4000)
print(x.withdrow(5000))
print(x.deposit(2000))
print(x.withdrow(5000))
print(x.checkBalance())