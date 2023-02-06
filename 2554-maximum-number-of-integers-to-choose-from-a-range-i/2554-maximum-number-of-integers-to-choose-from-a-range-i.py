class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        z=Counter(banned)
        ans=0
        s=0
        for i in range(1,n+1):
            if(z[i]==0 and s+i<=maxSum):
                ans+=1
                s+=i
        return ans