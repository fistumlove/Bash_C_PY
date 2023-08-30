
##Python File handling

#Open and read file
f = open('/home/fistum/py.txt', 'r')
f.read()
f.readline()
f.readlines() #to read all lines
f.close()


#Open and write file
f = open('/home/fistum/py.txt', 'w')
f.write("\nHello Fistum!\nThis is your first python test file.")
f.close()

f = open('/home/fistum/Documents/py/hello.py', 'w')
f.write('print("Hello World!")')
f.close()


#Open and append file
f = open('/home/fistum/py.txt', 'a')
f.write('\nIn this file I am tring to read, write and append txt files by using python code!')
f.close()

#Looping through the data using for loop
f = open('/home/fistum/py.txt', 'r')
for line in f:
    print(line)

f.close()
