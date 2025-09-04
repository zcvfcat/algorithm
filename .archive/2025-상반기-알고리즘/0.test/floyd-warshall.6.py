from math import inf


def floyd_warshall(graph):
    distances = [[inf for i in range(len(graph))] for i in range(len(graph))]

    for node in range(len(graph)):
        distances[node][node] = 0
        for edge, cost in graph[node]:
            distances[node][edge] = cost
    
    for route in range(len(graph)):
        for node in range(len(graph)):
            for dest in range(len(graph)):
                distances[node][dest] = min(distances[node][dest], distances[node][route] + distances[route][dest])
    
    return distances
