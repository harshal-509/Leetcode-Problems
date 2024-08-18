class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = set()
        s.add(1)
        for i in range(n):
            x= min(s)
            s.remove(x)
            s.add(x* 2)
            s.add(x* 3)
            s.add(x* 5)
        return x