import sys
input = sys.stdin.readline

n = int(input())
parent = [-1] * 3001


def create_ccw(x1, y1, x2, y2, x3, y3):
    ccw = (x1 * y1 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

    if ccw > 0:
        return 1
    elif ccw < 0:
        return -1
    else:
        return 0


def is_overlab(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and \
            min(x3, x4) <= max(x1, x2) and \
            min(y1, y2) <= max(y3, y4) and \
            min(y3, y4) <= max(y1, y2):
        return True
    return False


def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = create_ccw(x1, y1, x2, y2, x3, y3)
    abd = create_ccw(x1, y1, x2, y2, x4, y4)
    cda = create_ccw(x3, y3, x4, y4, x1, y1)
    cdb = create_ccw(x3, y3, x4, y4, x2, y2)

    if abc * abd == 0 and cda * cdb == 0:
        return is_overlab(x1, y1, x2, y2, x3, y3, x4, y4)
    elif abc * abd <= 0 and cda * cdb <= 0:
        return True
    return False


def find(node):
    if parent[node] < 0:
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]


def union(node_a, node_b):
    parent_node_a = find(node_a)
    parent_node_b = find(node_b)

    if parent_node_a == parent_node_b:
        return

    parent[parent_node_a] += parent[parent_node_b]
    parent[parent_node_b] = parent_node_a


l = [[]]

for i in range(1, n + 1):
    l.append([])
    l[i] = list(map(int, input().split()))
    for j in range(1, i):
        if is_cross(l[i][0], l[i][1], l[i][2], l[i][3], l[j][0], l[j][1], l[j][2], l[j][3]):
            union(i, j)

ans = 0
res = 0

for i in range(1, n + 1):
    if parent[i] < 0:
        ans += 1
        res = min(res, parent[i])

print(ans)
print(-res)
