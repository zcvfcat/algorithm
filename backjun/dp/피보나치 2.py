n = int(input())
l = 90
dp = [0 for _ in range(l + 1)]

dp[1] = 1
dp[2] = 1

for i in range(3, l + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
