"""
    우선순위 큐

    시간 복잡도
        삽입(Insert): O(log2n)
        삭제(Delete): O(log2n)
        최솟값/최댓값 확인(Get Minimum/Maximum): O(1)

    사용하는 이유
        1. 우선순위에 따른 데이터 정렬
            우선 순위에 따라 정렬되어 저장되는 자료구조
        2. 최솟값 또는 최댓값 검색
            내부적으로 데이터를 정렬하여 가장 작은 값 또는 가장 큰 값을 빠르게 찾음
        3. 이벤트 스케줄링
            우선순위에 따라 이벤트를 처리하는데 사용
        4. 힙 자료구조의 구현
            힙은 최소 힙 또는 최대 힙과 같은 정렬된 완전 이진 트리
            우선 순위 큐를 사용하여 힙을 구현할 수 있음
            힙의 특성을 이용하여 효율적인 데이터 정렬 및 검색 가능
"""


class Heap:
    def __init__(self, q=None) -> None:
        if q == None:
            self.q = []
        else:
            self.q = q

    def insert(self, v):
        self.q.append(v)

        idx = len(self.q) - 1
        parent = (idx - 1) // 2

        while parent >= 0 and self.q[parent] < self.q[idx]:
            self.q[parent], self.q[idx] = self.q[idx], self.q[parent]

            idx = parent
            parent = (idx - 1) // 2

    def remove(self):
        if len(self.q) == 0:
            return None

        if len(self.q) == 1:
            return self.q.pop()

        # swap and pop
        max_value = self.q[0]
        self.q[0] = self.q.pop()

        idx = 0

        left = (idx * 2) + 1
        right = (idx * 2) + 2

        while left < len(self.q) and self.q[left] > self.q[idx] \
                or right < len(self.q) and self.q[right] > self.q[idx]:

            if right < len(self.q) and self.q[right] > self.q[left]:
                self.q[right], self.q[idx] = self.q[idx], self.q[right]
                idx = right

            else:
                self.q[left], self.q[idx] = self.q[idx], self.q[left]
                idx = left

            left = (idx * 2) + 1
            right = (idx * 2) + 2

        return max_value


h = Heap()

h.insert(1)
h.insert(2)
h.insert(3)
h.insert(4)
h.insert(5)
h.insert(6)
print(h.q)
print(h.remove())
print(h.q)
