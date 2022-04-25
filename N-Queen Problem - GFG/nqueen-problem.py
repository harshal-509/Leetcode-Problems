#User function Template for python3
import sys
sys.setrecursionlimit(1000000)
class Solution:
    def nQueen(self, n):
        # code here
        def valid(a,b):
            if(a<n and b<n and a>=0 and b>=0):
                for i in range(n):
                    if(q[i][b]==1):
                        return 0
                for i in range(n):
                    if(q[a][i]==1):
                        return 0
                x=a
                y=b
                while(x<n and y<n):
                    if(q[x][y]==1):
                        return 0
                    x+=1
                    y+=1
                x=a
                y=b
                while(x>=0 and y>=0):
                    if(q[x][y]==1):
                        return 0
                    x-=1
                    y-=1
                x=a
                y=b
                while(x>=0 and y<n):
                    if(q[x][y]==1):
                        return 0
                    x-=1
                    y+=1
                x=a
                y=b
                while(x<n and y>=0):
                    if(q[x][y]==1):
                        return 0
                    x+=1
                    y-=1
                return 1
            return 0
        def solve(q,i,temp):
            if(i==n):
                ans.append(temp.copy())
                return
            for j in range(n):
                if(valid(i,j)):
                    temp.append(j+1)
                    q[i][j]=1
                    solve(q,i+1,temp)
                    temp.pop()
                    q[i][j]=0
        ans=[]
        q=[[0 for i in range(n)] for i in range(n)]
        solve(q,0,[])
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends