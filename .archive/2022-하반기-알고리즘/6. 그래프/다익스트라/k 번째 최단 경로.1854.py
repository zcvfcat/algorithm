import sys
import heapq

input = sys.stdin.readline

width, edge_range, k = map(int, input().split())
graph = [[] for _ in range(width + 1)]
distance = [[sys.maxsize] * k for _ in range(width + 1)]

for _ in range(edge_range):
    node, edge, weight = map(int, input().split())
    graph[node].append((edge, weight))

q = [(1, 0)]  # 시작 위치, 시작 비용
distance[1][0] = 0

while q:
    node, node_weight = heapq.heappop(q)

    for edge, edge_weight in graph[node]:
        cost = node_weight + edge_weight  # 현재 노드 비용 + 현재 엣지 노드 비용

        if distance[edge][k - 1] > cost:
            distance[edge][k - 1] = cost
            distance[edge].sort()

            heapq.heappush(q, (edge, cost))

for i in range(1, width + 1):
    if distance[i][k - 1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k - 1])
