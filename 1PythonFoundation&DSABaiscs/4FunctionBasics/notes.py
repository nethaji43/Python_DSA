#A function is a reusable block of code that performs a specific task.
def greeting():
    print("Hello World")
#call the function
greeting()

#Parameters & Arguments
#Parameter → variable in function definition
#Argument → value passed during function call
def add(a,b):
    return a+b
print(add(1,2))

#return sends a value back to the caller and ends the function.
def square(num):
    return num*num
print(square(5))
"""
Key Rules
=>Code after return is not executed
=>A function without return returns None
"""

#Python allows returning multiple values using tuples.
def calculate(num1,num2):
    return num1+num2, num1*num2, num2/num1, num2-num1
print(calculate(100,150))

#Scope Basics (Intro)
#Variables inside a function are local.
def demo():
    x = 5
    print(x) #value print here
print(x) #return an error