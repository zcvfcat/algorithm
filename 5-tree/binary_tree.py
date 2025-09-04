from collections import deque


class TreeNode:
    """
    이진 트리 노드
    - val: 값
    - left, right: 자식 노드
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_level(values):
    """
    레벨 순서 리스트로부터 이진 트리 구성. None은 비어있는 노드.
    예) [1, 2, 3, None, 4] ->      1
                                /    \
                               2      3
                                \
                                 4
    """
    if not values:
        return None
    it = iter(values)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    queue = deque([root])
    for left_val in it:
        node = queue.popleft()
        right_val = next(it, None)
        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)
    return root


def preorder(root):
    """전위 순회: root -> left -> right"""
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def inorder(root):
    """중위 순회: left -> root -> right"""
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def postorder(root):
    """후위 순회: left -> right -> root"""
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result


def level_order(root):
    """레벨 순회: BFS 순서로 각 레벨을 왼쪽에서 오른쪽으로 방문"""
    if not root:
        return []
    q = deque([root])
    order = []
    while q:
        node = q.popleft()
        order.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return order


def height(root):
    """트리 높이(노드 수 기준 경로 길이). 빈 트리 높이 0, 단일 노드 1."""
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def size(root):
    """트리의 총 노드 수"""
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)


