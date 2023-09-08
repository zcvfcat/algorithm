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
    def __init__(self, keys, children, is_leaf) -> None:
        self.keys = keys
        self.children = children
        self.is_leaf = is_leaf


class BTree:
    def __init__(self, t) -> None:
        self.root = BTreeNode([], [], True)
        self.t = t
