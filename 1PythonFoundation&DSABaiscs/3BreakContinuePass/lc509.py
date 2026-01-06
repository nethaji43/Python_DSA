n = int(input())
if n == 0:
     print(0)
elif n == 1:
    print(1)
else:
    first = 0
    second = 1
    total = 0
    for i in range(1,n):
        total = first + second
        first = second
        second = total
    print(total)