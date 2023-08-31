class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)
        
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)
        
        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root

    def leftRotate(self, z):
        pass

    def rightRotate(self,z):
        pass

    def getHeight(self,root):
        if not root:
            return 0
        
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)

avl = AVL()
root = None
