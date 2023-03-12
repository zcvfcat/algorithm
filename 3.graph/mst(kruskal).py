def kruskal(graph):
    mst = []  # 최소 신장 트리
    parent = dict()  # 부모 노드 저장용 딕셔너리
    rank = dict()  # 랭크 저장용 딕셔너리

    # 모든 노드의 부모를 자기 자신으로 초기화
    def make_set(node):
        parent[node] = node
        rank[node] = 0

    # 노드 a와 노드 b가 속한 집합을 합치는 함수
    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_a] = root_b
                if rank[root_a] == rank[root_b]:
                    rank[root_b] += 1

    # 노드 a의 최상위 부모를 찾는 함수
    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]

    # 모든 노드에 대해 make_set 함수 실행
    for node in graph['vertices']:
        make_set(node)

    # 간선을 오름차순으로 정렬
    edges = graph['edges']
    edges.sort()

    # 간선 연결
    for edge in edges:
        weight, a, b = edge
        if find(a) != find(b):
            union(a, b)
            mst.append(edge)

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
