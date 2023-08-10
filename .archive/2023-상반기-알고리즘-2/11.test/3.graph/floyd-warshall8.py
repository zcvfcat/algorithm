from math import inf

def floyd_warshall(graph):
    distances = [[inf for _ in len(graph)] for _ in range(len(graph))]
    
    for node in range(len(graph)):
        distances[node][node] = 0

    for node in range(len(graph)):
        for edge, cost in graph[node]:
            distances[node][edge] = cost
    
    length = len(graph)

    for route in range(length):
        for node in range(length):
            for edge in range(length):
                distances[node][edge] = min(distances[node][edge], distances[node][route] + distances[route][edge])
    
    return distances