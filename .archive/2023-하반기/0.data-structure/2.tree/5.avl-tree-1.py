class Node:
    def __init__(self, data):
        self.data =data
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
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0
        
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)
    
# Create an instance of AVL tree
avl = AVL()
root = None

# Insert nodes into the AVL tree
root = avl.insert(root, 30)
root = avl.insert(root, 20)
root = avl.insert(root, 40)
root = avl.insert(root, 10)
root = avl.insert(root, 25)

# Verify the AVL tree
assert root.data == 30
assert root.left.data == 20
assert root.right.data == 40
assert root.left.left.data == 10
assert root.left.right.data == 25

# Insert a node to trigger Right-Right rotation
root = avl.insert(root, 5)
assert root.data == 20
assert root.left.data == 10
assert root.left.left.data == 5
assert root.right.data == 30
assert root.right.left.data == 25
assert root.right.right.data == 40

# Insert a node to trigger Left-Left rotation
root = avl.insert(root, 50)
assert root.data == 30
assert root.left.data == 20
assert root.left.left.data == 10
assert root.left.right.data == 25
assert root.right.data == 40
assert root.right.right.data == 50

# Insert a node to trigger Left-Right rotation
root = avl.insert(root, 35)
assert root.data == 30
assert root.left.data == 20
assert root.left.left.data == 10
assert root.left.right.data == 25
assert root.right.data == 40
assert root.right.left.data == 35
assert root.right.right.data == 50

# Insert a node to trigger Right-Left rotation
root = avl.insert(root, 15)
assert root.data == 30
assert root.left.data == 20
assert root.left.left.data == 10
assert root.left.right.data == 25
assert root.right.data == 35
assert root.right.left.data == 15
assert root.right.right.data == 40
assert root.right.right.right.data == 50

print("All test cases passed!")