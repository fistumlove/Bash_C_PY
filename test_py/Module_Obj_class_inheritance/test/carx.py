class vicheal:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def getBrand(self):
        return self.brand
    def getModel(self):
        return self.model
    def getYear(self):
        return self.year
class car(vicheal):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color
    def getCarInfo(self):
        return self.getBrand()+" brand new "+self.getModel()+" "+self.getYear()+" model in "+self.color+" color!"

x = car("Toyota","Corolla","2023","White"); print(x.getCarInfo());