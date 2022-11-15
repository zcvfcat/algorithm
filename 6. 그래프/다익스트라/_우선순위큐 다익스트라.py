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
        node, node_weight = heapq.heappop(q)  # min 우선순위 힙 (가장 작은 거리) 가 나옴

        if distance[node] < node_weight:
            continue

        for edge, edge_wight in graph[node]:
            cost = node_weight + edge_wight

            if cost < distance[edge]:
                distance[edge] = cost
                heapq.heappush(q, (edge, cost))


dijkstra(start)
print(distance)
