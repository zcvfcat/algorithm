import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(2)] for _ in range(n + 1)]
dp[1][1] = 1
dp[1][0] = 0

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1] + dp[i - 1][0]
    dp[i][1] = dp[i - 1][0]

print(dp[n][0] + dp[n][1])

# N = int(input())
# dp = [1, 1]

# for i in range(2, N):
#     dp.append(dp[i-1]+dp[i-2])

# print(dp[N-1])
