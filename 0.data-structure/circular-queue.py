# 삽입, 삭제 O(1)
# 검색 O(n)

class CircularQueue:
    def __init__(self, max_len = 10) -> None:
        self.container = []
        self.max_len = 10
        self.front = 0
        self.rear = 0