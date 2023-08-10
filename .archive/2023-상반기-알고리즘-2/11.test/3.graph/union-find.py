parents = [i for i in range(10)]


def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]


def union(a, b):
    a = find(a)
    b = find(b)

    if b != a:
        parents[b] = a


union(1, 5)
union(1, 4)

union(2, 3)
union(2, 5)

print(set(map(lambda x: find(x), parents)))
