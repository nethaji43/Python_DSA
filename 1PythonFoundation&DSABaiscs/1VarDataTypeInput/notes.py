#variable
#A variable is just a name that points to a value in memory.
x = 10
name = "nani"
is_active = True
"""
Rules:
No need to declare type
Python decides type automatically
Variables are references, not boxes
"""

a = 10
b = a
a = 20
print(b) #print 10 not 20


#Data Types
#int
number = 10
print(number)
#float
Float = 1.224
print(Float)
#str
name = "nani"
print(name)
#bool only true or flase
is_active = True
print(is_active)

#input & output
age = input()
print(age)
#input() always returns string
print(type(age))
#convert your input() data type
age1 = int(input())
print(type(age1))

#coding based knowledge
a, b = input().split()
"""
split() is seperate values by whitespace by default
we can seperate values by our own
example split(",")
"""
print(a)
print(b)
#convert input into another datatype
a, b = map(int,input().split())
#map(function, iterables) will be iterate iterables and excute the function
"""
input()        → "10 20 30"
split()        → ['10', '20', '30']
map(int, ...)  → [10, 20, 30]
"""

#type() used to check datatype of a variable
a = True
print(type(a))
