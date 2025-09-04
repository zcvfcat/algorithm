class SegmentTree:
    """
    세그먼트 트리 (구간 합 예시)
    - 배열의 구간 합 질의와 단일 원소 갱신을 O(log N)에 처리
    """

    def __init__(self, arr):
        self.n = len(arr)
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.tree = [0] * (2 * size)
        # 리프 채우기
        for i, v in enumerate(arr):
            self.tree[size + i] = v
        # 내부 노드 채우기
        for i in range(size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        """arr[index] = value 갱신"""
        i = self.size + index
        self.tree[i] = value
        i //= 2
        while i >= 1:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def query(self, left, right):
        """구간 합 [left, right] (포함)"""
        left += self.size
        right += self.size
        res = 0
        while left <= right:
            if left % 2 == 1:
                res += self.tree[left]
                left += 1
            if right % 2 == 0:
                res += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return res


