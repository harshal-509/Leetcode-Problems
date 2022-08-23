class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans=[]
        t=s[0]
        p=1
        n=len(s)
        st=0
        for i in range(1,n):
            if(t==s[i]):
                p+=1
            else:
                if(p>=3):
                    ans.append([st,i-1])
                p=1
                t=s[i]
                st=i
        if(p>=3):
            ans.append([st,n-1])
        return ans