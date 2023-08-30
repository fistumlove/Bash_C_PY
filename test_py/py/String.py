### Python String

##Pyton print string
print("Hello World!");
Name = 'fistum'; print(type(Name)); Name;
fn = 'fistum'; mn = 'g'; ln = 'mitiku'; fns = fn + ' ' + ' ' + mn + ' ' + ln; print(fns); 
fns.upper(); fns.lower(); fns.swapcase(); fns.title();
str(123);


name = 'fistum'; age = 32; sex = 'male';
print(f"Hello {name}! You are {age} years old and your gender is {sex}.");#f method
print("Hello {0}! You are {1} years old and your gender is {2}." .format(name, age, sex));#format
print("Hello %s!. You are %d years old and your gender is %s."%(name, age, sex)); # % method

fname = 'Fistum Mitiku'; f'Hello {fname}! How are you?'; #f method
fname = 'Fistum Mitiku'; 'Hello {}! How are you?'.format(fname); #format method
fname = 'Fistum Mitiku'; 'Hello %s! How are you?'%(fname); # % method

##Python string user input
name = str(input()); age = int(input()); sex = str(input());
print(f"Hello {name}! You are {age} years old and your gender is {sex}"); 
print("Hello {name}! You are {age} years old and your gender is {sex}." .format(name = 'Abebe', age = 25, sex = 'male'));

##Indexing
name = 'Fistum G Mitiku';
name[:]; name[2]; name[-2]; name[7 : 8]; name[-6 : -1];

"""
Strings are immutable and you cannot delete them or update them. 
You can assign a new object to the variable.
Note that: you can delete a complete string with the del keyword, 
but you cannot delete a character or slice.
"""
name = 'Fistum Mitiku'; print(name);
del name[5]; print(name);
del name; print(name);

##Concatnation
fname = 'Fistum'; lname = 'Mitiku'; print(fname + ' ' + lname); 
fname = 'Fistum'; lname = 'Mitiku'; fullname = fname + ' ' + lname; fullname * 3;

#Membership (in and not in)
'Mark' in 'Mitiku'; 'Mark' in 'Market'; 'Mitiku' not in 'Market';

#Python string length
len(name);

for index in range(len(name)):
    print(index, name[index]); # for loop index with length

#Python string method and function
':'.join('ABC'); ' ABC '.strip(); ' ABC'.lstrip(); 'ABC '.strip(); name.swapcase();
name.capitalize(); name.upper(); name.lower(); name.title(); name.find('G'); name.split('i'); 
min(name); max(name); name.replace('G', 'Girum'); name.startswith('T'); name.endswith('u');
name.count('s'); name.isalpha(); name.isdigit(); name.isupper(); name.islower();
