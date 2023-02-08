from math import inf

node_length = 4
edges = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]


def floyd_warshall(edges, node_length):
    distance = [[inf if w != h else 0 for w in range(node_length + 1)] for h in range(node_length + 1)]

    for node, edge, cost in edges:
        distance[node][edge] = cost

    for route in range(1, node_length + 1):
        for node in range(1, node_length + 1):
            for edge in range(1, node_length + 1):
                distance[node][edge] = min(distance[node][route] + distance[route][edge],distance[node][edge])

    return distance

distance = floyd_warshall(edges, node_length)
print(distance)
