def find(parents, node):
    if parents[node] != node:
        parents[node] = find(parents, parents[node])
    return parents[node]

def union(parents,node_a,node_b):
    node_a = find(parents, node_a)
    node_b = find(parents, node_b)
    
    if node_b != node_a:
        parents[node_b] = node_a

def kruskal(edges, node_length):
    sorted_edges=sorted(edges)
    parents = [node for node in range(node_length + 1)]

    total = 0
    for record in sorted_edges:
        cost, node, edge = record
        
        if find(parents,node) != find(parents, edge):
            union(parents, node, edge)
            total += cost
    
    return total

edges = [
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

print(kruskal(edges,7))