from math import inf
from heapq import heappush, heappop

def dijkstra(graph, start, end):
    distances = [inf for _ in range(graph)]
    q = [(0, start)]

    while q:
        cost, node = heappop(q)

        if distances[node] < cost:
            continue
            
        for edge, weight in graph[node]:
            total = weight + cost

            if distances[edge] > total:
                q.append(((total, edge)))
                distances[edge] = total
    
    return distances[edge]