"""
첫째 줄에 문제의 수 N(1 ≤ N ≤ 32,000)과 먼저 푸는 것이 좋은 문제에 대한 정보의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 둘째 줄부터 M개의 줄에 걸쳐 두 정수의 순서쌍 A,B가 빈칸을 사이에 두고 주어진다. 이는 A번 문제는 B번 문제보다 먼저 푸는 것이 좋다는 의미이다.

항상 문제를 모두 풀 수 있는 경우만 입력으로 주어진다.
"""

import sys
# from collections import deque
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
degrees = [0 for _ in range(n + 1)]
q = []

ans = []

for _ in range(m):
    node, edge = map(int, input().split())
    graph[node].append(edge)
    degrees[edge] += 1

for node in range(1, n + 1):
    if degrees[node] == 0:
        heapq.heappush(q, node)

while q:
    node = heapq.heappop(q)
    ans.append(node)

    for edge in graph[node]:
        degrees[edge] -= 1

        if degrees[edge] == 0:
            heapq.heappush(q, edge)

print(' '.join(map(str, ans)))
