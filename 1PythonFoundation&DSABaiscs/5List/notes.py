#Lists
#A list is an ordered, mutable collection of elements.
nums = [1,2,3,5,6]
print(nums)
"""
Key Properties
=>Ordered
=>Allows duplicates
=>Mutable (can change values)
"""

#List indexing
#Indexes start from 0.
print(nums[0]) #1
print(nums[1]) #2
print(nums[-2]) #5 negetive indexing
#Accessing invalid index → IndexError

#Updating List Values
nums[3] = 4
print(nums)

#append() — Add Element at End
nums.append(7)
print(nums)
"""
✔ Adds one element
✔ Very fast
"""

#pop() — Remove Element
nums.pop() # removes last element
nums.pop(1) # removes element at index 1
print(nums)

#Iteration Over List
#Using for
for i in nums:
    print(i)
#using index
for i in range(len(nums)):
    print(nums[i])

#List Copy
nums1 = nums
#num1 is NOT a copy, it’s a reference.
nums2 = nums.copy()
#proper copy(proper explanation in future)
