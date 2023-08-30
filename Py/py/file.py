f = open('t.txt' , 'w'); #Write in file
f.write('Hola!\n');
f.write('Heyyy!\n');
f.close(); # Close the file
f = open('t.txt' , 'a'); #Append the file
f.write('Hi\n');
f.close();
f = open('t.txt' , 'r'); #Read the file
f.read();
f.readline();
f.readlines();

for line in f:
    print(line);
