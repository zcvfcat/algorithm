import sys
input = sys.stdin.readline

mod = 10_007
n = int(input())
dp = [0] * (1001)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod

print(dp[n])
