# (가중치, node, edge)
def kruskal(edges, l:int):
    parents = [i for i in range(l)]

    def find(n):
        if n != parents[n]:
            parents[n] = find(parents[n])
        return parents[n]
    
    def union(a,b):
        a = find(a)
        b = find(b)

        if a != b:
            parents[a] = b
    
    total = 0
    for weight,node,edge in edges:
        if find(node) != find(edge):
            union(node,edge)
            total += weight
    
    return total