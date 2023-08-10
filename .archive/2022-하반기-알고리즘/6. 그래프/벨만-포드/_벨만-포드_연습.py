import sys

start_node = 1
width = 3
edge_range = 4
edges = [
    (1, 2, 4),
    (1, 3, 3),
    (2, 3, -1),
    (3, 1, -2),
]

distance = [sys.maxsize] * (width + 1)


def bellman_ford(start_node):
    distance[start_node] = 0

    for node_index in range(width):
        for edge_index in range(edge_range):
            node, edge, weight = edges[edge_index]
            cost = distance[node] + weight

            if distance[node] != sys.maxsize and distance[edge] > cost:
                distance[edge] = cost

                if node_index == width:
                    return True
    return False


isCycle = bellman_ford(start_node)

if isCycle:
    print("-1")
else:
    for node in range(2, width + 1):
        if distance[node] == sys.maxsize:
            print("-1")
        else:
            print(distance[node])
