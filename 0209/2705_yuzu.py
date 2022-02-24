def dps(n):
    dp = {0:1, 1:2, 2:4, 3:6, 4:10}
    for i in range(5, n+1):
        dp[i] = dp[i-1] + dp[i-(((i-3)//2)+2)]
    return dp[n]

t = int(input())
for tc in range(t):
    n = int(input())
    print(dps(n//2))