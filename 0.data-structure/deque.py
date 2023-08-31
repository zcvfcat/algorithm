# 삽입, 삭제 O(1)
# 검색 O(n)

class Deque:
    def __init__(self) -> None:
        self.container = []
