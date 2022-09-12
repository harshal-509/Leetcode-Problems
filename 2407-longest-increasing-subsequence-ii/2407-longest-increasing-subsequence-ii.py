class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n
        
    def getMax(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])
            
    def getMin(self, l, r) :
        l += self.n
        r += self.n
        res = float('inf')
        while l < r :
            if l & 1 : 
                res = min(res, self.tree[l])
                l += 1
            l >>= 1
            if r & 1 :
                r -= 1      
                res = min(res, self.tree[r]) 
            r >>= 1
        return res
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n, ans = max(nums), 1
        seg = SEG(n)
        for a in nums:
            a -= 1
            x = seg.getMax(max(0, a - k), a)
            ans = max(ans,x + 1)
            seg.update(a,x + 1)
        return ans