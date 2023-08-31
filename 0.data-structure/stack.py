# 삽입, 삭제 O(1)
# 검색 O(n)

class Stack:
    def __init__(self) -> None:
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0
