"""
Take a number and print:
"Positive" if > 0
"Negative" if < 0
"Zero" if 0
"""
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

#Print numbers from 1 to N
num = int(input("Enter a number: "))
for i in range(1,num+1):
    print(i)

#Print all even numbers between 1 and 50
for i in range(1,51):
    if i % 2 == 0:
        print(i)

#Count how many digits are in a given number
num1 = int(input("Enter a number: "))
digits = 0
while num1 > 0:
    digits += 1
    num1 = num1//10
print(digits)

"""
Given a number:
Keep dividing by 2
Count how many steps until it becomes 0
"""
num2 = int(input("Enter a number: "))
count = 0
while num2 > 0:
    num2 = num2//2
    count += 1
print(count)
