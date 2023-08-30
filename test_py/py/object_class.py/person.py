
class person():
    def __init__(self, fullname):
        self.fullname = fullname

    def name(self):
        return "Hello " + self.fullname + "!"
name1 = person('Fistum Mitiku')
name2 = person("Mike Tyson")
print(name1.name()); print(name1.fullname);
print(name2.name()); print(name2.fullname);

"""
class Person:

       # constructor or initializer
    def __init__(self, name): 
            self.name = name # name is data field also commonly known as instance variables

      # method which returns a string
    def whoami(self):
           return "You are " + self.name

p1 = Person('tom') # now we have created a new person object p1
print(p1.whoami())
print(p1.name)
"""