## Python Control Statements

### If statements
Today = "Sunday"

if Today == 'Sunday':
    print("It is my day off!")
else:
    print("It is my work day!")


### Multiple If statements (if-elif-else statement)
today = "monday"

if today == "monday":
   print("this is monday")
elif today == "tuesday":
   print("this is tuesday")
elif today == "wednesday":
   print("this is wednesday")
elif today == "thursday":
   print("this is thursday")
elif today == "friday":
   print("this is friday")
elif today == "saturday":
   print("this is saturday")
elif today == "sunday":
   print("this is sunday")
else:
   print("something else")



###Nested If statements
Today = "Holiday"
BankBalance = 5000
if Today == "Holiday":
    if BankBalance > 10000:
        print("Go to shopping!")
    else:
        print("Watch Movie!")
else:
    print("Go to your work!")