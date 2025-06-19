print('hello world, Ashley!')
import sys

print(sys.version)

# python indentation, it will give you an error
if 5 > 2:
    print('five can be good')

#python variables
x =5
y = 'Hey Ashraf'

# comments start with # and python ignores them
#This is a comment
print("Hello, World!")
print("Hello, World!") #This is a comment
#print("Hello, World!")
print("Cheers, Mate!")

#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#python variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# type casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# get the type or print the type
x = 5
y = "John"
print(type(x))
print(type(y))

# single or double quotes are the same
x = "John"
# is the same as
x = 'John'

# Case-sensitive, a != A
a = 4
A = "Sally"
#A will not overwrite a

# Python variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#illegal variable names
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""
# Assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Variable inside a function is local, and outside the function is global
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Global keyword, global allows the variable to work both local in the function, and global
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)