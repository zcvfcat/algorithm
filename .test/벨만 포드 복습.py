from math import inf

edges = [
    [1, 2, 4],
    [1, 3, 3],
    [2, 3, -1],
    [3, 1, -2],
]

node_length = 3
edge_length = 4
distance = [inf for _ in range(node_length + 1)]


def bellman_ford(start_node, distance):
    distance[start_node] = 0

    for cycle in range(node_length):
        for node, edge, cost in edges:
            edge_cost = distance[node] + cost

            if distance[node] == inf:
                continue

            if distance[edge] > edge_cost:
                distance[edge] = edge_cost

                if cycle == node_length - 1:
                    return True

    return False

isCycle = bellman_ford(1, distance)

if not isCycle:
    for node in range(1, node_length + 1):
        if distance[node] == inf:
            print('도달 불가')
        else:
            print('node:', node, 'cost : ', distance[node])
else:
    print('negative cycle')
