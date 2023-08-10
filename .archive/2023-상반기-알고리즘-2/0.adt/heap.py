class Heap:
    def __init__(self, heap_list=None):
        if heap_list == None:
            self.lst = []
        else:
            self.lst = heap_list

    def insert(self, value):
        self.lst.append(value)
        index = len(self.lst) - 1
        parent_index = (index - 1) // 2

        while parent_index >= 0 and self.lst[parent_index] < self.lst[index]:
            self.lst[parent_index], self.lst[index] = self.lst[index], self.lst[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def remove(self):
        if len(self.lst) == 0:
            return None

        if len(self.lst) == 1:
            return self.lst.pop()

        max_value = self.lst[0]
        self.lst[0] = self.lst.pop()
        index = 0
        child_left_index = (index * 2) + 1
        child_right_index = (index * 2) + 2
        
        while child_left_index < len(self.lst) and self.lst[child_left_index] > self.lst[index] or \
            child_right_index < len(self.lst) and self.lst[child_right_index] > self.lst[index]:

            if child_right_index < len(self.lst) and self.lst[child_right_index] > self.lst[child_left_index]:
                self.lst[child_right_index], self.lst[index] = self.lst[index], self.lst[child_right_index]
                index = child_right_index
            else:
                self.lst[child_left_index], self.lst[index] = self.lst[index], self.lst[child_left_index]
                index = child_left_index

            child_left_index = (index * 2) + 1
            child_right_index = (index * 2) + 2

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
