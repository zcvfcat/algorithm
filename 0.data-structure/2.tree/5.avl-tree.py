"""
    AVL Tree
        균형 잡힌 이진 트리
        모든 노드의 서브트리 높이 차이가 1 이하로 유지되는 트리
    
    시간 복잡도
        삽입 (insert): O(log2N)
        삭제 (delete): O(log2N)
        검색 (search): O(log2N)
    
    사용 이유
        균형 잡힌 트리
            모든 노드의 왼쪽 서브트리와 오른쪽 서브트리의 높이 차이가 1 이하로 유지
                높이 균형을 유지하기 위해 회전 연산 (ll, rr, lr, rl)
        이진 탐색 트리 특성

        높은 검색 성능
            AVL 트리는 균형을 유지하기 때문에 최악의 경우에도 검색, 삽입, 삭제 연산의 시간 복잡도가 O(log n)으로 보장
"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)


avl = AVL_Tree()
root = None

# LL (Left-Left)
root = avl.insert(root, 30)
root = avl.insert(root, 20)
root = avl.insert(root, 40)
root = avl.insert(root, 10)
root = avl.insert(root, 25)

# RR (Right-Right)
root = avl.insert(root, 30)
root = avl.insert(root, 40)
root = avl.insert(root, 20)
root = avl.insert(root, 50)
root = avl.insert(root, 45)

# LR (Left-Right)
root = avl.insert(root, 30)
root = avl.insert(root, 20)
root = avl.insert(root, 40)
root = avl.insert(root, 35)
root = avl.insert(root, 45)

# RL (Right-Left)
root = avl.insert(root, 30)
root = avl.insert(root, 40)
root = avl.insert(root, 20)
root = avl.insert(root, 15)
root = avl.insert(root, 25)
