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
        if node.is_leaf:
            for i, item in enumerate(node.keys):
                if key == item:
                    return True
            return False
        else:
            for i, item in enumerate(node.keys):
                if key < item:
                    return self.search(node.children[i], key)
            return self.search(node.children[-1], key)

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.max_keys:
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self.split_child(new_root, 0, self.root)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def split_child(self, parent, i, node):
        new_node = BPlusTreeNode(is_leaf=node.is_leaf)
        mid = len(node.keys) // 2
        parent.keys.insert(i, node.keys[mid])
        parent.children.insert(i + 1, new_node)

        new_node.keys = node.keys[mid + 1:]
        node.keys = node.keys[:mid]

        if not node.is_leaf:
            new_node.children = node.children[mid + 1:]
            node.children = node.children[:mid + 1]

    def _insert_non_full(self, node, key):
        if node.is_leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            for i, item in enumerate(node.keys):
                if key < item:
                    child = node.children[i]
                    if len(child.keys) == self.max_keys:
                        self.split_child(node, i, child)
                        if key > node.keys[i]:
                            i += 1
                    self._insert_non_full(node.children[i], key)
                    return
            child = node.children[-1]
            if len(child.keys) == self.max_keys:
                self.split_child(node, len(node.keys), child)
            self._insert_non_full(node.children[-1], key)

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        if not node.is_leaf:
            for child in node.children:
                self.display(child, level + 1)

# B+ 트리 생성 및 테스트
tree = BPlusTree(max_keys=4)
keys = [20, 10, 30, 40, 50, 60, 70, 80, 90]

for key in keys:
    tree.insert(key)

tree.display()

# 검색 테스트
print(tree.search(tree.root, 50))  # True
print(tree.search(tree.root, 15))  # False