    
def kruskal(edges, node_length):
    parents = [i for i in range(node_length)]
    edges.sort()

    def find(node):
        if parents[node] == node:
            parents[node] = find(parents[node])
        return parents[node]

    def union(a, b):
        a, b = find(a), find(b)

        if a != b:
            parents[b] = a

    total = 0
    for node, edge, cost in edges:
        if find(node) != find(edge):
            union(node, edge)
            total += cost
    
    return total