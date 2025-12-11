#Commenting is important for code readability and maintenance.
# There are two types of comments in Python: single-line comments and 
# multi-line comments.
# Single-line comments start with the hash character (#) and 
# extend to the end of the line.
# Multi-line comments can be created using triple quotes (''' or """).


#Variables in python
'''Variables are used to store data in Python. 
They are created when you assign a value to a name. 
Variables can be of different types, 
such as integers, floats, strings, and booleans. 
Variables are case-sensitive, 
so myVar and myvar are considered different variables.

There are rules for naming variables in Python. These includes:
1. Variable names must start with a letter 
or the underscore character.
2. Variable names cannot start with a number.
3. Variable names can only contain alpha-numeric characters 
and underscores (A-z, 0-9, and _ ).
4. Variable names are case-sensitive 
(age, Age and AGE are three different variables).
5. Variable names cannot be any of the Python keywords.'''


'''Data types in Python:'''
'''string, float, integer, complex, list, tuple, dictionary, set, boolean'''
my_string = "Hello, World!"  # This variable holds a string value
my_float = 3.14  # This variable holds a float value
my_integer = 42  # This variable holds an integer value
my_complex = 2 + 3j  # This variable holds a complex number
my_list = [1, 2, 3, 4, 5]  # This variable holds a list
my_tuple = (1, 2, 3)  # This variable holds a tuple
my_dictionary = {"key1": "value1", "key2": "value2"}  # This variable holds a dictionary
my_set = {1, 2, 3}  # This variable holds a set
my_boolean = True  # This variable holds a boolean value

# Variables

x=5
print(x)
#Check the type of variable
print(type(x))


_firstname_ = "Alice"
print(_firstname_)
print(type(_firstname_))

abc_123=12.5
print(abc_123)
print(type(abc_123))

ABC_123=3+4j
print(ABC_123)
print(type(ABC_123))


#Lists in Python: Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data,
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets: [].
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0],
# the second item has index [1] etc.

# When we say that lists are ordered, it means that the items have a defined order,
# and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# The list is changeable, meaning that we can change, add,
# and remove items in a list after it has been created."""

# Since lists are indexed, lists can have items with the same value.
# To determine how many items a list has, use the len() function.
# To add an item to the end of the list, use the append() method.
# To add an item at the specified index, use the insert() method.
# To remove an item from the list, use the remove() method.
# To remove an item at the specified index, use the pop() method.
# To remove all items from the list, use the clear() method.

healthy_fruits = ["Guava","Mango", "Pineapple", "Grapes", "Tomato", "Strawberry"]
print(healthy_fruits)
print(type(healthy_fruits))
print(len(healthy_fruits))  # Get the number of items in the list

#List in another list
healthy_vegetables = ["Carrot","Onion", "Garlic", "Broccoli", "Spinach"]
healthy_foods = [healthy_fruits, healthy_vegetables]
print(healthy_foods)
print(type(healthy_foods))
print(len(healthy_foods))  # Get the number of items in the outer list

#Accessing list items
#You access list items by referring to the index number.
print(healthy_fruits[0])  #Access the first item in the list
print(healthy_fruits[2])  #Access the third item in the list
print(healthy_fruits[-1])  #Access the last item in the list
print(healthy_fruits[-3])  #Access the third last item in the list
print(healthy_foods[0][1])  #Access the second item in the first list
print(healthy_foods[1][3])  #Access the fourth item in the second list
print(healthy_foods[0]) #Access the first list

#Slicing lists
#You can return a range of items by specifying where to start and where to end the slice.
cars = ["Ford", "BMW", "Volvo", "Audi", "Toyota","Chevrolet", "Honda"]
print(cars)
print(cars[1:5])
print(cars[-4:-1])
print(cars[2:])
print(cars[:3])
print(cars[:])

#Modifying list items
#You can change the value of a specific item by referring to its index number.
cars[5] = "Mercedes Benz"
print(cars)

#How to add items to the end of a list
cars.append("G-Wagon")
print(cars)

# How to insert an item at the specified index
cars.insert(4, "Lexus")
print(cars)

#How to remove an item from the list
cars.remove("Audi")
print(cars)

#How to remove an item at the specified index
cars.pop(4)
print(cars)

#How to remove an entire list
#del cars
#print(cars) #This will raise an error because the list has been deleted

#How to clear all items from a list
cars.clear()
print(cars)

#Tuples in Python: Tuples are used to store multiple items in a single variable.
#Tuples are one of 4 built-in data types in Python used to store collections of
#data, the other 3 are List, Set, and Dictionary, all with different qualities and 
# usage. Tuples are written with round brackets. ()
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0],
#the second item has index [1] etc.
#When we say that tuples are ordered, it means that the items have a defined order,
#and that order will not change.
#If you add new items to a tuple, the new items will be placed at the end of the tuple.
#The tuple is unchangeable, meaning that we cannot change,
#add, or remove items in a tuple after it has been created."""


sneakers = ["Nike", "Adidas", "Puma", "Reebok", "Vans", "Converse"]
print(sneakers)
print(type(sneakers))
print(len(sneakers))  # Get the number of items in the list

#Accessing Tuple items
print(sneakers[0])  #Access the first item in the list
print(sneakers[-5]) 


#Slicing Tuples
print(sneakers[0:3])
print(sneakers[-4:-1])


#Modifying Tuple items
#Tuples are unchangeable, meaning that we cannot change,
#add, or remove items in a tuple after it has been created.
#However, you can convert the tuple into a list,make changes,and convert it back to a tuple.
#sneakers["Nike"]= "New Balance"  #This will raise an error because tuples are unchangeable
#print(sneakers)

# Convert the tuple into a list
sneakers = list(sneakers)
print(sneakers)
sneakers[5]="New Balance"
print(sneakers)
sneakers=tuple(sneakers)
print(sneakers)
print(type(sneakers))


#Sets in Python: Sets are used to store multiple items in a single variable.
#Sets are written with curly brackets. {}
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Set items can appear in a different order every time you use them,
#and cannot be referred to by index or key.
#Sets are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can add new items.
#Sets are unordered, so you cannot be sure in which order the items will appear.
#Sets cannot have two items with the same value.
#Sets can be any data type, string, integer and boolean.
#Sets are defined as objects with the data type 'set':
#<class 'set'>
#Sets are unordered, so you cannot be sure in which order the items will appear.
#Sets are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can add new items.
#Sets cannot have two items with the same value.
#Sets can be any data type, string, integer and boolean.
#Sets are defined as objects with the data type 'set':

#Creating a set
political_parties = {"NPP", "GCPP", "PPP", "CPP", "NDC"}
print(political_parties)
print(type(political_parties))
print(len(political_parties))  # Get the number of items in the set

#Accessing Set items. Note indexing has no meaning in set data type
#You cannot access items in a set by referring to an index or key,
#print(political_parties[0])  #This will raise an error because sets are unordered

#Adding items to a set
political_parties.add("New force")
print(political_parties)

#Modifying items in the set is not possible
#political_parties[0]="DPP"  #This will raise an error because sets are unchangeable
#print(political_parties)

#Removing items from a set
political_parties.remove("CPP")
print(political_parties)