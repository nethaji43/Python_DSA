#Print numbers from 1 to 10
#Stop printing when number is 6
for i in range(1,10):
    if i == 6:
        break
    print(i)

#Print numbers from 1 to 10
#Skip multiples of 3
for i in range(1,10):
    if i == 3:
        continue
    print(i)

#Print only odd numbers from 1 to 20(use continue)
for i in range(1,20):
    if i%2 == 0:
        continue
    else:
        print(i)

#Given a number, extract digits one by one
#Stop when digit 0 is found
num = int(input("Enter a number: "))
while(num > 0):
    rem = num % 10
    print(rem)
    num = num // 10
