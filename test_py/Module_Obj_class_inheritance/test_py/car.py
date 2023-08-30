class car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def getName(self):
        return self.name
    def getColor(self):
        return self.color
    
class vicheal(car):
    def __init__(self, name, model, color):
        super().__init__(name, color)
        self.model = model
    def getCarInfo(self):
        return "It is "+ self.getName() +' '+self.model+" model in "+self.getColor()+" color!"
    
car1 = vicheal("Toyota", "Corolla", "White")
car1.getCarInfo()