n1 = 13; n2 = 22;
a = n1 + n2; s = n1 - n2; m = n1 * n2; d = n1 / n2; dd = n1 // n2; 
a; s; m; d; dd;

n1 = int(input()); n2 = int(input());
a = n1 + n2; s = n1 - n2; m = n1 * n2; d = n1 / n2; dd = n1 // n2; 
print("A = ",a); print("S = ",s); print("M = ",m); print("D = ",d); print("DD = ",dd);

num = [21, 22, 32, 13, 34, 54, 42, 25];
num[:]; num[2]; num[:2]; num[3:]; num[1:4]; len(num); 
num[2] = 23; num.insert(3, 27); num.append(68); num.extend([71, 38, [29, 52, 30], [1, 7]]);
num.pop(); num.pop(3); num.remove(68); num.clear(); del(num);
num.reverse();

print("Hello Mark");
name1 = 'Mark'; print("Hello", name1); 
Greatings = 'Hello' + ' ' + name1 + ' ' + 'How are you?'; Greatings;

name = " Fistum G Mitiku ";
name[:]; name[:7]; name[10:]; name[8:9];
name.capitalize(); name.upper(); name.lower(); name.title(); name.swapcase();
name.strip(); name.rstrip(); name.lstrip(); name.index('G'); name.count('i');
name.replace('G', 'K'); name.find('s'); name.startswith(''); name.endswith('u');
del(name); 
for i in range(len(name)):
    print(i, name[i]);




