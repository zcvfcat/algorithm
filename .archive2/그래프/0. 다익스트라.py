from math import inf
from heapq import heappush, heappop

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

node_length = len(graph) - 1
start_node = 1


def dijkstra(start_node, graph):
    distance = [inf for _ in range(node_length + 1)]
    distance[start_node] = 0
    
    q = []
    heappush(q,(0,start_node))

    while q:
        prev_cost, vertex = heappop(q)
        
        if distance[vertex] < prev_cost:
            continue

        for edge, next_cost in graph[vertex]:
            cost = prev_cost + next_cost

            if distance[edge] > cost:
                distance[edge] = cost
                heappush(q, (cost, edge))

    return distance

distance = dijkstra(1, graph)

print(distance)

