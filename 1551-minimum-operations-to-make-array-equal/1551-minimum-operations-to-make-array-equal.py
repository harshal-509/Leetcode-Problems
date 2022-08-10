class Solution:
    def minOperations(self, n: int) -> int:
        ans=0
        for i in range(1,n,2):
            ans+=n-i
        return ans