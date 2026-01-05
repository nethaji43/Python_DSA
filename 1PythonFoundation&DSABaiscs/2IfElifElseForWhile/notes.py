#if-elif-else
#Used when execution depends on conditions.
age = 23
if age >= 18:
    print("You are old enough to vote")
else:
    print("you are not enough to vote")
"""
Key Rules
Conditions evaluate to True / False
Only one block runs
elif is optional
else is optional
"""

#Comparison Operators
#==,!=, >, <, >=, <=

#logical operator
"""
and both true
or any one
not reverse
"""
if (age >= 21) and (age < 61):
    print("You are eligible to work")

#for loop
#Used when number of iterations is known.
for i in range(1, 11):
    print(i)

#while loop
#Used when iterations depend on a condition.
n=6
while n>0:
    print(n)
    n=n-1
"""
Always ensure the condition becomes False
Otherwise → infinite loop
"""
