class Solution:
    def countBits(self, num: int) -> List[int]:
        ans=[0]*(num+1)
        for i in range(1,num+1):
            if(i%2==0):
                ans[i]=ans[i//2]
            else:
                ans[i]=ans[i//2]+1
        return ans