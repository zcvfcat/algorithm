class Heap:
    def __init__(self, q=None) -> None:
        if q == None:
            self.q = []
        else:
            self.q = q

    def insert(self, v):
        self.q.append(v)
        idx = len(self.q) - 1
        p_idx = (idx - 1) // 2
        while p_idx >= 0 and self.q[p_idx] < self.q[idx]:
            self.q[p_idx], self.q[idx] = self.q[idx], self.q[p_idx]
            idx = p_idx
            p_idx = (idx - 1) // 2

    def remove(self):
        if len(self.q) == 0:
            return None

        if len(self.q) == 1:
            return self.q.pop()

        max_value = self.q.pop(0)

        idx = 0

        l_idx = (idx * 2) + 1
        r_idx = (idx * 2) + 2

        while l_idx < len(self.q) and self.q[l_idx] > self.q[idx] \
                or r_idx < len(self.q) and self.q[r_idx] > self.q[idx]:

            if r_idx < len(self.q) and self.q[r_idx] > self.q[l_idx]:
                self.q[r_idx], self.q[idx] = self.q[idx], self.q[r_idx]
                idx = r_idx
            else:
                self.q[l_idx], self.q[idx] = self.q[idx], self.q[l_idx]
                idx = l_idx

            l_idx = (idx * 2) + 1
            r_idx = (idx * 2) + 2

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