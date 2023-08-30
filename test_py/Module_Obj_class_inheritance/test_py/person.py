class student:
    def __init__(self, name):
        self.name = name
        return 
    def stuName(self):
        return "Hello "+ self.name +"!"

s1 = student("Abebe")

print(s1.name)
print(s1.stuName())