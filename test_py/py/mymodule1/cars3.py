class Toyota():
    def Corolla(self):
        return "This is Toyota Corolla model 2023!"
class Suzuki():
    def Desire(self):
        print("This is Suzuki Desire model 2022!")
class cars(Toyota, Suzuki):
    def NewCars(self):
        print("New Car!")

c = cars()
c.Corolla()
c.Desire()
c.NewCars()

class A():
    def __init__(self):
        self.__x =1
    def m1(self):
        print("m1 from A!")
class B(A):
    def __init__(self):
        self.__y =1
    def m1(self):
        print("m1 from B!")
c = A()
c.m1()

isinstance()