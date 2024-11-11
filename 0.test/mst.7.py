def mst(edges, node_length):
    parents = [i for i in range(node_length)]
    edges.sort(key=lambda x: x[2])

    def find(node):
        if parents[node] != node:
            parents[node] = find(parents[node])
        return parents[node]

    def union(a, b):
        a, b = find(a), find(b)

        if a != b:
            parents[a] = b

    total_weight = 0
    for edge in edges:
        u, v, w = edge
        if find(u) != find(v):
            union(u, v)
            total_weight += w

    return total_weight
