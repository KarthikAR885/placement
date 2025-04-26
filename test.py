1.py
def max_steal(val):
    n = len(val)
    if n == 0:
        return 0
    if n == 1:
        return val[0]
    
    dp = [0] * n
    dp[0] = val[0]
    dp[1] = max(val[0], val[1])
    
    for i in range(2, n):
        dp[i] = max(val[i] + dp[i-2], dp[i-1])
    
    return dp[-1]

# Sample Input
val = [6, 7, 1, 3, 8, 2, 5]
print("Maximum stolen value:", max_steal(val))

2.py
for i in range(5):
    for j in range(5):
        if (i % 2 == 0 and j == 4):
            print(i + 2, end="")
        elif (i % 2 == 1 and j == 0):
            print(i + 2, end="")
        else:
            print(i + 1, end="")
    print()
