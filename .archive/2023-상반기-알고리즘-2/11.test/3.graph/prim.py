inf = float('inf')


def prim(graph, start):
    distance = {node: inf for node in graph}
    distance[start] = 0

    current = start
    visited = set()
    mst = []

    while len(visited) < len(graph):
        visited.add(current)

        for neighbor, weight in graph[current].items():

            if neighbor in visited:
                continue

            if weight < distance[neighbor]:
                distance[neighbor] = weight

        next_node = min(distance, key=distance.get)
        mst.append((current, next_node, distance[next_node]))
        current = next_node
        distance[next_node] = inf

    for edge in mst:
        print(edge[0], '-', edge[1], ':', edge[2])


graph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5, 'F': 8},
    'D': {'A': 5, 'B': 9, 'E': 15},
    'E': {'B': 7, 'C': 5, 'D': 15, 'F': 9, 'G': 11},
    'F': {'C': 8, 'E': 9, 'G': 10},
    'G': {'E': 11, 'F': 10}
}

prim(graph, 'A')
