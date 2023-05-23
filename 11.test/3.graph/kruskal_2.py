def kruskal(graph):
    mst = []
    parents = {}
    rank = {}

    def make_set(node):
        parents[node] = node
        rank[node] = 0

    def find(a):
        if parents[a] != a:
            parents[a] = find(parents[a])
        return parents[a]

    def union(a,b):
        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            if rank[root_a] > rank[root_b]:
                parents[root_b] = root_a
            else:
                parents[root_a] = root_b
                if rank[root_a] == rank[root_b]:
                    rank[root_b] += 1

    for node in graph['vertices']:
        make_set(node)
    
    edges = graph['edges']
    edges.sort()

    total = 0

    for edge in edges:
        weight, a, b = edge

        if find(a) != find(b):
            union(a,b)
            mst.append(edge)
            total += weight

    print(total)
    return mst

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'C', 'B'),
        (5, 'C', 'E'),
        (8, 'C', 'F'),
        (7, 'D', 'A'),
        (9, 'D', 'B'),
        (15, 'D', 'E'),
        (6, 'E', 'D'),
        (8, 'E', 'C'),
        (9, 'E', 'F'),
        (11, 'E', 'G'),
    ]
}

print(kruskal(graph))