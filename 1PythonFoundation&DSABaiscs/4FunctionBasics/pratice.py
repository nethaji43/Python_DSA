#Write a function that takes a number and returns its square.
def square(num):
    return num * num
print(square(5))

"""
Write a function that takes two numbers and returns:
sum
difference
product
"""
def func(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2
print(func(1,2))

#Write a function that checks whether a number is positive, negative, or zero
#Return the result as a string.
def number_is(num1):
    if num1>0:
        return "Positive"
    elif num1<0:
        return "Negative"
    else:
        return "Zero"
num1 = int(input("Enter number: "))
print(number_is(num1))

#Write a function that takes a list of numbers and returns:
#total sum
#maximum value
def sum_max(List):
    return max(List), sum(List)
print(sum_max([2,3,4,5,6,7,8,9]))

def m_sum_max(List):
    total = 0
    max = List[0]
    for i in range(len(List)):
        total += List[i]
        if max < List[i]:
            max = List[i]
    return total, max
print(m_sum_max([2,3,4,5,6,7,8,9]))

#Write a function that counts how many digits are in a number.
def digit_count(num):
    digit = 0
    while num>0:
        remainder = num % 10
        digit += 1
        num = num // 10
    return digit
print(digit_count(123))
num = "120.22"
print(num.split("."))

