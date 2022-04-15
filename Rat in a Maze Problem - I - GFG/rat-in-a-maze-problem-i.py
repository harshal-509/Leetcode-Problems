#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        def valid(i,j):
            if(i>=0 and i<n and j>=0 and j<n and vis[i][j]!=2 and m[i][j]!=0):
                return 1
            return 0
        def solve(i,j,temp):
            if(i==n-1 and j==n-1 and m[i][j]==1):
                ans.append("".join(temp.copy()))
                return
            vis[i][j]=2
            if(valid(i+1,j)):
                temp.append("D")
                solve(i+1,j,temp)
                temp.pop()
            if(valid(i-1,j)):
                temp.append("U")
                solve(i-1,j,temp)
                temp.pop()
            if(valid(i,j-1)):
                temp.append("L")
                solve(i,j-1,temp)
                temp.pop()
            if(valid(i,j+1)):
                temp.append("R")
                solve(i,j+1,temp)
                temp.pop()
            vis[i][j]=0
        ans=[]
        vis=[[0 for i in range(n)] for j in range(n)]
        if(m[0][0]==0):
            return []
        solve(0,0,[])
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends