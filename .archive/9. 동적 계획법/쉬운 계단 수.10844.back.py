import sys
input = sys.stdin.readline

mod = 1_000_000_000
n = int(input())
dp = [[0 for _ in range(11)] for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]

    for j in range(1, 9):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1])

total = sum(dp[n]) % mod

print(total)
