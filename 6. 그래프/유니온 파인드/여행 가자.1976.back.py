n = int(input())
m = int(input())

city = [[0 for j in range(n + 1)] for i in range(n + 1)]
parent = [i + 1 for i in range(n)]


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


for i in range(1, n + 1):
    city[i] = list(map(int, input().split()))
    city[i].insert(0, 0)

route = list(map(int, input().split(' ')))
route.insert(0, 0)
