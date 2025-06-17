#iterating over a list
fruits = ['apjple', 'banana', 'mango', 'strawberry']
for fruit in fruits:
    print(fruit)
#iterating over a list using for loop and range
fruits = ['apple', 'banana', 'mango', 'strawberry']
for fruit in range(len(fruits)):
    print(fruit)
# list comprehension
fruits = ['apple', 'banana', 'mango', 'strawberry']
[print(fruit) for fruit in fruits]
#iterating over a dictionary, this mthd accesses keys of the dictionary
course = {'name' : 'python', 'instructor' : 'Ashley'}
for x in course:
    print(x)
#accessing values of a dictionary
for x in course:
    print(course[x])
# accessing values using values mthd
for y in course.values():
    print(y)
#accessing keys using keys mthd
for x in course.keys():
    print(x)
#accessing keys and values at the same time
for x, y in course.items():
    print(x, y)
#use of for loop with else
fav_languages = ['python','c','java','ruby']
for lang in fav_languages:
    if 'java' == lang:
        print('i like java')
        break
else:
    print('i dont like java')
#the break statement
numbers = list(range(0, 100))
for i in numbers:
    if i > 5:
        break
    print(i)
#while True:
#i =input('enter a to quit loop')
#if i == 'a':
#break
#print(i)

#use the Continue statement
for i in range(5):
    if i == 2 or i == 4:
        continue
    print(i)
n = 0
while n <= 10:
    n += 1
    if n % 2 != 0:
        continue
    print(n)
# nested for loop
list1 = [1,2,3]
list2 = [4,5,6]
for i in list1:
    for j in list2:
        print(i, j,end=' ')
    print()
# nested while loop
list1 = [1,2,3]
list2 = [4,5,6]
i = 0
while i < len(list1):
    j = 0
    while j < len(list2):
        print(list1[i], list2[j],end=' ')
        j += 1
    print()
    i += 1

#PYTHON SPECIAL PROGRAMS

li = list(range(1,25))
even_numbers = []
odd_numbers = []
for item in li:
    if item % 2 == 0:
        even_numbers.append(item)
    else:
        odd_numbers.append(item)
print(odd_numbers)
print(even_numbers)

#print the right triangle number pattern

rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j,end=' ')
    print()

n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# print multiplication table pattern

rows = 5
for i in range(1,rows+1):
    for j in range(1,i+1):
        square = i * j
        print(square,end=' ')
    print()

# full pyramid of stars

rows = 5
for i in range(1, rows+1):
    for space in range(1, rows - i + 1):
        print(end=' ')
    for star in range(1, i+1):
        print('*',end=' ')
    print()


