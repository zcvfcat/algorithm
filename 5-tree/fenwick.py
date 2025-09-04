class FenwickTree:
    """
    펜윅 트리(Binary Indexed Tree): 부분합/단일 갱신을 O(log N)으로 처리
    인덱스는 0 기반 입력을 1 기반 내부로 변환하여 저장.
    """

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, index, delta):
        """arr[index] += delta"""
        i = index + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, index):
        """arr[0..index] 합"""
        s = 0
        i = index + 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, left, right):
        """arr[left..right] 합"""
        if right < left:
            return 0
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


