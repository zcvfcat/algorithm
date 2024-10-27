from heap import heappop, heappush
from math import inf

def dijkstra(graph, start, end):
    distances = {vertex: inf for vertex in graph}
    distances[start] = 0

    q = [(0, start)]

    while q:
        cost, node = heappop(q)
        
        if cost > distances[start]:
            continue

        for edge, weight in graph[node]:
            next_cost = cost + weight

            if next_cost < distances[edge]:
                distances[edge] = next_cost
                heappush(q, (next_cost, edge))
    
    return distances