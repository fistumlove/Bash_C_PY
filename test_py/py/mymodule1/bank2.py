class Bank:
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money
    def deposit(self, money):
        self.__balance += money
        return self.__balance
    def withdrow(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Hello " + self.__name + "!"+ ' ' + "Your balance is insufficient!"
    def checkbalance(self):
        return self.__balance
c1 = Bank('Mike', 3000)
c1.deposit(300)
c1.withdrow(4000)
c1.checkbalance()
c1.withdrow(1000)
c1.checkbalance()