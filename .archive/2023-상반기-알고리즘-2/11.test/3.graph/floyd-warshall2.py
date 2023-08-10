from math import inf

# node, edge, cost
node_length = 4
edges = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]


def floyd_warshall(edges: list, node_length: int):
    distances = [[inf for w in range(node_length)] for h in range(node_length)]

    for node in range(node_length):
        for edge in range(node_length):
            if node is edge:
                distances[node][edge] = 0
        
    for distance in distances:
        print(distance)

    for node, edge, cost in edges:
        distances[node][edge] = cost
    
    for distance in distances:
        print(distance)

    for route in range(node_length):
        for node in range(node_length):
            for edge in range(node_length):
                distances[node][edge] = min(distances[node][edge], distances[node][route] + distances[route][edge])

    return distances


dists = floyd_warshall(edges, node_length + 1)
for dist in dists:
    print(dist)
