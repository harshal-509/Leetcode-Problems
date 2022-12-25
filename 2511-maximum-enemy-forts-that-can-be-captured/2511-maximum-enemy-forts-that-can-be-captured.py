class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans=0
        n=len(forts)
        t=0
        flag=0
        i=0
        while(i<n):
            if(forts[i]==1):
                t=0
                j=i+1
                while(j<n and forts[j]==0):
                    j+=1
                    t+=1
                if(j<n):
                    if(forts[j]==-1):
                        ans=max(ans,t)
                i=j
            else:
                i+=1
        i=n-1
        while(i>=0):
            if(forts[i]==1):
                t=0
                j=i-1
                while(j>=0 and forts[j]==0):
                    j-=1
                    t+=1
                if(j>=0):
                    if(forts[j]==-1):
                        ans=max(ans,t)
                i=j
            else:
                i-=1
        return ans