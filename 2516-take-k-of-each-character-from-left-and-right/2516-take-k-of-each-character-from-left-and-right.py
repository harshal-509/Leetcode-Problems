class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n=len(s)
        pre=[[0,0,0] for i in range(n+1)]
        suff=[[0,0,0] for i in range(n+1)]
        a=0
        b=0
        c=0
        for i in range(n):
            pre[i]=[a,b,c]
            if(s[i]=='a'):
                a+=1
            if(s[i]=='b'):
                b+=1
            if(s[i]=='c'):
                c+=1
        pre[-1]=[a,b,c]
        a=0
        b=0
        c=0
        for i in range(n-1,-1,-1):
            if(s[i]=='a'):
                a+=1
            if(s[i]=='b'):
                b+=1
            if(s[i]=='c'):
                c+=1
            suff[i+1]=[a,b,c]
        def hs(m):
            flag=0
            for i in range(m+1):
                x=i
                y=m-i
                a=pre[x][0]+suff[-y][0]
                b=pre[x][1]+suff[-y][1]
                c=pre[x][2]+suff[-y][2]
                if(a>=k and b>=k and c>=k):
                    flag=1
                    break
            return flag
        ans=-1
        i=k*2
        j=n
        while(i<=j):
            m=i+(j-i)//2
            t=hs(m)
            if(t):
                ans=m
                j=m-1
            else:
                i=m+1
        return ans