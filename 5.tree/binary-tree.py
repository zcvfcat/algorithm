class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root == None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, end=" ")
        in_order(root.right)


root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = insert(root, key)
