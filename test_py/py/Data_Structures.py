##Data Structure

#1 Set
name = {'Alx', 'Bety', 'Carl', 'Dany', 'Eric'};
print(type(name)); name; name.add('Frank'); name.pop(); name.remove('Bety'); 
name1 = name.copy(); name1.clear(); del name1; 

#2 List
name1 = ['Aby', 'Berry', 'Candy', 'Don', 'Eyob', 1888, 2015, 2023];
print(type(name1)); name1[0]; name1[1]; name1[2:4]; name1[3:];
name1.append("Fish"); name1.insert(0, 000); name1.extend(['a', 0, ['b', 1]]);
name1.pop(0); name1.pop(); name1.remove('a'); name1.clear(); del name1;
name2 = name1.copy(); name2;
name2.reverse(); name2.count('a'); 

#3 Tuple
name1 = ('Aby', 'Tom', 'Mark', 'Fistum', 'Rose', 'Aby');
name1; print(type(name1)); name1[:]; name1[3]; name1[2:];
name1.count('Aby'); name1.index('Tom'); del name1;

#4 Dictionary
name1 = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3};
print(type(name1)); name1;
name1['B']; name1['D']; name1['E', 4];

#5 String
fn = ' Fistum G Mitiku';
print(type(fn)); fn;
fn.strip(); fn.lstrip(); fn.rstrip(); fn;
fn.capitalize(); fn.upper(); fn.lower(); fn.title(); fn.swapcase();


