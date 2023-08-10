parents = []


def find(node):
    if node != parents[node]:
        parents[node] = find(parents[node])
    return parents[node]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[b] = a

# edges (weight, node, edge)
def kruskal(edges: list):
    edges.sort()  # weight 기준 최소값

    cost = 0

    for weight, node, edge in edges:
        if find(node) != find(edge):  # 같은 서로소 집합인지 확인
            union(node, edge)
            cost += weight

    return cost


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
