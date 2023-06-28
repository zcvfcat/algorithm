def find(parents: list, node: int):
    if parents[node] != node:
        parents[node] = find(parents, parents[node])
    return parents[node]


def union(parents: list, a: int, b: int):
    a = find(parents, a)
    b = find(parents, b)

    if a != b:
        parents[a] = b


def kruskal(graph):
    parents = [i for i in range(len(graph))]

    edges = []
    for node in graph:
        for edge, cost in graph[node]:
            edges += [cost, node, edge]

    edges.sort()
    total = 0

    for cost, node, edge in edges:
        if find(parents,node) != find(parents,edge):
            union(parents, node, edge)
            total += cost

    return total