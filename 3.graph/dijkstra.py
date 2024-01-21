from heapq import heappop, heappush
from math import inf

def dijkstra(graph,start,end):
    visited = [inf for _ in range(len(graph))]
    visited[start] = 0

    q = [(0,start)]

    while q:
        node, cost = heappop(q)
        
        if node == end:
            return visited[end]
        
        for edge, weight in graph[node]:
            next_cost = cost + weight

            if visited[edge] > next_cost:
                visited[edge] = next_cost
                heappush((next_cost, edge))

    return None
                