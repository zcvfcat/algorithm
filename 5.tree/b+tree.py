class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

    def insert_non_full(self, key):
        if self.leaf:
            self.keys.append(key)
            self.keys.sort()
        else:
            i = 0
            while i < len(self.keys) and key > self.keys[i]:
                i += 1
            if len(self.children[i].keys) == self.order - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        new_node = BPlusTreeNode(leaf=self.children[i].leaf)
        mid = len(self.children[i].keys)//2
        new_node.keys = self.children[i].keys[mid:]
        self.children[i].keys = self.children[i].keys[:mid]

        if not self.children[i].leaf:
            new_node.children = self.children[i].children[mid:]
            self.children[i].children = self.children[i].children[:mid]

        self.children.insert(i+1, new_node)


class BPlusTree:
    def __init__(self, order=4):
        self.root = BPlusTreeNode(True)
        self.root.order = order
        self.order = order

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.order - 1:
            new_root = BPlusTreeNode()
            new_root.children.append(root)
            new_root.split_child(0)
            new_root.insert_non_full(key)
            self.root = new_root
        else:
            root.insert_non_full(key)

    def search(self, key, node=None):
        if node is None:
            node = self.root

        if node.leaf:
            return key in node.keys

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        return self.search(key, node.children[i])

    def display(self, key, node=None, level=0):
        if node is None:
            node = self.root

        print(f'level {level} : {node.keys}')

        if not node.leaf:
            for i in range(len(node.keys)):
                self.display(key, node.children[i], level + 1)

