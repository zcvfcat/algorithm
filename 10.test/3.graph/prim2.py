def prim(edges):
    # vertices으로부터 시작하는 모든 edge들 중 가장 가중치가 작은 값을 찾아 반환하는 함수
    def get_min_edge(vertices, edges):
        min_edge = None  # 가중치가 가장 작은 edge
        for edge in edges:
            if (edge[1] in vertices) != (edge[2] in vertices):  # 하나의 vertex는 포함되어야 함
                if not min_edge or edge[0] < min_edge[0]:
                    min_edge = edge
        return min_edge

    mst = []  # minimum spanning tree
    vertices = {edges[0][1]}  # 임의의 vertex로부터 시작
    while len(vertices) < len(edges)+1:  # 모든 vertex를 포함할 때까지 반복
        min_edge = get_min_edge(vertices, edges)
        mst.append(min_edge)
        vertices.update([min_edge[1], min_edge[2]])
    return mst

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

print(prim(edges))
