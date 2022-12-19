import sys

node_length = 4
edges = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]


def floyd_warshall(node_length, edges):
    d = [[sys.maxsize if w != h else 0 for w in range(node_length + 1)] for h in range(node_length + 1)]

    for node, edge, cost in edges:
        d[node][edge] = cost

    for route in range(1, node_length + 1):
        for node in range(1, node_length + 1):
            for edge in range(1, node_length + 1):
                d[node][edge] = min(d[node][edge], d[node][route] + d[route][edge])

    return d


print(floyd_warshall(node_length, edges))
