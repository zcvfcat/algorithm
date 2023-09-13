"""
    레드 블랙 트리

    출처
        https://8iggy.tistory.com/188
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.parent= None
        self.left = None
        self.right = None
        self.color = "Red"
    
class RedBlackTree:
    def __init__(self) -> None:
        self.root = None
        self.inserted_node = None
    
    def find(self, data):
        return self._find_data(self.root, data)
    
    def _find_data(self, root, data):
        if root is None or root.data == data:
            return root
        elif root.data >= data:
            return self.find_data(root.left, data)
        elif root.data < data:
            return self._find_data(root.right, data)
    
    def insert(self, data):
        self.root = self._insert_node(self.root, data, None)
        self._balancing(self.insert_node)
        return
    
    def _insert_node(self, cur, data, parent):
        if cur is None:
            cur = Node(data)
            cur.parent = parent
            self.inserted_node= cur
        else:
            if data < cur.data:
                cur.left = self._insert_node(cur.left, data, cur)
            elif data > cur.data:
                cur.right = self._insert_node(cur.right, data, cur)
        return cur
    
    def _balancing(self, node):
        P = node.parent
        if P is None:
            node.color = "Black"
        else:
            if P.color == "Red":
                G = P.parent
                U = None
                if G.left == P:
                    U = G.right
                elif G.right == P:
                    U = G.left
                
                if U is not None and U.color == "Red":
                    P.color, U.color = "Black", "Black"
                    G.color = "Red"

                    self._balancing(G)
                else:
                    if P == G.left and P.left == node:
                        G.color, P.color = P.color, G.color
                        self._right_rotate(G)
                    elif P == G.left and P.right == node:
                        self._left_rotate(P)
                        G.color, node.color = node.color, G.color
                        self._right_rotate(G)
                    elif P == G.right and P.right == node:
                        G.color, P.color = P.color, G.color
                        self._left_rotate(G)
                    elif P == G.right and P.left == node:
                        self._right_rotate(P)
                        G.color, node.color = node.color, G.color
                        self._left_rotate(G)

    def delete(self, data):
        node = self._get_delete_node(self.root, data)
        if node is None:
            return False
        self._delete_node(node)
        return True




