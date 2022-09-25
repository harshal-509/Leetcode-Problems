class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.t = [0]*k
        self.front = self.rear = -1
    def enQueue(self, value):
        if self.size == self.max_size:
            return 0
        if self.rear == -1:
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1)%self.max_size
        self.t[self.rear] = value
        self.size += 1
        return 1       
    def deQueue(self):
        if self.size == 0:
            return 0
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1)%self.max_size
        self.size -= 1
        return 1
    def Front(self):
        if self.size != 0:
            return self.t[self.front]     
        else:
            return -1
    def Rear(self):
        if self.size != 0:
            return self.t[self.rear] 
        else:
            return -1
    def isEmpty(self):
        return self.size == 0
    def isFull(self):
        return self.size == self.max_size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()