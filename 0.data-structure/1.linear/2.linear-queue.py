"""
    Linear Queue (선형 큐)
        선입선출(FIFO)

    시간복잡도
        Enqueue(삽입): O(1)
        Dequeue(삭제): O(1)
        Peek(조회): O(1)
        IsEmpty(비어있는지 확인): O(1)
        Size(크기 확인): O(1)

    사용 이유
        순차적인 데이터 처리
            데이터를 선입선출(FIFO) 순서로 처리할 수 있는 구조
        작업 대기열
            LinearQueue는 작업을 대기시키고, 차례대로 처리
        너비 우선 탐색(BFS)
            BFS 알고리즘에서는 큐를 사용하여 노드를 방문 순서대로 저장
        캐시 구현
            LinearQueue는 최근에 접근한 데이터를 가장 빠르게 제공하는 구조
        이벤트 처리
            이벤트 큐는 사용자 상호작용, 시스템 이벤트 등을 관리하기 위한 용도
"""


class LinearQueue:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.q = []
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, element):
        if self.is_full() is False:
            self.rear = (self.rear + 1) % self.capacity
            self.q.append(element)
            self.size += 1

    def dequeue(self):
        if self.is_empty() is False:
            removed_element = self.q[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return removed_element

    def peek(self):
        if self.is_empty() is False:
            return self.q[self.front]


q = LinearQueue(5)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

removed = q.dequeue()
print(removed)

# front에 있는 요소 확인
front = q.peek()
print(front)
