class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []

class BPlusTree:
    def __init__(self, max_keys=4):
        self.root = BPlusTreeNode(is_leaf=True)
        self.max_keys = max_keys

    def search(self, node, key):
        # LEAF 노드일시
        if node.is_leaf:
            for i, item in enumerate(node.keys):
                if key == item:
                    return True
            return False

        for i, item in enumerate(node.keys):
            if key < item:
                return self.search(node.children[i], key)
        return self.search(node.children[-1], key)
    
    def insert(self, key):
        root = self.root
        if len(root.keys) != self.max_keys:
            self._insert_non_full(self.root, key)

        new_root = BPlusTreeNode()
        new_root.children.append(self.root)
        self.split_child(new_root, 0, self.root)
        self.root = new_root