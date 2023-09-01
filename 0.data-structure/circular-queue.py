"""
    CircularQueue
        한 쪽 끝과 다른 쪽 끝이 연결된 구조

    시간 복잡도
        enqueue: O(1)
        dequeue: O(1)
        front: O(1)
        rear: O(1)

    사용 이유
        큐의 최대 길이가 정해져 있는 경우
            배열 기반의 큐를 구현하면 효율적인 데이터 관리
        메모리 제한이 있는 시스템
            한정된 메모리를 효율적으로 활용
"""


class CircularQueue:
    def __init__(self, max_len=10):
        self.items = []
        self.max_len = max_len
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.max_len == self.front

    def enqueue(self, value):
        if not self.is_full():
            self.items.append(value)
            self.rear = (self.rear + 1) % self.max_len

    def dequeue(self):
        if not self.is_empty():
            value = self.items[self.front]
            self.front = (self.front + 1) % self.max_len
            return value

    def get_front(self):
        if not self.is_empty():
            return self.items[self.front]

    def get_rear(self):
        if not self.is_empty():
            return self.items[self.rear - 1]


cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)

print(cq.get_front())  # 1
print(cq.get_rear())   # 5

cq.dequeue()
cq.enqueue(6)

print(cq.get_front())  # 2
print(cq.get_rear())   # 6
