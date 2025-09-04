from math import inf

def floyd(graph):
    distances = [[inf for _ in range(len(graph))] for _ in range(len(graph))]

    for node in range(len(graph)):
        distances[node][node] = 0

        for edge, weight in graph[node]:
            distances[node][edge] = weight

    for route in range(len(graph)):
        for node in range(len(graph)):
            if route == node:
                continue

            for edge in range(len(graph)):
                distances[node][edge] = min(distances[node][route] + distances[route][edge], distances[node][edge])
    
    return distances

