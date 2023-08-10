from math import inf

def floyd_warshall(edges, length):
    distances = [[inf for _ in range(length)] for _ in range(length)]
    
    for node in range(length):
        distances[node][node] = 0

    for node, edge, weight in edges:
        distances[node][edge] = weight
    
    for route in range(length):
        for node in range(length):
            for edge in range(length):
                distances[node][edge] = min(distances[node][edge], distances[node][route] + distances[route][edge])
    
    return distances

node_length = 4
edges = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]

distances = floyd_warshall(edges, node_length + 1)
for distance in distances:
    print(distance)