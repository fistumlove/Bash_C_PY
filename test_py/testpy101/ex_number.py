#Python number operators
x = 10; y = 15; z = 0;
print("Result of z = ", x + y)
print("Result of z = ", x - y)
print("Result of z = ", x * y)
print("Result of z = ", x / y)

#Adding two numbers
num1 = 20;
num2 = 30;
sum = num1 + num2;
print("Sum = ", sum)

#User input
num = int(input());
num = num - 50;
print("sum = ", num)

#Simple python program to compare two numbers
print("Enter your first number : ")
num1 = int(input());
print("Enter your second number : ")
num2 = int(input());
if(num1 < num2):
    print("Num1 is less than Num2!")
elif(num1 > num2):
    print("Num1 greater than Num2!")
else:
    print("Both values are equal!")

#Binary
print(0b100, 0B100) #100 in binary
print(0o100, 0O100) #100 in octal
print(0x100, 0X100) #100 in hexadecimal

#Complex
print( complex(3) )
print( complex(8.5))

X = 4+2j; Y = 2-5j; Z = -5j;
print(X); print(Y); print(Z); type(5-4j)

#X = 4 + j # NameError: name ‘j’ is not defined
Y = 4 + 1j # Valid complex number

#Binary representations
print( bin(20) )
print( bin(4) )

#Octal representations
print( oct(20) )
print( oct(4) )

#Hexadecimal representations
print( oct(10) )
print( oct(5000) )

#Implicity conversion
X = 12; Y = 20.50; Z = X + Y;
print(Z); type(X); type(Y); type(Z)

#Explicity conversion or type casting
print( int(5.25) )
print( int(5.80) )
print( int('456') )
print( int(0b1010) )