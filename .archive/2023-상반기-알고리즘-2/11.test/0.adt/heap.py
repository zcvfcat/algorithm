# 최대 힙
# [5, 4, 3, 2, 1]
# [1, 4, 3, 2]
# [4, 1, 3, 2]
# [4, 2, 3, 1]

# 최소 힙
# [1, 2, 3, 4, 5]
# [5, 2, 3, 4]
# [2, 5, 3, 4]
# [2, 4, 3, 5]

class Heap:
    def __init__(self, lst=None):
        if lst == None:
            self.lst = []
        else:
            self.lst = lst

    def insert(self, value):
        self.lst.append(value)
        idx = len(self.lst) - 1
        parent_idx = (idx - 1) // 2

        while parent_idx >= 0 and self.lst[parent_idx] < self.lst[idx]:
            self.lst[parent_idx], self.lst[idx] = self.lst[idx], self.lst[parent_idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2
    
    def remove(self):
        if len(self.lst) == 0:
            return None
        
        if len(self.lst) == 1:
            return self.lst.pop()
        
        max_value = self.lst[0]
        self.lst[0] = self.lst.pop()
        idx = 0
        child_left_idx = (idx * 2) + 1
        child_right_idx = (idx * 2) + 2

        while child_left_idx < len(self.lst) and self.lst[child_left_idx] > self.lst[idx] or \
            child_right_idx < len(self.lst) and self.lst[child_right_idx] > self.lst[idx]:

            if child_right_idx < len(self.lst) and self.lst[child_right_idx] > self.lst[child_left_idx]:
                self.lst[child_right_idx], self.lst[idx] = self.lst[idx],  self.lst[child_right_idx]
                idx = child_right_idx
            else:
                self.lst[child_left_idx], self.lst[idx] = self.lst[idx], self.lst[child_left_idx]
                idx = child_left_idx
            
            child_left_idx = (idx * 2) + 1
            child_right_idx = (idx * 2) + 2

        return max_value


h = Heap()

h.insert(1)
h.insert(2)
h.insert(3)
h.insert(4)
h.insert(5)
h.insert(6)
print(h.lst)
print(h.remove())
print(h.lst)