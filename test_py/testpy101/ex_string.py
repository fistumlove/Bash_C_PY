# Python String-Formatters

# % Percent operator
name = "Fistum";
age = 32;
print("Hello %s! You are %s years old." % (name, age))

name = str(input())
age = int(input())
print("Hello %s! You are %s years old." %(name, age))

# f operator
name = "Tom";
age = 22;
sex = 'male';
print(f"Hello {name}! You are {age} years old and your gender is {sex}.")

name = str(input());
age = int(input());
sex = str(input());
print(f"Hello {name}! You are {age} years old and your gender is {sex}.")

# format Method
name = "Betty";
age = 25;
sex = 'female';
print("Hello {0}! You are {1} years old and your gender is {2}." .format(name, age, sex))

name = str(input());
age = int(input());
sex = str(input());
print("Hello {0}! You are {1} years old and your gender is {2}." .format(name, age, sex))


print("Hello {name}! You are {age} years old and your gender is {sex}." .format(name = 'Betty', age = 23, sex = 'female'))

#Python * operator – String Replication operator
x = 3 * "Hi!"
print(x)

#Indexing
name = "Fistum G Mitiku"
name[-2]
len(name)

text = 'Ayushi bought a pen!'
#complete string 
text[:]
'Ayushi bought a pen!'
#beginning to index 6 
text[:7]
'Ayushi '
#index 3 to end
text[3:] 
'shi bought a pen!'
#-2 to -7 left to right is nothing 
text[-2:-7] 
''
#index -7 to -1 left to right
text[-7:-2] 
' a pe'

###
for index in range(len(text)):
    print(index, text[index])

### to removes whitespace
' hello '.strip()

###lower() and upper() in Python
text
'Ayushi bought a pen!'
text.upper()
'AYUSHI BOUGHT A PEN!'
text
'Ayushi bought a pen!'
text.lower()
'ayushi bought a pen!'

### Split
text.split(' ')

### Replace
text.replace('bought','buys')

### Find
text.find('u')

### Join
','.join(['1','2','3'])

###startswith() and endswith() in Python
text.startswith('Ayu')

### max() and min() in Python
max(text)
min(text)

### format() method in Python
cats=10
'She has {} cats'.format(cats)

f'She has {cats} cats'

'She has %d cats' %(cats)

###isdigit(), isalpha(), isalnum() in Python
"""
We can use these methods to check whether a string is completely made of digits, 
alphabetical characters or both.
"""