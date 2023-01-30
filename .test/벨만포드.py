from math import inf

edges = [
    [1, 2, 4],
    [1, 3, 3],
    [2, 3, -1],
    [3, 1, -2],
]

node_length = 3


def bellman_ford(edges, node_length, start_node):
    distance = [inf for _ in range(node_length + 1)]
    distance[start_node] = 0

    for cycle in range(node_length):
        for node, edge, cost in edges:
            edge_cost = distance[node] + cost

            if distance[node] == inf:
                continue

            if distance[edge] > edge_cost:
                distance[edge] = edge_cost

                if cycle == node_length - 1:
                    return True, distance

    return False, distance


isCycle, distance = bellman_ford(edges, node_length, 1)

print(distance)
