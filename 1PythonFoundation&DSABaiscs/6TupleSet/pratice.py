"""
Create a tuple of 3 numbers
Try changing one value
Observe the error
"""
my_tuple = (1, 2, 3)
print(my_tuple)
print(my_tuple[1])
#my_tuple[1] = 5 TypeError: 'tuple' object does not support item assignment
print(my_tuple)

"""
Create a list with duplicate values
Convert it into a set
Print result
"""
my_list = [1, 2, 3, 1, 2, 3, 5, 4]
covert_set = set(my_list)
print(covert_set)

#Given a set of numbers, check if a number exists
my_set = {1, 2, 3, 1, 2, 3, 5, 4}
if 5 in my_set:
    print("5 is in my_set")

#Count how many unique characters are in a string
my_str = "Hello"
converted_str = set(my_str)
print(len(converted_str))

"""
Given two lists, find how many common elements they have
(Think uniqueness, not counting)
"""
list1 = [1, 2, 3, 1, 2, 3, 5, 4]
list2 = [1, 2, 3, 4, 5, 6]
converted_list1 = set(list1)
converted_list2 = set(list2)
print(len(converted_list1.intersection(converted_list2)))
