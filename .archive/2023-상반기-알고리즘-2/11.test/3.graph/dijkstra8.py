from math import inf
from heapq import heappop, heappush

def dijkstra(graph, start, end):
    distance = [inf for _ in range(len(graph))]
    q = [(0, start)]
    
    while q:
        node_cost, node = heappop(q)

        if node_cost > distance[node]:
            continue

        if node == end:
            return distance

        for edge, edge_cost in graph[node]:
            next_cost = node_cost + edge_cost

            if distance[edge] > next_cost:
                distance[edge] = next_cost
                heappush(q, (next_cost, edge))

    return distance

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

# 1 -> 4로 갈 때, 최소 코스트
dist = dijkstra(graph, 1, 4)
print(dist)