class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = deque(range(1, n + 1))
        while len(circle) > 1:
            for _ in range(k - 1):
                circle.append(circle.popleft())
            circle.popleft()
        return circle[0]