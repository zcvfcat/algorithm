from collections import deque


def hopcroft_karp(left_size, right_size, edges):
    """
    Hopcroft-Karp 이분 매칭 O(E*sqrt(V))
    - left_size: 좌측 정점 수, right_size: 우측 정점 수
    - edges: 좌측 u -> 우측 v 간선 리스트
    - 반환: 매칭 수, pair_u, pair_v
    """
    adj = [[] for _ in range(left_size)]
    for u, v in edges:
        adj[u].append(v)

    pair_u = [-1] * left_size
    pair_v = [-1] * right_size
    dist = [0] * left_size

    INF = 10 ** 18

    def bfs():
        q = deque()
        for u in range(left_size):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        reachable_free = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                if pu == -1:
                    reachable_free = True
        return reachable_free

    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(left_size):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u, pair_v


