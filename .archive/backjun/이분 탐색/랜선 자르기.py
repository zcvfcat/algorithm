import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lanes = [int(input()) for _ in range(K)]
left, right = 1, max(lanes)

while left <= right:
    mid = (left + right) // 2

    lines = 0
    for lan in lanes:
        lines += lan // mid

    if lines >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)
