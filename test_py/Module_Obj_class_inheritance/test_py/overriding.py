class A:
    def __init__(self):
        self.__x = 1
    def x(self):
        return "x from A class"
class B(A):
    def __init__(self):
        self.__y = 1
    def x(self):
        return "x from B class"

C = B()
C.x()
D = A()
D.x()