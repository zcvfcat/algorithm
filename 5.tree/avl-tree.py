class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = max(self.height(root.left), self.height(root.right)) + 1

        balance = self.balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left or not root.right:
                temp = root.left if root.left else root.right
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        root.height = max(self.height(root.left), self.height(root.right)) + 1

        balance = self.balance(root)

        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def search(self, root, key):
        if not root or root.key == key:
            return root
        if root.key < key:
            return self.search(root.right, key)
        return self.search(root.left, key)
    
    def in_order(self, root):
        result = []

        if root:
            result = self.in_order(root.left)
            result.append(root.key)
            result = result + self.in_order(root.right)
        
        return result

    def pre_order(self, root):
        result = []

        if root:
            result.append(root.key)
            result = result + self.pre_order(root.left)
            result = result + self.pre_order(root.right)
        
        return result
    
    def post_order(self, root):
        result = []

        if root:
            result = self.post_order(root.left)
            result = result + self.post_order(root.right)
            result.append(root.key)
        
        return result