"""
    이진 트리
        최대 두 개의 자식 노드를 가지는 트리

    시간 복잡도
        삽입 (insert): O(log2N)
        검색 (search): O(log2N)
    
    사용하는 이유
        시간 복잡도가 검색 시, 선형 구조보다 작기 때문에 사용
        최악의 경우 N으로 만듬, 따라서 avl, 레드-블랙 트리로 변경해서 사용

    코드
        아래의 코드는 완전 이진 트리가 아닌 `이진트리`
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, curr, value):
        if value < curr.value:
            if curr.left is None:
                curr.left = Node(value)
            else:
                self._insert_recursive(curr.left, value)
        else:
            if curr.right is None:
                curr.right = Node(value)
            else:
                self._insert_recursive(curr.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, curr, value):
        if curr is None or curr.value == value:
            return curr
        elif value < curr.value:
            return self._search_recursive(curr.left, value)
        else:
            return self._search_recursive(curr.right, value)


tree = BinaryTree()

tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

result = tree.search(8)

if(result):
    print(result.value)
