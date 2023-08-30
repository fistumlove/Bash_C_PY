# Local and Global variables

#Global variables
num = 10;
def func():
    global num
num += 20;
print(num)

#Local variables
count = 3;
def func():
    count = 10;
    count += 5;
    print(count)

func()
print(count)

#Nonlocal variables
def func1():
    achievements=9
    def func2():
            nonlocal achievements
            achievements+=2
            print(achievements)
    func2()

func1()

#Local scope variables
a = 10
def function():
    print("Hello")
    b = 20;
function()
print(a)
#print(b)

#Global scope variables
Msg = "This is declared globally"

def function():
  #local scope of function
  print(Msg)

function()


msg = "global variable"

def function():
  #local scope of function
  msg = "local variable"
  print(msg)

function()
print(msg)

#Enclosing scope variables (fun = start, is an enclosing scope)
def vehicle():
  fun= "Start"
  def car():
    model= "Toyota"
    print(fun)
    print(model)
  car()
vehicle()

#Built in scope variables (It always check local, enclosing, global finally the built-in variables)
#int, type, print is a built in variable
a = 5.5
int(a)
print(a)
print(type(a))

#Global Keyword
a = 100
def method():
  a = 50
  print(a)
method()
print(a)

a = 100
def method():
  global a
  a = 50
  print(a)
method()
print(a)

#NonLocal Keyword
a = "global variable"
def method():
        a = "nonlocal variable"
        def function():
                a = "local variable"
                print(a)
        function()
        print(a)
method()
print(a)

a = "global variable"
def method():
        a = "nonlocal variable"
        def function():
                nonlocal a
                a = "local variable"
                print(a)
        function()
        print(a)
method()
print(a)


#var1 is in the global namespace
var1 = 5
def function():

    # var2 is in the local namespace
    var2 = 6
    def inner_function():

        # var3 is in the nested local
        # namespace
        var3 = 7
function()

var = "10"
def example():
  var = "30"
  def method():
    global var
    var = "40"
    def function():
      global var
      var = "50"
      print("Function Scope: " + var)
    function()
    print("Method Scope: " + var)
  method()
  print("Example Scope: " + var)
example()
print("Module Scope: " + var)