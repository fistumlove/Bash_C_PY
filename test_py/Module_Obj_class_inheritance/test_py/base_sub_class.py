class X:
    def xx(self):
        return "xx from X class"
class Y:
    def yy(self):
        return "yy from Y class"
class Z(X, Y):
    def zz(self):
        return
    
xyz = Z()
xyz.xx()
print(xyz.yy())
xyz.zz()