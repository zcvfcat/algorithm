# 대표 노드 끼리 묶는게 아니라
# 선택된 노드 끼리 묶어야한다?

n, m = map(int, input().split(' '))
parent = [0] * (n + 1)


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


def is_same(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False


for i in range(n + 1):
    parent[i] = i

for i in range(m):
    quiz, a, b = map(int, input().split())
    if quiz == 0:
        union(a, b)
    else:
        if is_same(a, b):
            print('YES')
        else:
            print('NO')

# 0 1 3

# 1 2 3 4 5 6 7
# 1 2 1 4 5 6 7

# 0 7 6

# 1 2 3 4 5 6 7
# 1 2 1 4 5 6 6

# 0 3 7

# 1 2 3 4 5 6 7
# 1 2 1 4 5 1 6

# 0 4 2

# 1 2 3 4 5 6 7
# 1 2 1 2 5 1 6

# 0 1 1

# 1 2 3 4 5 6 7
# 1 2 1 2 5 1 6
