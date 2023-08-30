class person:

    def __init__(self, name):
        self.name = name

    def whoami(self):
        return "You are " + self.name +"!"
    
p1 = person('Tom')
print(person.whoami(p1))
print(p1.name)
p2 = person("Betty")
print(person.whoami(p2))
print(p2.name)

p1.name = 'Abebe'; p2.name = 'Marta';
print(person.whoami(p2))
print(p2.name)
print(person.whoami(p1))
print(p1.name)