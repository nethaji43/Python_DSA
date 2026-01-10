#Tuple — Immutability
#A tuple is an ordered collection that cannot be changed after creation.
t = (1,2,3)
print(t)
"""
Key Properties
=>Ordered
=>Allows duplicates
=>Immutable
=>Faster than list for read-only data
"""
"""
Use tuple when:
=>Data should never change
=>You want safety
=>Fixed data like coordinates, settings
"""


#Set — Uniqueness
#A set stores only unique values.
s = {1,2,3}
print(s)

"""
Key Properties
=>Unordered
=>No duplicates
=>Mutable
=>Very fast membership check
"""
#common operation
s.add(4)
print(s)
s.remove(4)
print(s)
#membership
if 4 in s:
    print("found")