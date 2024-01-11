class disjointSet:
    def __init__(self, n) -> None:
        self.data = [i for i in range(n)]
        self.size = n

    def find(self, idx):
        return self.data[idx]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x == y:
            return

        for i in range(len(self.data)):
            if self.data[i] == y:
                self.data[i] = x

        self.size -= 1


s = disjointSet(10)
s.union(0, 1)
s.union(2, 3)
s.union(1, 2)
s.union(0, 1)
s.union(4, 5)
s.union(5, 6)
s.union(7, 8)
s.union(7, 9)

print(s.data)
print(s.size)
