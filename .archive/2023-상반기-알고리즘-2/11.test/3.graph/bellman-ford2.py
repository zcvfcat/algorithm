from collections import inf


def bellman_ford_by_graph(graph, start_node):
    distance = [inf for _ in range(len(graph))]
    distance[start_node] = 0

    for cycle in range(len(graph)):
        for node in range(len(graph)):
            for edge, weight in graph[node]:
                cost = weight + distance[node]

                if distance[edge] > cost:
                    distance[edge] = cost
    return distance


def bellman_ford_by_edges(edges, node_length):
    distance = [inf for _ in range(node_length)]

    edges = sorted(edges, key=lambda edge: edge[0])

    for cycle in range(len(node_length)):
        for node, edge, weight in edges:
            cost = weight + distance[node]

            if distance[edge] > cost:
                distance[edge] = cost

    return distance
