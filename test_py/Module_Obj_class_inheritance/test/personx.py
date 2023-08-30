class student:
    def __init__(self, name):
        self.name = name
        #return self.name
    def fn(self):
        return "Your name is "+self.name

x = student("Aby Lakew")
print(x.name)
print(x.fn())