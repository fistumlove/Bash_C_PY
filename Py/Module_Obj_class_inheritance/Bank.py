## Multiple functions and methods 

class BankAccount():

    def __init__(self, name, money):
        self.__name = name
        self.__balance = money
    def Deposit(self, money):
        self.__balance += money
        return self.__balance
    def Withdrow(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Sorry "+self.__name+","+" Your balance is insufficient!"
    def checkBalance(self):
        return self.__balance
    
cx1 = BankAccount("Abebe", 8000)
cx1.checkBalance()
cx1.Deposit(2000)
cx1.Withdrow(11000)
cx1.Withdrow(4000)
cx1.checkBalance()
