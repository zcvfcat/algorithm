# weight, start, end
def mst(edges: list[(int, int, int)], node_length: int):
    group = [i for i in range(len(node_length))]
    edges.sort() # weight 기준으로 오름차순

    def find(node):
        if group[node] != node:
            group[node] = find(group[node])
        return group[node]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            group[b] = a

    total = 0
    for weight, node, edge in edges:
        if find(node) != find(edge):
            union(node, edge)
            total += weight

    return total