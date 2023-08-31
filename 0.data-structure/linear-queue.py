# 삽입, 삭제 O(1)
# 검색 O(n)

class LinearQueue:
    def __init__(self) -> None:
        self.container = []

    def enqueue(self, item):
        self.container.append(item)

    def dequeue(self):
        return self.container.pop(0)

    def is_empty(self):
        return len(self.container) == 0
