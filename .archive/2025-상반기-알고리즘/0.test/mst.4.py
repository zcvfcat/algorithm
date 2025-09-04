def mst(graph: list[(int, int)]):
    parents = [i for i in range(len(graph))]

    def find(a):
        if parents[a] != a:
            parents[a] = find(parents[a])
        return parents[a]

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parents[b] = a

    edges = []
    for node, connections in enumerate(graph):
        for neighbor, weight in connections.items():
            edges.append((weight, node, neighbor))

    edges.sort()
    total = 0

    for edge in edges:
        weight, node, neighbor = edge
        if find(node) != find(neighbor):
            total += weight
            union(node, neighbor)

    return total