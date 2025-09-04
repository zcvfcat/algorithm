from collections import deque


class Dinic:
    """Dinic 최대 유량 O(E*V^2) (실전에서 빠름)"""

    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])

    def _bfs(self, s, t, level):
        for i in range(self.n):
            level[i] = -1
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, _ in self.adj[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0

    def _dfs(self, u, t, f, level, it):
        if u == t:
            return f
        for i in range(it[u], len(self.adj[u])):
            it[u] = i
            v, cap, rev = self.adj[u][i]
            if cap > 0 and level[u] + 1 == level[v]:
                d = self._dfs(v, t, min(f, cap), level, it)
                if d > 0:
                    self.adj[u][i][1] -= d
                    self.adj[v][rev][1] += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        level = [-1] * self.n
        while self._bfs(s, t, level):
            it = [0] * self.n
            while True:
                pushed = self._dfs(s, t, 10 ** 18, level, it)
                if pushed == 0:
                    break
                flow += pushed
        return flow


