class BSTNode:
    """이진 탐색 트리 노드"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    이진 탐색 트리(BST)
    - 모든 노드에 대해: left의 값 < node의 값 < right의 값
    """

    def __init__(self):
        self.root = None

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def insert(self, key):
        if not self.root:
            self.root = BSTNode(key)
            return
        node = self.root
        while True:
            if key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = BSTNode(key)
                    return
            elif key > node.key:
                if node.right:
                    node = node.right
                else:
                    node.right = BSTNode(key)
                    return
            else:
                return  # 중복 키는 무시

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        def _delete(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                successor = self._min_node(node.right)
                node.key = successor.key
                node.right = _delete(node.right, successor.key)
            return node

        self.root = _delete(self.root, key)

    def inorder(self):
        res = []

        def _in(node):
            if not node:
                return
            _in(node.left)
            res.append(node.key)
            _in(node.right)

        _in(self.root)
        return res


