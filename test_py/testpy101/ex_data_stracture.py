##The data structures in Python are lists, tuple, dictionaries, sets, and strings. 

###Note that : Mutable you can change their calues. Immutable you cannot change their values.

#Lists in Python (Mutable)
groceries=['milk','eggs']
groceries[0]
groceries[1]
groceries.append('meat') #Adding items in Python using append method
groceries.extend(['ham', 'tea', 'bread']) #Adding items in Python using extend method
'meat' in groceries #Checking membership using in or not in
groceries
groceries[-1]
len(groceries)

groceries[1:4] #Slicing in Python
groceries[-3:-1]

groceries[4] = 'coffee' #Modifying in Python
groceries

del groceries[5] #Deleting in Python
groceries

groceries.remove('milk') #Removing in Python
groceries

groceries.pop() #Which removes the last item in the list

groceries.extend(['milk', 'chees', 'yogurt'])


### Looping in Python
for item in groceries:
    print(item)

###Concatenating in Python
[1,2,3]+[4,5]

users = ['A', 'B', 'C','D']
groceries[0:4] + users[0:4] 
groceries[0:4] + users[0:4] * 2 # we can multiply too

###Coping in python
groceries.copy()
list(groceries)

###Nested lists and comprehension in Python
nums=[1,2,[3,4],5]
nums[0:3]
nums=[num for num in range(7)] #we can also create a list quickly 
nums

##Python Tuples (Immutable)
"""Note that: 
Tuples are almost the same with Lists except the following difference:
Tuples are immutable so we cannot add items to them.
Tuples are immutable so we cannot modify elements.
You can delete a complete tuple but you cannot delete elements from it.
"""
groceries=('milk','eggs')

nums=tuple([1,2,3]) #you can also create with Tuples function
nums


##Sets and frozensets in Python
"""
Sets are collections of values and are "unordered", "heterogeneous", "not indexed" and 
"do not hold duplicate elements".
You can create a set with curly braces {} and separating elements with commas.
You can perform operations on sets like union, intersection and set-difference.
frozensets are immutable sets. They can be used as keys for dictionaries– 
regular sets can’t be used.
"""
myset={1, 2.0, False}
set([1, 2.0])

myset.add(4) # Adding item
myset
myset.update([7, 9]) #Updating item
myset
myset.discard(7) # Deleting item
myset.remove(4)
myset.pop()
myset.clear()
#Frozenset
frozenset((1,2,3))

###Python Dictionaries
"""
Note that:
Dictionaries are unordered mutable and indexed collections of items.
Dictionaries have key-value pairs. They are created in curly braces. 
Dictionary keys are unique and immutable.
"""
groceries={'milk':25, 'eggs':15}
groceries
groceries['milk'] # Indexing
groceries.get('eggs') # Accessing elements
groceries['eggs']=30 # Changing item
groceries['cheese']=30 # Adding item
groceries.pop('eggs') # Removing item
groceries.popitem()
del groceries['cheese']
groceries.clear() # Removing all items
groceries=dict([(1,2),(3,4)]) # You can create dictioneries with dict function
#Dictioneries Looping
for key,value in groceries.items():
    print(key,value)

dict1={'a': {'a':1, 'b':2}, 'c':3} # Nesting loops