###Python string and numbers exersies

###Python string

print("Hello")
name = 'fistum G Mitiku'
name
name[-2]
name[0:6]
print(name)

name = str(input())
age = int(input())
sex = str(input())
print("Hello %s! You are %s years old and your gender is %s." %(name, age, sex))
print(f"Hello {name}! You are {age} years old and your gender is {sex}")
print("Hello {0}! You are {1} years old and your gender is {2}." .format(name, age, sex))
print("Hello {name}! You are {age} years old and your gender is {sex}." .format(name = 'Bruk', age = 32, sex = 'M'))


Msg = "Hello World!";
print(Msg)

Name = input()
Name = 'Hello' + ' ' + Name + ' ' + 'How are you!'
print(Name)

fname, lname = 'Fistum', 'Mitiku';
print(f"Hello {fname} {lname}! How are you?")

name = 'Mark'; sex = 'm'; age = 23;
print("Hello %s! Your gender is %s and you are %s years old!" % (name, sex, age))
print("Hello {0} Your gender is {1} and you are {2} years old!".format (name, sex, age))
print("Hello {name} Your gender is {sex} and you are {age} years old!".format (name = 'Abebe',
sex = 'M', age = 42))

#Another format examples
Lname = 'Mark'
'My last name is %s.' %(Lname) 
f'My last name is {Lname}.'
'My last name is {}.' .format(Lname)


"""
This is a multiple line comment
And the belows are some of phyton string indexed and functions
"""
name = 'fistum G Mitiku'
name[:]; name[:6]; name[9:15]; name[-8]
name.upper(); name.lower(); name.swapcase(); name.split(); max(name); min(name); 
len(name); ':'.join(name); name.replace('G', 'Girum'); name.find('G'); name.strip(); 
name.startswith('f'); name.endswith('s'); name.isalpha(); name.isdigit(); name.isalnum();

#Python if closes and string user inputs
first_name = 'Abebe'
if first_name == 'Abebe':
    print("This is the right customer name!")
elif first_name == '':
    print("This customer name is unknown!")
else:
    print("This is invalid customer name!")


#Loop to find the index of 'name'
for index in range(len(name)):
    print(index, name[index])


###Python Numbers

#Python numbers and user inputs

num = 25;
num += 10;
print(num);

num1 = 10;
num2 = 20;
print("Sum = ", num1 + num2)
sum = num1 + num2;
sum
print(sum)

n1 = int(input())
n2 = int(input())
sum = n1 + n2
print(sum)

#Python if closes and numbers user inputs to compare two numbers
print("Please enter your first number : ")
num1 = int(input())
print("Please enter your second number : ")
num2 = int(input())
if(num1 > num2):
    print("The first number is greater than the second one!")
elif(num1 < num2):
    print("The first number is less than the second one!")
else:
    print("Both values are equal!")




