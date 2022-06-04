#User function Template for python3
from collections import *
class Solution:
    def __init__(self):
        self.ans=0
    def minColour(self, n, m, matrix):
        # code here
        def dfs(i,s):
            vis[i]=1
            for j in d[i]:
                if(vis[j]==0):
                    dis[i]=dfs(j,s+1)
                else:
                    dis[i]=max(dis[j]+1,dis[i])
            return dis[i]+1
        d=defaultdict(list)
        for i in matrix:
            d[i[1]].append(i[0])
        ans=0
        dis=[0 for i in range(n+1)]
        vis=[0 for i in range(n+1)]
        for i in range(1,n+1):
            if(vis[i]==0):
                dfs(i,0)
        return max(dis)+1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = [int(x) for x in input().split()]
        mat = [[0]*2 for y in range(M)]
        for i in range(M):
            arr = input().split()
            mat[i][0] = int(arr[0])
            mat[i][1] = int(arr[1])
        
        ob = Solution()
        print(ob.minColour(N, M, mat))
# } Driver Code Ends