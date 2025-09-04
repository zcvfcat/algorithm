def kruskal(graph):
    parents = [i for i in range(len(graph))]

    def find(node):
        if parents[node] != node:
            parents[node] = find(parents[node])
        return parents[node]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        
        if a != b:
            parents[b] = a
    
    edges = []
    total = 0

    for node, node_edges in enumerate(graph):
        for edge, cost in node_edges:
            edges.append((cost, node, edge))

    for cost, node, edge in edges:
        if find(node) != find(edge):
            union(node, edge)
            total += cost
    
    return total