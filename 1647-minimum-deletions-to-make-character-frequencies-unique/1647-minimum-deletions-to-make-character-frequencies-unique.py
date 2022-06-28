class Solution:
    def minDeletions(self, s: str) -> int:
        z=Counter(s)
        def check(i):
            for j in range(97,123):
                y=chr(j)
                if(z[y]==z[i] and i!=y and z[y]!=0):
                    return 1
            return 0
        ans=0
        for i in range(97,123):
            x=chr(i)
            while(check(x)):
                z[x]-=1
                ans+=1
        return ans