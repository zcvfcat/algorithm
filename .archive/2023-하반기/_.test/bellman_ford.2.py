from math import inf

def bellman(edges, start, node_length):
    distance = [inf for _ in range(node_length)]
    distance[start] = 0

    for route in range(node_length):
        for node, edge, weight in edges:
            cost = distance[node] + weight

            if distance[node] != inf and distance[edge] > cost:
                distance[edge] = cost

                if route == node_length:
                    return True

    return False