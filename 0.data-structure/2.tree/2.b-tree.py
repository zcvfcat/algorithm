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
"""


class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.child = []
        self.leaf = leaf


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root

        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        print(x.leaf)
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1

            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)

        x.child.insert(i + 1, z)
        x.keys.insert[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]

        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def search(self, k, x=None):
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1

            if i < len(x.keys) and k == x.keys[i]:
                return x
            elif x.leaf:
                return None
            else:
                return self.search(k, x.child[i])
        else:
            return self.search(k, self.root)


btree = BTree(3)  # t = 3으로 설정된 B-트리 생성

# 키 삽입
btree.insert(10)
btree.insert(20)
btree.insert(5)
btree.insert(15)
btree.insert(25)

# 특정 키 검색
result = btree.search(15)
if result:
    print("15를 찾았습니다")
else:
    print("15를 찾을 수 없습니다")

# 존재하지 않는 키 검색
result = btree.search(30)
if result:
    print("30을 찾았습니다")
else:
    print("30을 찾을 수 없습니다")
