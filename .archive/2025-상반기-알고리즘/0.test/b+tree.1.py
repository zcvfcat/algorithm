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
            return key in node.keys

        for i, item in enumerate(node.keys):
            if key < item:
                return self.search(node.children[i], key)

        return self.search(node.children[-1], key)

    def insert(self, key):
        root = self.root
        # 루트 노드가 가득 찬 경우에만 새로운 루트를 생성합니다.
        if len(root.keys) == self.max_keys:
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self.split_child(new_root, 0, self.root)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def split_child(self, parent, i, node):
        next_node = BPlusTreeNode(is_leaf=node.is_leaf)
        mid = len(node.keys) // 2

        # 부모에 중간 값을 추가하고, 부모의 자식에 새로운 노드를 연결합니다.
        parent.keys.insert(i, node.keys[mid])
        parent.children.insert(i + 1, next_node)

        # 노드를 분할하여 키와 자식을 분배합니다.
        next_node.keys = node.keys[mid + 1:]
        node.keys = node.keys[:mid]

        if not node.is_leaf:
            next_node.children = node.children[mid + 1:]
            node.children = node.children[:mid + 1]

    def _insert_non_full(self, node, key):
        if node.is_leaf:
            node.keys.append(key)
            node.keys.sort()
            return

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
