class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        i=0
        t=""
        while(i<n):
            if(int(t+s[i])<=k):
                t+=s[i]
            else:
                t=s[i]
                if(int(t)>k):
                    return -1
                ans+=1
            i+=1
        return ans+1