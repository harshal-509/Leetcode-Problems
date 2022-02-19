from sortedcontainers import *
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        sl = SortedList([i*2 if i%2==1 else i for i in nums])
        diff = float('inf')
        while sl[-1] % 2 == 0:
            diff = min(diff, sl[-1]-sl[0])
            sl.add(sl.pop(-1) // 2)
        return min(diff, sl[-1]-sl[0])