def mst(edges, n):
    parents = [i for i in range(n)]
    rank = [0] * n
    total_weight = 0

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(x, y, weight):
        root_x = find(x)
        root_y = find(y)

        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parents[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parents[root_x] = root_y
            else:
                parents[root_y] = root_x
                rank[root_x] += 1
            return weight
        return 0
    
    # 엣지를 가중치 기준으로 정렬
    edges.sort(key=lambda x: x[2])
    
    for edge in edges:
        u, v, w = edge
        total_weight += union(u, v, w)
    
    return total_weight