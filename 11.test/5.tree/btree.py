class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if not node:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def in_order(node):
    if not node:
        return

    in_order(node.left)
    print(node.key, end=' ')
    in_order(node.right)


def pre_order(node):
    if not node:
        return

    print(node.key, end=' ')
    in_order(node.left)
    in_order(node.right)


def post_order(node):
    if not node:
        return

    in_order(node.left)
    in_order(node.right)
    print(node.key, end=' ')


root = None
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)

print("Inorder traversal of the given tree is: ")
in_order(root)
print()
pre_order(root)
print()
post_order(root)

#  3
# 2 5
#  4 7
#   6

