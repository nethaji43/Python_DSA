#break — Exit the Loop Completely
#Used to stop the loop immediately, even if iterations are remaining.
for i in range(1,10):
    if i == 3:
        break
    print(i)
"""
As soon as break executes, loop ends.
Common Use Cases
=>Stop when condition is met
=>Searching problems
=>Early exit for optimization
"""

#continue — Skip Current Iteration
#Used to skip the remaining code in the current iteration and move to the next one.
for i in range(1,10):
    if i == 3:
        continue
    print(i)

#pass — Do Nothing (Placeholder)
#pass is used when Python expects a statement, but you don’t want to write logic yet.
i = 3
if i == 3:
    pass
#Without pass, Python throws an error.
#Python does not allow empty blocks.
"""
Common Real-World Use
=>While building code step-by-step
=>Empty functions / classes
=>Temporary placeholder
"""

#Nested Loop Behavior
#break and continue affect only the inner loop.
for i in range(1,5):
    for j in range(1,5):
        if j == 3:
            break
        print(i,j)