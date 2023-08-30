class bank:
    def __init__(self, name, money):
        self.name = name
        self.__balance = money
    def depo(self, money):
        self.__balance += money
        return self.__balance
    def w_drow(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Hello "+self.name+", your balance is insufficient!"
    def c_balance(self):
        return self.__balance

cx1 = bank("Mark", 12000)
cx1.w_drow(15000)
cx1.depo(5000)
cx1.c_balance()