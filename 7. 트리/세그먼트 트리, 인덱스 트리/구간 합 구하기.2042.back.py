import sys
input = sys.stdin.readline

node_range, changing, summing = map(int, input().split())

tree_height = 0

tree_index = node_range

while node_range != 0:
    tree_index //= 2
    tree_height += 1

tree_size = pow(2, tree_height + 1)
left_node_start = tree_size // 2 - 1
tree = [0] * (tree_size + 1)

for i in range(left_node_start + 1, left_node_start + node_range + 1):
    tree[i] = int(input())


def setTree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1


setTree(tree_size - 1)


def change_val(index, value):
    diff = value - tree[index]

    while index > 0:
        tree[index] = tree[index] + diff
        index = index // 2


def get_sum(node, edge):
    part_sum = 0

    while node <= edge:
        if node % 2 == 1:
            part_sum += tree[node]
            node += 1

        if node % 2 == 0:
            part_sum += tree[node]
            edge -= 1

        node = node // 2
        edge = edge // 2

    return part_sum


for _ in range(changing + summing):
    question, node, edge = map(int, input().split())

    if question == 1:
        change_val(left_node_start + node, edge)

    elif question == 2:
        node = node + left_node_start
        edge = edge + left_node_start
        print(get_sum(node, edge))
