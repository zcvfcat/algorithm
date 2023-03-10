class Node:
    def __init__(self, key, value, M):
        self.key = key
        self.value = value
        self.children = [None] * M


class MTree:
    def __init__(self, M):
        self.M = M
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value, self.M)
        else:
            self.insert_node(key, value, self.root)

    def insert_node(self, key, value, node):
        if key == node.key:
            node.value = value
            return

        child_index = self.get_child_index(key, node)
        if node.children[child_index] is None:
            node.children[child_index] = Node(key, value, self.M)
        else:
            self.insert_node(key, value, node.children[child_index])

    def get_child_index(self, key, node):
        return key % self.M

    def search(self, key):
        if self.root is None:
            return None
        return self.search_node(key, self.root)

    def search_node(self, key, node):
        if key == node.key:
            return node.value

        child_index = self.get_child_index(key, node)
        if node.children[child_index] is None:
            return None
        else:
            return self.search_node(key, node.children[child_index])


# 테스트
tree = MTree(5)
tree.insert(1, 'A')
tree.insert(2, 'B')
tree.insert(11, 'K')
tree.insert(6, 'F')

print(tree.search(1))  # A
print(tree.search(2))  # B
print(tree.search(11))  # K
print(tree.search(6))  # F
print(tree.search(3))  # None
