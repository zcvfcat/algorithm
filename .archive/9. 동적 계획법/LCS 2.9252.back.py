# 모르겠누...

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

array = [*input()][:-1]
target = [*input()][:-1]

dp = [[0 for _ in range(len(target) + 1)] for _ in range(len(array) + 1)]
path = []

for i in range(1, len(array) + 1):
    for j in range(1, len(target) + 1):
        if array[i - 1] == target[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(array)][len(target)])


def get_text(row, column):
    if row == 0 or column == 0:
        return

    if array[row - 1] == target[column - 1]:
        path.append(array[row - 1])
        get_text(row - 1, column - 1)
    else:
        if dp[row - 1][column] > dp[row][column - 1]:
            get_text(row - 1, column)
        else:
            get_text(row, column - 1)


get_text(len(array), len(target))

for i in range(len(path) - 1, -1, -1):
    print(path.pop(i), end='')

print()
