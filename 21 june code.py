# Python Data Types
x = 5
print(type(x))

""" 
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType

"""
# Python Numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -7.3e2
print(type(x))
print(type(y))
print(type(z))

print(x)
print(y)
print(z)

x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# Type Conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)


print(a)
print(b)
print(c)


print(type(a))
print(type(b))
print(type(c))

"""
Random Number
Python does not have a random() function to make a random number,
 but Python has a built-in module called random that can be used
  to make random numbers:
"""
import random
print(random.randrange(1, 10))

# Multi line Strings

a = """hey
how 
you
"""
print(a)

#Strings are Arrays

a = "Hello, World!"
print(a[1])

# Looping through a string

for i in "love":
    print(i)

# String Length

a = 'hi, my dear'
print(len(a))

# Check String

txt = 'the best things in life are free.'
print('free' in txt)
print('love' in txt)

txt = 'the best things in life are free.'
if 'free' in txt:
    print('yes, "free" is present.')

# Check if NOT

txt = 'the best things in life are free.'
print('expensive' not in txt)

if 'expensive' not in txt:
    print('no, "expensive" is not present')

# Slicing Strings

b = 'hello world'
print(b[2:5])

# Slicing from the start

print(b[:5])

# Slicing to the end

print(b[2:])

# Negative Indexing

print(b[-5:-2])

# Upper Case

a = 'hello, world'
print(a.upper())


# Lower  Case

print(a.lower())

# Removing Whitespace

print(a.strip())

# Replace String

print(a.replace('h', 's'))

# Split String

print(a.split(','))

# String Concatenation

a ='hello'
b = 'world'
c = a+b

print(c)
print(a+" "+b)