class MyQueue:

    def __init__(self):
        self.a=deque([])

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        return self.a.popleft()

    def peek(self) -> int:
        return self.a[0]

    def empty(self) -> bool:
        return not(len(self.a))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()