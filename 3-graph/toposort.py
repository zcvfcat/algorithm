from collections import deque


def toposort_kahn(n, edges):
    """
    위상 정렬(Kahn 알고리즘). DAG에서만 유효.

    - 입력:
      n: 정점 수 (0..n-1)
      edges: (u, v) 리스트 (u -> v)
    - 반환: 위상 정렬 순서 리스트. 사이클이 있으면 ValueError.
    """
    indeg = [0] * n
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1

    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(order) != n:
        raise ValueError("사이클이 존재하여 위상 정렬이 불가능합니다.")

    return order


