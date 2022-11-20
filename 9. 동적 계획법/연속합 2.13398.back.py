import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

left = [0] * n
right = [0] * n
ans = left[0]

left[0] = array[0]
right[n - 1] = array[n - 1]

for i in range(1, n):
    left[i] = max(array[i], left[i - 1] + array[i])
    ans = max(ans, left[i])

for i in range(n - 2, -1, -1):
    right[i] = max(array[i], right[i + 1] + array[i])

for i in range(1, n - 1):
    prefix_sum = left[i - 1] + right[i + 1]
    ans = max(ans, prefix_sum)

print(ans)
