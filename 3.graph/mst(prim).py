from heapq import heappush, heappop


def prim(graph, start_node):
    visited = [False for _ in range(len(graph))]
    visited[start_node] = 0

    mst = []

    q = []
    for edge, cost in graph[start_node]:
        heappush(q, (cost, start_node, edge))

    while q:
        cost, node, edge = heappop(q)

        if visited[edge] is True:
            continue

        visited[edge] = True
        mst.append((node, edge, cost))

        for next_edge, weight in graph[edge]:
            if not visited[edge]:
                heappush(q, (weight, edge, next_edge))

    return mst


# 인접 리스트 그래프: (정점, 정점, 가중치)
graph = [
    [(1, 4), (2, 3)],
    [(0, 4), (2, 2), (3, 1)],
    [(0, 3), (1, 2), (3, 5)],
    [(1, 1), (2, 5)]
]

mst = prim(graph, 0)

for edge in mst:
    print(edge)
