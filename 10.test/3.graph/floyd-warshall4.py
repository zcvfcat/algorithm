from math import inf


def floyd_warshall(edges: list, size: int):
    distances = [[inf for _ in range(size)] for _ in range(size)]

    for x in range(size):
        distances[x][x] = 0

    for node, edge, cost in edges:
        distances[node][edge] = cost

    for route in range(size):
        for node in range(size):
            for edge in range(size):
                distances[node][edge] = min(distances[node][edge], distances[node][route] + distances[route][edge])

    return distances


node_length = 4
edges = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]

distances = floyd_warshall(edges, node_length + 1)
for distance in distances:
    print(distance)
