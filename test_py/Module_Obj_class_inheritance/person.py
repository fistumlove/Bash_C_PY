## Class and objects

class person():
    def __init__(self, name): #initializer or constructor
        self.name = name # name is a data field
    def whoami(self):
        return "You are " +' '+ self.name
    
p1 = person('Abebe Kebede')
p1.name
p1.whoami()
