graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}


def bf(graph, start):
    distance, predecessor = {}, {}
    for node in graph:
        distance[node] = float('inf')
        predecessor[node] = None

    distance[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for edge in graph[node]:
                cost = distance[node] + graph[node][edge]

                if distance[edge] > cost:
                    distance[edge] = cost

                    predecessor[edge] = node

    for node in graph:
        for edge in graph[node]:
            cost = distance[node] + graph[node][edge]

            if distance[edge] > cost:
                return -1

    return distance, predecessor

print(bf(graph,'A'))