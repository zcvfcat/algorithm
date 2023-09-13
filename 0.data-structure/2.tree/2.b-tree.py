"""
    B-Tree
        효율적인 데이터 저장 및 검색을 위한 트리 구조 데이터 구조
    
    시간 복잡도
        삽입, 삭제, 검색 O(log2N)
    
    사용 이유
        데이터베이스 관리 시스템(DBMS)
            인덱스를 구현하는데 자주 사용
        파일 시스템
            파일 및 디렉토리 구조를 관리시 B-tree 활용
        외부 메모리 관리
            디스크 접근 비용을 최소화 하여 I/O 작업을 최적화
        정렬된 데이터 유지
            B-tree는 데이터를 정렬된 상태로 유지하므로 정렬된 데이터 검색이 빠름
        범위 검색
            범위 검색시 유용
    
    코드
        구현이 빡세므로... 나중에 ^______^ 하자

    출처
        https://8iggy.tistory.com/190
"""



import bisect


class BTreeNode:
    def __init__(self, keys, children, is_leaf) -> None:
        self.keys = keys
        self.children = children
        self.is_leaf = is_leaf


class BTree:
    def __init__(self, t) -> None:
        self.root = BTreeNode([], [], True)
        self.t = t

    def search(self, key):
        return self._search_key(key, self.root)

    def _search(self, key, node):
        i = bisect.bisect_leaf(node.keys, key)

        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
        elif node.is_leaf:
            return None
        else:
            return self._search_key(key, node.children[i])

    def insert(self, key):
        if len(self.root.keys) == 2 * self.t - 1:
            self.root = BTreeNode([], [self.root], False)
            self._split_child(self.root, 0)
        self._insert_key(key, self.root)

    def _insert_key(self, key, node):
        i = bisect.bisect_left(node.keys, key)
        if node.is_leaf:
            node.keys.insert(i, key)
        else:
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i = i + 1
            self._insert_key(key, node.children[i])

    def _split_child(self, node, i):
        c = node.children[i]
        c_l = BTreeNode(c.keys[0: self.t - 1], c.children[0:self.t], c.is_leaf)
        c_r = BTreeNode(c.keys[self.t:2 * self.t - 1], c.children[self.t: 2 * self.t], c.is_leaf)

        median = c.keys[self.t - 1]
        node.keys.insert(i, median)
        node.children[i] = c_l
        node.children.insert(i + 1, c_r)

    def delete(self, key):
        if len(self.root.keys) == 1:
            root = self.root
            t = self.t
            left, right = root.children[0], root.children[1]

            if len(left.keys) == t - 1 and len(right.keys) == t - 1:
                self.root = BTreeNode([],[],False)
                self.root.keys.extend(left.keys)
                self.root.keys.extend(root.keys)
                self.root.keys.extend(right.keys)
                self.root.children.extend(left.children)
                self.root.children.extend(right.children)

                if len(self.root.children) == 0:
                    self.root.is_leaf = True
        
        self._delete_key(key, self.root)
    
    def _delete_key(self, key, node):
        i = bisect.bisect_left(node.keys, key)

        if i < len(node.keys) and node.keys[i] == key:
            if node.is_leaf:
                node.keys.pop(i)
                return
            else:
                successor = self._find_successor(node.children[i + 1])
                node.keys[i], successor.keys[0] = successor.keys[0], node.keys[i]
                self._delete_key(key, node.children[i + 1])
        else:
            if len(node.children[i].keys) == self.t - 1:
                self._delete_balancing(node.children[i], node, i)
            i = bisect.bisect_left(node.keys, key)
            self._delete_key(key, node.children[i])
    
    def _delete_balancing(self, node, parent, i):
        if i == len(parent.children) - 1:
            if len(parent.children[i - 1].keys) > self.t - 1:
                node.keys.insert(0, parent.keys.pop())
                parent.keys.append(parent.children[i - 1].keys.pop() )
                if len(parent.children[i - 1].children) > 0:
                    node.children.insert(0, parent.children[i - 1].children.pop())
            else:
                parent.children[i - 1].keys.append(parent.keys.pop())
                parent.children[i - 1].keys.extend(node.keys)
                parent.children.pop()
        elif i == 0:
            if len(parent.children[i + 1].keys) > self.t - 1:
                node.keys.append(parent.keys.pop(0))
                parent.keys.insert(0, parent.children[i + 1].keys.pop(0))
                if len(parent.children[i + 1].children) > 0:
                    node.children.append(parent.children[i + 1].children.pop(0))
            else:
                parent.children[i + 1].keys.insert(0, parent.keys.pop(0))
                for k in node.keys:
                    parent.children[i + 1].keys.insert(0, k)
                parent.children.pop(0)
        else:
            if len(parent.children[i - 1].keys) > self.t - 1:
                node.keys.insert(0, parent.keys[i])
                parent.keys[i] = parent.children[i - 1].keys.pop()
                if len(parent.children[i - 1].children) > 0:
                    node.children.insert(0, parent.children[i - 1].children.pop())
            elif len(parent.children[i - 1].keys) > self.t - 1:
                node.keys.append(parent.keys[i])
                parent.keys[i] = parent.children[i + 1].keys.pop(0)
                if len(parent.children[i + 1].children) > 0:
                    node.children.append(parent.children[i + 1].children.pop(0))
            else:
                parent.children[i - 1].keys.append(parent.keys.pop(i - 1))
                parent.children[i - 1].keys.extend(node.keys)
                parent.children.pop(i)
    
    def _find_successor(self,node):
        if node.is_leaf:
            return node
        else:
            return self._find_successor(node.children[0])
    
    def print_tree(self, node, l = 0):
        for i in node.keys:
            print(i, end = " ")
        print()
        l += 1

        if len(node.children) > 0:
            for i in node.children:
                self.print_tree(i, l)


            

