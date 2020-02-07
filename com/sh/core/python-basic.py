'''
Created on 05-Feb-2019

@author: impadmin
'''
print("Hello, World!")
print("---------------------------")

if 5 > 2:
  	print("Five is greater than two!")
#This condition will not be pass
if 5 < 2:
	print("Five is less than two!")
print("---------------------------")
"""This is a 
multiline docstring."""
print("multiline docstring:")
print("---------------------------")

#Python variables
x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type and can even change type after they have been set.
x = 4 # x is of type int
x = "Sally" # x is now of type str
print("x: "+ x) #print Sally
print("---------------------------") 

#If you try to combine a string and a number, Python will give you an error:
x = 5
y = "John"
#print(x + y)  #Run time error

"""Python Numbers
There are three numeric types in Python:
int
float
complex
Variables of numeric types are created when you assign a value to them"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
print("---------------------------")

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
print("---------------------------")

#Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
print("---------------------------")

#Python Casting
"""Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number) literal, or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals"""

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#String Literals
"""Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string."""
a = "Hello, World!"
print(a[1])

#Substring. Get the characters from position 2 to position 4:
print(a[2:4])

#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(len(a))
print(a.lower())
print(a.upper())
a = "Hello, World! Hai hai"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
print("---------------------------")

#Command-line String Input
print("Enter your name:")
#x = raw_input()
print("Hello, " + x)
print("---------------------------")

#Modulus
x = int(11)
y = int(3)
print(x%y)
print("---------------------------")

#Python Logical Operators
"""
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)"""

#Python Identity Operators
"""Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:"""
"""
is 	Returns true if both variables are the same object	x is y	
is not	Returns true if both variables are not the same object	x is not y
"""

#Python Membership Operators
"""
in 	Returns True if a sequence with the specified value is present in the object		x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
"""

f = ["apple", "banana"]
print("banana" in f)
print("mango" in f)
print("mango" not in f)


#Python Collections (Arrays)
"""There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""

the_list = ["apple", "banana", "cherry"]
print(the_list)
print("---------------------------")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
print("---------------------------")

"""
The list() Constructor
It is also possible to use the list() constructor to make a list. To add an item to the list use append() object method. To remove a specific item use the remove() object method. The len() function returns the length of the list.
"""
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
thislist.append("damson")
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.insert(1,"mango")
thislist.append("banana")
print(thislist)
thislist.sort()
print(thislist)
#count() Returns the number of elements with the specified value
print(thislist.count("banana"))
print("---------------------------")


#Tuple
"""A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets."""
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
#You cannot change values in a tuple:
#thistuple[1] = "blackcurrant" # test changeability
#print(thistuple)
