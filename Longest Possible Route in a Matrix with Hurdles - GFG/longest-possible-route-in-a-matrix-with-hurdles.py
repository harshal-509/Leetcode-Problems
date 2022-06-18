class Solution:
    def __init__(self):
        self.ans=-1
    def longestPath(self,mat,n : int, m : int, xs : int, ys : int, xd : int, yd : int) -> int:
        # code here
        def valid(i,j):
            if(i>=0 and i<n and j<m and j>=0 and vis[i][j]==0 and mat[i][j]==1):
                return 1
            return 0
        def dfs(i,j,s):
            if(valid(i,j)):
                if(i==xd and j==yd):
                    self.ans=max(self.ans,s)
                vis[i][j]=1
                dfs(i,j+1,s+1)
                dfs(i,j-1,s+1)
                dfs(i+1,j,s+1)
                dfs(i-1,j,s+1)
                vis[i][j]=0
        vis=[[0 for i in range(m)] for j in range(n)]
        dfs(xs,ys,0)
        return self.ans

#{ 
#  Driver Code Starts


class IntArray:

    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        b=IntArray().Input(4)
        
        
        mat=IntMatrix().Input(a[0], a[0])
        
        obj = Solution()
        res = obj.longestPath(mat,a[0],a[1],b[0],b[1],b[2],b[3])
        
        print(res)
        


# } Driver Code Ends