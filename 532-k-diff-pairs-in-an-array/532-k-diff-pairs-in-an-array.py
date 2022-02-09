class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        z=Counter(nums)
        ans=0
        if(k==0):
            for i in z:
                if(z[i]>=2):
                    ans+=1
            return ans
        for i in z:
            if(z[i-k]):
                ans+=1
            if(z[i+k]):
                ans+=1
        return ans//2