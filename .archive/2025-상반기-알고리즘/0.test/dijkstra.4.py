from math import inf
from heapq import heappush, heappop


def dijkstra(graph: list[list[int]], start, end):
    distance = [inf for i in graph]
    distance[start] = 0
    
    q = [(0, start)]

    while q:
        cost, node = heappop(q)
        
        if distance[node] < cost:
            continue

        for edge, weight in graph[node]:
            next_cost = cost + weight
            
            if distance[edge] > next_cost:
                distance[edge] = next_cost
                heappush((next_cost, edge))
            
    return distance[end] 