def mst(edges, l):
    parents = [i for i in range(l)]

    def find(n):
        if parents[n] != n:
            parents[n] = find(parents[n])
        return parents[n]

    def union(a, b):
        a, b = find(a), find(b)

        if a != b:
            parents[a] = b
    
    edges.sort()
    t = 0

    for w, n, e in edges:
        if find(n) != find(e):
            t += w
            union(n, e)
    
    return t