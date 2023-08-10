
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1

# Red Black Tree class
class RedBlackTree:
    def __init__(self):
        self.root = None

    # Tree Insertion
    def insert(self, data):
        node = Node(data)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        node.left = None
        node.right = None
        node.color = 0
        self.insert_fix(node)

    def insert_fix(self, node):
        while node.parent != None and node.parent.color == 0:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y != None and y.color == 0:
                    node.parent.color = 1
                    y.color = 1
                    node.parent.parent.color = 0
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 1
                    node.parent.parent.color = 0
                    self.right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y != None and y.color == 0:
                    node.parent.color = 1
                    y.color = 1
                    node.parent.parent.color = 0
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 1
                    node.parent.parent.color = 0
                    self.left_rotate(node.parent.parent)
        self.root.color = 1

    # Left Rotate
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Right Rotate
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Print Tree
    def inorder_tree_walk(self, node):
        if node != None:
            self.inorder_tree_walk(node.left)
            print(node.data, end=' ')
            if node.color == 0:
                print('(RED)', end=' ')
            else:
                print('(BLACK)', end=' ')
            self.inorder_tree_walk(node.right)

# Main program
tree = RedBlackTree()

# Insertion
lst = [7, 6, 5, 4, 3, 2, 1]
for i in lst:
    tree.insert(i)

# Print Tree
print('Inorder Tree Walk: ')
tree.inorder_tree_walk(tree.root)

# Output
# Inorder Tree Walk: 
# 1 (BLACK) 2 (RED) 3 (BLACK) 4 (RED) 5 (BLACK) 6 (RED) 7 (BLACK)