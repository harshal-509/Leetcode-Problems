#User function Template for python3
from collections import defaultdict
class Solution:
    def solve(self, n, p ,a, b, d): 
        #code here
        def dfs(i,val):
            vis[i]=1
            if(not(g[i])):
                return i,val
            val=min(val,h[i])
            for j in g[i]:
                if(vis[j]==0):
                    return dfs(j,val)
            
        g=defaultdict(list)
        inc=[0 for i in range(n+1)]
        out=[0 for i in range(n+1)]
        vis=[0 for i in range(n+1)]
        h={}
        for i in range(p):
            h[a[i]]=d[i]
        for i in range(p):
            g[a[i]].append(b[i])
            inc[b[i]]+=1
            out[a[i]]+=1
        ans=0
        ans1=[]
        for i in range(1,n+1):
            val=101
            if(vis[i]==0 and inc[i]==0 and out[i]==1):
                ans+=1
                y,val=dfs(i,val)
                ans1.append([i,y,val])
        return ans1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        
        n,p = map(int,input().strip().split())
        a = []
        b = []
        d = []
        for i in range(p):
            x,y,z = map(int,input().strip().split())
            a.append(x)
            b.append(y)
            d.append(z)
            
        ob = Solution()
        ans = ob.solve(n, p, a, b, d)
        print(len(ans))
        for i in ans:
            print(str(i[0])+" "+str(i[1])+" "+str(i[2]))


# } Driver Code Ends