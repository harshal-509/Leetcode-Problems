from collections import defaultdict
class Solution:
    def __init__(self):
        self.ans=0
    def pathMoreThanK (self, V, E, K, A):
        # code here
        def dfs(i,c):
            vis[i]=1
            if(c>=K):
                self.ans=1
                return
            for j in d[i]:
                if(vis[j[0]]==0):
                    dfs(j[0],j[1]+c)
            vis[i]=0
        d=defaultdict(list)
        n=len(A)
        for i in range(0,n,3):
            d[A[i]].append((A[i+1],A[i+2]))
            d[A[i+1]].append((A[i],A[i+2]))
        vis=[0 for i in range(V)]
        dfs(0,0)
        a=self.ans
        self.ans=0
        return a
#{ 
#  Driver Code Starts



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        V, E, K= map(int, input().split())
        A = list(map(int, input().split()))
        ans = ob.pathMoreThanK(V, E, K, A);
        if(ans):
            print(1)
        else:
            print(0)


# } Driver Code Ends