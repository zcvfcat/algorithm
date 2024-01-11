class CircleQueue:
    def __init__(self) -> None:
        self.items = []
        self.max_len = 10
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