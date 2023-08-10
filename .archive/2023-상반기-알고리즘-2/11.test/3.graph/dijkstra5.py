from math import inf
from heapq import heappop, heappush


def dijkstra(graph, start_node):
    distance = [inf for _ in range(len(graph))]
    distance[start_node] = 0
    q = [(0, start_node)]

    while q:
        weight, node = heappop(q)
        
        for edge, current_weight in graph[node]:
            next_weight = weight + current_weight

            if distance[edge] > next_weight:
                distance[edge] = next_weight
                heappush(q, (next_weight, edge))
    
    return distance