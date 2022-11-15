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
        now_edge, now_weight = heapq.heappop(q)  # min 우선순위 힙 (가장 작은 거리) 가 나옴

        if distance[now_edge] < now_weight:
            continue

        for next_edge, next_wight in graph[now_edge]:
            cost = now_weight + next_wight

            if cost < distance[next_edge]:
                distance[next_edge] = cost
                heapq.heappush(q, (next_edge, cost))


dijkstra(start)
print(distance)
