class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None
        self.color: int = 1


class RedBlackTree:
    def __init__(self) -> None:
        self.root: Node = None
    
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
    
    def insert_fix(self, node: Node):
        pass
