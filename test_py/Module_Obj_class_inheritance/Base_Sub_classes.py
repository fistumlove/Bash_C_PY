## Multiple inheritance

class super1:
    def superX(self):
        return "This is super number 1 class!"
class super2:
    def superY(self):
        return "This is super number 2 class!"
class child(super1, super2):
    def superchild(self):
        return self.superchild
    
Base = child()
Base.superX()
Base.superY()