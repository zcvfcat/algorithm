from math import inf

def floyd_warshall(graph):
    node_length = len(graph)
    distances = [[inf for _ in range(node_length)] for _ in range(node_length)]

    for node in range(node_length):
        distances[node][node] = 0
    
    for node in range(node_length):
        for edge, cost in graph[node]:
            distances[node][edge] = cost

    for route in range(node_length):
        for node in range(node_length):
            for edge in range(node_length):
                distances[node][edge] = min(distances[node][edge], distances[node][route] + distances[route][edge])