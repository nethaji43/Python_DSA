#Create a list of numbers from 1 to 5
#Print each element using a loop
nums1 = [1,2,3,4,5]
for i in nums1:
    print(i)

"""
Take a list and:
Append a number
Pop the last element
Print final list
"""
nums2 = [1,2,3,4,5,6]
nums2.append(7)
nums2.pop()
print(nums2)

"""
Given a list, print:
First element
Last element
Middle element (if exists)
"""
nums3 = [10,20,30,40,50]
print(nums3[0])
print(nums3[-1])
print(nums3[len(nums3)//2])

"""
Count how many times a given number appears in a list
(do not use built-in count)
"""
nums4 = [1,2,3,4,5,1,2,3,1,2,3,1,3,2,1,3]
num = 1
Count = 0
for i in nums4:
    if num == i:
        Count +=1
print(Count)

#Create a new list that contains only even numbers from a given list
nums5 = [1,2,4,5,3,5,6,8,10,2,14,13,2,12,1,2,3,3,1]
even_list = []
for i in nums5:
    if i % 2 == 0:
        even_list.append(i)
print(even_list)
