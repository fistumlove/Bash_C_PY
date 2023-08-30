class toyota():
    def __init__(self, name, model):
        self.__name = name
        self.__model = model
    def getname(self):
        return self.__name
    def setcolor(self, model):
        self.__model = model
    def getmodel(self):
        return self.__model
class suzuki():
    def __init__(self,name, model, color):
        super().__init__(name, model)
        self.__color = color
    def getcolor(self):
        return self.__color

class cars(toyota,suzuki):
    def __init__(self,name, model, color, year):
        super().__init__(name, model, color)
        self.__year = year
    def getyear(self):
        return self.__year
    def getdesc(self):
        return self.getname() + ' ' + self.getmodel() + ' ' + self.__color + ' ' + self.__year + "!"

t = cars("Toyota", "Camery", "White", "1996")
#print(t.getname()); print(t.getmodel()); print(t.getyear()); print(t.getdesc());
"""s = cars("Suzuki", "Desire", "Silver", "2021")
print(s.getname()); print(s.getmodel()); print(s.getyear()); print(s.getdesc());"""
