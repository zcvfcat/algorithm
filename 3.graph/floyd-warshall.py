from math import inf


def floyd(graph):
    distances = [[inf for _ in range(len(graph))] for _ in range(len(graph))]

    for node in range(len(graph)):
        distances[node] = 0

    for node, edges in enumerate(graph):
        for cost, edge in edges:
            distances[node][edge] = cost

    for route in range(len(graph)):
        for node in range(len(graph)):
            for edge in range(len(graph)):
                distances[node][edge] = min(distances[node][edge], distances[node][route] + distances[route][edge])
    
    return distances