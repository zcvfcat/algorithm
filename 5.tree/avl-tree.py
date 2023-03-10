class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.height = 1
  
class AVL_Tree: 
  
    def insert(self, root, key): 
  
        if not root: 
            return Node(key) 
        elif key < root.data: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        balance = self.getBalance(root) 
  
        # Left Left Case 
        if balance > 1 and key < root.left.data: 
            return self.rightRotate(root) 
  
        # Right Right Case 
        if balance < -1 and key > root.right.data: 
            return self.leftRotate(root) 
  
        # Left Right Case 
        if balance > 1 and key > root.left.data: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Right Left Case 
        if balance < -1 and key < root.right.data: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.data), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
  
  

myTree = AVL_Tree() 
root = None

root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 

print("Pre order traversal of the", 
        "constructed AVL tree is") 
myTree.preOrder(root) 
print()