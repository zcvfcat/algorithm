def find(node):
    if node != parents[node]:
        parents[node] = find(parents[node])
    return parents[node]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parents[b] = a

def kruskal(edges):
    edges.sort()
    total = 0

    for weight, node, edge in edges:
        if find(node) != find(edge):
            union(node, edge)
            total += weight
    
    return total

가중치_노드_엣지_집합 = [
    [29, 1, 2],
    [75, 1, 6],
    [35, 2, 3],
    [34, 2, 6],
    [7, 3, 4],
    [23, 4, 6],
    [13, 4, 7],
    [53, 5, 6],
    [25, 6, 7],
]

노드_길이 = 7

parents = [node for node in range(노드_길이 + 1)]

cost = kruskal(edges=가중치_노드_엣지_집합)

print(cost)
