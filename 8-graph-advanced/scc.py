def tarjan_scc(adj):
    """
    Tarjan 알고리즘으로 SCC 분해
    - 입력: adj[u] = 이웃 리스트 (0..n-1 가정, 누락 노드는 빈 리스트)
    - 반환: sccs (리스트의 리스트, 각 SCC 구성 노드들)
    """
    n = len(adj)
    index = 0
    ids = [-1] * n
    low = [0] * n
    onstack = [False] * n
    stack = []
    sccs = []

    def dfs(u):
        nonlocal index
        ids[u] = index
        low[u] = index
        index += 1
        stack.append(u)
        onstack[u] = True
        for v in adj[u]:
            if ids[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif onstack[v]:
                low[u] = min(low[u], ids[v])
        if low[u] == ids[u]:
            comp = []
            while True:
                w = stack.pop()
                onstack[w] = False
                comp.append(w)
                if w == u:
                    break
            sccs.append(comp)

    for u in range(n):
        if ids[u] == -1:
            dfs(u)
    return sccs


