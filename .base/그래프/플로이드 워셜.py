import sys

node_length = 4
edges = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]


def floyd_warshall(node_length, edges):
    distance = [[sys.maxsize if w != h else 0 for w in range(node_length)] for h in range(node_length)]

    for node, edge, cost in edges:
        distance[node - 1][edge - 1] = cost

    for point in range(node_length):
        for node in range(node_length):
            for edge in range(node_length):
                distance[node][edge] = min(distance[node][edge], distance[node][point] + distance[point][edge])

    return distance


print(floyd_warshall(node_length, edges))
