def kruskal(graph):
    parents = [i for i in range(len(graph))]

    def find(node):
        if node != parents[node]:
            parents[node] = find(parents[node])
        return parents[node]
    
    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            parents[b] = a
    
    edges = []
    for node in range(len(graph)):
        for edge, weight in graph[node]:
            edges.append((weight, node, edge))
    
    edges.sort()
    total = 0

    for cost, node, edge in edges:
        if find(node) != find(edge):
            union(node, edge)
            total += cost
    
    return total
