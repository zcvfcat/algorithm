import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
namus = [*map(int,input().split())]

left = 1
right = max(namus)

while left <= right:
    mid = (left + right) // 2
    rest_namu = 0
    for namu in namus:
        if namu > mid:
            rest_namu += namu - mid

    if rest_namu >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
