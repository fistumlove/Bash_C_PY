class Vicheals:

    def __init__(self, name, color):
        self.__name = name
        self.__color = color
    def getName(self):
        return self.__name
    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color
class Car(Vicheals):
    def __init__(self, name, model, color):
        super().__init__(name, color)
        self.__model = model
    def getDescription(self):
        return "It is " +self.getName()+' '+"model"+' '+self.__model+' '+self.getColor()+' '+"Color!"
t1 = Car("Toyota", "Corolla", "White")
print(t1.getDescription())
print(t1.getName())

