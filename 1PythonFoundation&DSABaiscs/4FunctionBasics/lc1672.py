def maxWealth(accounts):
    rich = 0
    for i in range(len(accounts)):
        wealth = 0
        for j in range(len(accounts[i])):
            wealth += accounts[i][j]
        if rich < wealth:
            rich = wealth
    return rich
print(maxWealth([[10,10,23],[34,32,12],[23,1,3]]))