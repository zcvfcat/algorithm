def kruskal(graph):
    mst = []
    parents = {}
    rank = {}

    def make_set(node):
        parents[node] = node
        rank[node] = 0

    def find(a):
        if parents[a] != a:
            parents[a] = find(parents[a])
        return parents[a]

    def union(a,b):
        root_a = find(a)
        root_b = find(b)

        # if root_a != root_b:
