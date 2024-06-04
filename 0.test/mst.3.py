def mst(graph: list[(int, int)]):
    edges = []
    for node, connections in graph.items():
        for weight, edge in connections:
            edges.append((weight, node, edge))

    n = max(max(node, edge) for _, node, edge in edges) + 1
    parents = [i for i in range(n)]

    def find(node):
        if parents[node] != node:
            parents[node] = find(parents[node])
        return parents[node]

    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA != rootB:
            parents[rootB] = rootA

    edges.sort()

    total = 0
    for weight, node, edge in edges:
        if find(node) != find(edge):
            union(node, edge)
            total += weight

    return total
