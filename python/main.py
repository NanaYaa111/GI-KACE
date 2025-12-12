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

student_id =set()

# student_id_input = int(input("Enter student ID: "))
# student_id.add(student_id_input)
# print("Your student ID has been added. Thank you!: ", student_id)

#Dictionaries in Python
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, 
#changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and have
# keys and values:
#Dictionary items are ordered, changeable, and does not
# allow duplicates.
#Dictionary items are presented in key:value pairs, and 
#can be referred to by using the key name.
#Dictionaries are changeable, meaning that we can change,
# add or remove items after the dictionary has been created.
#Dictionaries cannot have two items with the same key:
#Dictionaries can be of any data type:

#Creating a dictionary
student_profile = {
    "name": "Miracle",
    "complexion": "Dark",
    "age": 12,
    }
print(student_profile)  
print(type(student_profile))
print(len(student_profile))  # Get the number of items in the dictionary                   

#Accessing dictionary items
print(student_profile["complexion"])  #Access the value of the key "complexion"
student_profile["age"]=13  #Modify the value of the key "age"
print(student_profile)

#Adding items to a dictionary
student_profile["gender"]="Female"
print(student_profile)

#Removing items from a dictionary
student_profile.pop("complexion")
print(student_profile)

#student_profile.clear()
#print(student_profile)

#del student_profile
#print(student_profile) 


#OPERATORS IN PYTHON
#Arithmetic Operators
#Assignment Operators
#Comparison Operators
#Logical Operators
#Identity Operators
#Membership Operators
#Bitwise Operators

#Arithmetic Operators
# +, -, *, /, %, **, //
# print(10 + 20)
# print(10 - 20)
# print(10 * 20)
# print(10 / 20)
# print(10 % 20)
# print(10 ** 20)
# print(10 // 20)

#Assignment Operators
# =, +=, -=, *=, /=, %=, **=, //=
# x = 10
# x += 10
# print(x)

#Comparison Operators
# ==, !=, >, <, >=, <=
# print(10 == 10)
# print(10 != 10)
# print(10 > 10)
# print(10 < 10)
# print(10 >= 10)
# print(10 <= 10)

#Logical Operators
# and, or
# print(10 > 5 and 5 < 10)
# print(10 > 5 or 5 > 10)
# print(not(10 > 5))
#Identity Operators
# is, is not
# x = ["apple", "banana"]
# y = x
# print(x is y)
# print(x is not y)
#Membership Operators
# in, not in
# fruits = ["apple", "banana", "cherry"]
# print("banana" in fruits)
# print("orange" not in fruits)
#Bitwise Operators
# &, |, ^, ~, <<, >>
# print(10 & 20)
# print(10 | 20)
# print(10 ^ 20)
# print(~10)
# print(10 << 20)
# print(10 >> 20)
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)
# assign 10 to a
a = 10

# assign 5 to b
b = 5 

# assign the sum of a and b to a
a += b      # a = a + b

print(a)

# Output: 15

a = 5

b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

#Conditional Statements in python
# if, elif, else statements
# The if statement used to test a specific condition. 
# If the condition is true, a block of code (if-block) is executed.
#If the condition is false, the if-block is skipped. 

#The syntax of an if statement is:
# if condition:
#     #block of code to be executed if the condition is true


# If statement to ask user to enter a age of a person 
# who is eligible to vote

#Else statement is used to execut a block of code
#  when the condition is false.


age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to cast your vote.")
else:
    print("You are not eligible to cast your vote.")

#Elif statement is used to check multiple conditions.
# The elif statement is short for "else if",
# and is used to check multiple conditions in an if-else statement.
# The syntax of an elif statement is:   
# if condition1:
#     #block of code to be executed if condition1 is true
# elif condition2:
#     #block of code to be executed if condition2 is true
# else:
#     #block of code to be executed if both condition1 and condition2 are false
marks = int(input("Enter your marks: "))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
elif marks>=50:
    print("Grade E")  
else:
    print("Grade F")
    
#Example of elif statement 
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("You got A+ grade.")
elif marks >= 80:
    print("You got A grade.")
elif marks >= 70:
    print("You got B+ grade.")
elif marks >= 60:
    print("You got B grade.")
elif marks >= 50:   
    print("You got C grade.")
else:
    print("You failed the exam. Better luck next time.")