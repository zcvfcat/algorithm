def kruskal(edges, vertex_length):
    parents = [i for i in range(vertex_length)]

    def find(vertex):
        if parents[vertex] != vertex:
            parents[vertex] = find(parents[vertex])
        return parents[vertex]
    
    def union(a, b):
        a, b = find(a), find(b)
        
        if a != b:
            parents[b] = a
    
    
    total = 0

    for cost, vertex, edge in edges:
        if find(vertex) != find(edge):
            union(vertex, edge)
            total = cost
    
    return cost
