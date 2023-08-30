class a:
    def __init__(self):
        self.__x = 1
    def x(self):
        return "I am x from a class"
class b(a):
    def __init__(self):
        self.__y = 1
    def x(self):
        return "I am x from b class"
c = b()
c.x()
d = a()
d.x()