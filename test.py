import sys
import heapq
input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
    number = int(input())

    if number != 0:
        heapq.heappush(q, number)
    else:
        if len(q):
            print(heapq.heappop(q))
        else:
            print(0)
