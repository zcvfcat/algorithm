class Node:
    left = None
    right = None

    def __init__(self, key) -> None:
        self.key = key

# 노드 생성


def insert(node, key):
    if not node:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def in_order(node: Node):
    if not node:
        return

    in_order(node.left)
    print(node.key, end=' ')
    in_order(node.right)


def pre_order(node: Node):
    if not node:
        return

    print(node.key, end=' ')
    pre_order(node.left)
    pre_order(node.right)


def post_order(node: Node):
    if not node:
        return

    post_order(node.left)
    post_order(node.right)
    print(node.key, end=' ')


root = None
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)

# 중위
print('중위')
in_order(root)
print()

# 전위
print('전위')
pre_order(root)
print()

# 후위
print('후위')
post_order(root)
