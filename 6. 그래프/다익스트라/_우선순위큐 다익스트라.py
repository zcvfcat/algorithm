import heapq

INF = 1e8
width = 5
start = 1

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

distance = [INF] * (width + 1)
visited = [False] * (width + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0

    while q:
        node, node_weight = heapq.heappop(q)  # 현재 (노드, 시작점에서 노드 비용)

        if distance[node] < node_weight: # visited 써도 되지만 최소 비용값으로도 가능
            continue

        for edge, edge_wight in graph[node]:
            cost = node_weight + edge_wight  # 시작점에서 (노드 비용 + 엣지까지 비용) = 시작점에서 엣지까지 비용

            if cost < distance[edge]:  # 기존 시작점 - 엣지 비용 : 신규 시작점 - 엣지 비용
                distance[edge] = cost
                heapq.heappush(q, (edge, cost))


dijkstra(start)
print(distance)
