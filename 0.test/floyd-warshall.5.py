from math import inf

def floyd_warshall(graph):
    distances = [[inf for _ in range(len(graph))] for _ in range(len(graph))]

    for node in range(len(graph)):
        distances[node][node] = 0
        for edge in graph[node]:
            distances[node][edge] = edge
            distances[edge][node] = edge

    for route in range(len(graph)):
        for node in range(len(graph)):
            for edge in range(len(graph)):
                distances[node][edge] = min(distances[node][edge], distances[node][route] + distances[route][edge])
    
    return distances