class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py


ds = DisjointSet(6)

ds.union(0, 1)
ds.union(1, 2)
ds.union(3, 4)
ds.union(4, 5)

print(ds.find(2))  # 0
print(ds.find(5))  # 3
