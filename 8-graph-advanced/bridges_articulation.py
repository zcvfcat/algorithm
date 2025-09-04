def find_bridges_and_articulation(n, edges):
    """
    무방향 그래프의 브리지(단절선)와 단절점 탐색 (Tarjan)
    - 입력: 정점 수 n, 간선 리스트 edges[(u,v)] (u!=v)
    - 반환: (bridges, articulation)
      bridges: (u,v) 형태 리스트(작은 정점 번호가 앞)
      articulation: 단절점 집합
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    timer = 0
    tin = [-1] * n
    low = [0] * n
    visited = [False] * n
    bridges = []
    articulation = set()

    def dfs(u, parent=-1):
        nonlocal timer
        visited[u] = True
        tin[u] = low[u] = timer
        timer += 1
        children = 0
        for v in adj[u]:
            if v == parent:
                continue
            if visited[v]:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridges.append((min(u, v), max(u, v)))
                if parent != -1 and low[v] >= tin[u]:
                    articulation.add(u)
                children += 1
        if parent == -1 and children > 1:
            articulation.add(u)

    for u in range(n):
        if not visited[u]:
            dfs(u)
    bridges.sort()
    return bridges, articulation


