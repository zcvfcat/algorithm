class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def Insert(node, key):
    if not node:
        return Node(key)
    if (key < node.key):
        node.left = Insert(node.left, key)
    else :
        node.right = Insert(node.right, key)
    return node

def PrintInorder(node):
    if not node:
        return
    PrintInorder(node.left)
    print(node.key, end=" ")
    PrintInorder(node.right)

root = None
root = Insert(root, 3)
root = Insert(root, 5)
root = Insert(root, 2)
root = Insert(root, 4)
root = Insert(root, 7)
root = Insert(root, 6)

print("Inorder traversal of the given tree is: ")
PrintInorder(root)