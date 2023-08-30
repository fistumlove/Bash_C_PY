f = open('', 'r'); f.read(); f.readline(); f.readlines();
f = open('', 'w'); f.write(); 
f = open('', 'a'); f.write();
f = open('', 'r');
for line in f:
    print(line);
f.close();
