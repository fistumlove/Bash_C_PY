## Override Methods

class A():
    def __init__(self):
        self.__x = 1
    def m1(self):
        return "M1 in A class!"
class B(A):
    def __init__(self):
        self.__y = 1
    def m1(self):
        print("M1 in B class!")
    
C = B()
C.m1()
D = A()
D.m1()