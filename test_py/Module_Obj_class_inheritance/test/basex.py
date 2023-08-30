class p1:
    def f1(self):
        return "I am f1 from p1"
class p2:
    def f2(self):
        return "I am f2 from p2"
class p3(p1, p2):
    def f3():
        return
x = p3()
print(x.f1())
print(x.f2())