# -------------------------

# class BTreeNode:
#     def __init__(self, leaf=False):
#         self.keys = []
#         self.child = []
#         self.leaf = leaf

# class BTree:
#     def __init__(self, t):
#         self.root = BTreeNode(True)
#         self.t = t

#     def insert(self, k):
#         root = self.root

#         if len(root.keys) == (2 * self.t) - 1:
#             temp = BTreeNode()
#             self.root = temp
#             temp.child.insert(0, root)
#             self.split_child(temp, 0)
#             self.insert_non_full(temp, k)
#         else:
#             self.insert_non_full(root, k)

#     def insert_non_full(self, x, k):
#         i = len(x.keys) - 1
#         print(x.leaf)
#         if x.leaf:
#             x.keys.append((None, None))
#             while i >= 0 and k < x.keys[i]:
#                 x.keys[i + 1] = x.keys[i]
#                 i -= 1
#             x.keys[i + 1] = k
#         else:
#             while i >= 0 and k < x.keys[i]:
#                 i -= 1

#             i += 1
#             if len(x.child[i].keys) == (2 * self.t) - 1:
#                 self.split_child(x, i)
#                 if k > x.keys[i]:
#                     i += 1
#             self.insert_non_full(x.child[i], k)

#     def split_child(self, x, i):
#         t = self.t
#         y = x.child[i]
#         z = BTreeNode(y.leaf)

#         x.child.insert(i + 1, z)
#         x.keys.insert[t: (2 * t) - 1]
#         y.keys = y.keys[0: t - 1]

#         if not y.leaf:
#             z.child = y.child[t: 2 * t]
#             y.child = y.child[0: t - 1]

#     def search(self, k, x=None):
#         if isinstance(x, BTreeNode):
#             i = 0
#             while i < len(x.keys) and k > x.keys[i]:
#                 i += 1

#             if i < len(x.keys) and k == x.keys[i]:
#                 return x
#             elif x.leaf:
#                 return None
#             else:
#                 return self.search(k, x.child[i])
#         else:
#             return self.search(k, self.root)

# btree = BTree(3)  # t = 3으로 설정된 B-트리 생성

# # 키 삽입
# btree.insert(10)
# btree.insert(20)
# btree.insert(5)
# btree.insert(15)
# btree.insert(25)

# # 특정 키 검색
# result = btree.search(15)
# if result:
#     print("15를 찾았습니다")
# else:
#     print("15를 찾을 수 없습니다")

# # 존재하지 않는 키 검색
# result = btree.search(30)
# if result:
#     print("30을 찾았습니다")
# else:
#     print("30을 찾을 수 없습니다")
