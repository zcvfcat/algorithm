from collections import deque


def build_rooted_tree(n, edges, root=0):
    """
    무방향 그래프 edges로부터 루트가 root인 트리 구성
    - 반환: (parent, depth, children)
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    parent = [-1] * n
    depth = [0] * n
    children = [[] for _ in range(n)]

    q = deque([root])
    parent[root] = root
    depth[root] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                depth[v] = depth[u] + 1
                children[u].append(v)
                q.append(v)
    return parent, depth, children


def lca_parent_depth(u, v, parent, depth):
    """
    LCA (부모/깊이 이용):
    - 같은 높이가 되도록 위로 끌어올리고, 동시에 위로 올리며 만나는 정점 반환.
    - O(height)
    """
    # depth 맞추기
    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]
    # 동시에 위로 이동
    while u != v:
        u = parent[u]
        v = parent[v]
    return u


