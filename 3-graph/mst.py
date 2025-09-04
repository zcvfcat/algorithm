class DisjointSetUnion:
    """유니온-파인드(경로압축 + 랭크)"""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def kruskal(n, edges):
    """
    크루스칼 MST.

    - 입력: n 정점 수, edges: (w, u, v) 혹은 (u, v, w) 허용
    - 반환: (총 가중치, 선택된 간선 리스트)
    """
    normalized = []
    for e in edges:
        if len(e) != 3:
            raise ValueError("edges는 3원소 튜플이어야 합니다.")
        if isinstance(e[0], (int, float)):
            w, u, v = e
        else:
            u, v, w = e
        normalized.append((w, u, v))

    dsu = DisjointSetUnion(n)
    mst_weight = 0
    mst_edges = []

    for w, u, v in sorted(normalized):
        if dsu.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))
            if len(mst_edges) == n - 1:
                break

    if len(mst_edges) != n - 1:
        raise ValueError("그래프가 연결되어 있지 않습니다.")

    return mst_weight, mst_edges


import heapq


def prim(n, adj, start=0):
    """
    프림 MST (인접 리스트 사용).

    - 입력: n 정점 수, adj[u] = [(v, w), ...], start 시작 정점
    - 반환: (총 가중치, 선택된 간선 리스트)
    """
    visited = [False] * n
    visited[start] = True
    pq = []
    for v, w in adj.get(start, []):
        heapq.heappush(pq, (w, start, v))

    mst_weight = 0
    mst_edges = []

    while pq and len(mst_edges) < n - 1:
        w, u, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        mst_weight += w
        mst_edges.append((u, v, w))
        for nv, nw in adj.get(v, []):
            if not visited[nv]:
                heapq.heappush(pq, (nw, v, nv))

    if len(mst_edges) != n - 1:
        raise ValueError("그래프가 연결되어 있지 않습니다.")

    return mst_weight, mst_edges


