import sys
input = sys.stdin.readline

height, width = map(int, input().split())
dp = [list(map(int, list(input().rstrip()))) for _ in range(height)]

ans = 0

for i in range(height):
    for j in range(width):
        if dp[i][j] == 1 and j > 0 and i > 0:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + dp[i][j]

        ans = max(ans, dp[i][j])


print(ans * ans)
