class DisjointSetUnion:
    """
    유니온-파인드(Disjoint Set Union, DSU)

    - 기능: 집합 합치기(union), 대표 찾기(find)
    - 최적화: 경로 압축(Path Compression) + 랭크 기준 합치기(Union by Rank)
    """

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


