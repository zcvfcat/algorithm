"""
    Deque(Double-ended Queue)
        큐(Queue)와 스택(Stack)의 특성을 모두 갖는 자료구조

    시간 복잡도
        삽입(insert): O(1)
        삭제(delete): O(1)
        조회(search): O(1)

    왜 사용하는가?
        1. 효율적인 데이터 조작
            덱은 양쪽에 대해 삽입삭제가 O(1) 보장
        2. 슬라이딩 윈도우 알고리즘 관리
            윈도우의 양 끝 위치에서 효율적으로 추가하거나 제거
        3. 회전 큐 구현
        4. BFS
"""


class Deque:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)


deque = Deque()

# 요소 추가
deque.add_front(3)   # [3]
deque.add_front(2)   # [2, 3]
deque.add_rear(4)    # [2, 3, 4]

print(deque.items)

# 요소 제거
deque.remove_front()  # 2 (2 제거됨)
deque.remove_rear()  # 4 (4 제거됨)

print(deque.items)

# 사이즈 확인
print(deque.size())  # 1
