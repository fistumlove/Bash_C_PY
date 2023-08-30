class student:

    def __init__(self, name):
        self.name = name
    def newStu(self):
        return "Hello " + self.name + "! You are our new student!"
    
stu1 = student('Abebe')
print(student.newStu(stu1))
print(stu1.name)

stu1.name = "Abebe Tola" 
print(student.newStu(stu1))
print(stu1.name)

stu2 = student('Belay Zeleke')
print(student.newStu(stu2))
print(stu2.name)
