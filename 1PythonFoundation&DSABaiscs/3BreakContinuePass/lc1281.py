n = int(input())
product = 1
digits = 0
while n > 0:
    remainder = n % 10
    product *= remainder
    digits += remainder
    n = n // 10
print(product - digits)