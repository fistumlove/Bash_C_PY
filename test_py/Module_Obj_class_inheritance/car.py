## Python inheritance

class Vicheal(): ## Vicheal is a Base or Parent or Super class
    def __init__(self, name, color):
        self.__name = name  # __name is private to Vehicle class
        self.__color = color
    def getName(self):
        return self.__name  # getName() is accessible outside the class
    def setColor(self, color):
        self.__color = color
    def getColor(self):
        return self.__color  # getColor() function is accessible to class Car
    
class Car(Vicheal): ## Car is a Subclass or Child or Drived class
    def __init__(self, name, model, color):
        super().__init__(name, color) # call parent constructor to set name and color  
        self.model = model
    def getCarInfo(self):
        return "This is "+self.getName()+' '+self.model+" in "+ self.getColor()+" color!"
    

"""in method getDescrition we are able to call getName(), getColor() 
because they are accessible to child class through inheritance"""
    
car1 = Car("Toyota", "Corolla", "White")
car1.getName(); car1.getColor(); car1.getCarInfo();
car2 = Car("Suzuki", "Desire", "Silver")
car2.getName(); 
car2.getColor(); # car has no method getName() but it is accessible through class Vehicle
car2.getCarInfo();