class car:
    def __init__(self, brand, year, price):
        self.__brand = brand
        self.__year = year
        self.__price = price
    def Toyota(self):
        return self.__brand 
    def Price(self):
        return self.__price 
    def Year(self):
        return self.__year
t1 = car("Camery", 1996, 20000)
t1.Toyota(); t1.Price(); t1.Year();
t2 = car("Corolla", 2023, 40000000)
t2.Toyota(); t2.Price(); t2.Year();
t3 = car("Hylux", 2011, 1000000)
t3.Toyota(); t3.Price(); t3.Year();