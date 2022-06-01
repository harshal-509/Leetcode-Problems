#User function Template for python3
from collections import deque
class Solution:
	def ShortestDistance(self, matrix):
		# Code here
		def safe(i,j):
		    if(i<n and j<n and i>=0 and j>=0 and vis[i][j]==0):
		        return 1
		    return 0
        def solve(i,j,vis):
            if(safe(i,j)==0):
                return 0
            vis[i][j]=1
            if(i==n-1 and j==n-1):
                return 1
            for k in range(1,matrix[i][j]+1):
                if(solve(i,j+k,vis)):
                    return 1
                if(solve(i+k,j,vis)):
                    return 1
            vis[i][j]=0
            return 0
        n=len(matrix)
        vis=[[0 for i in range(n)] for i in range(n)]
        if(solve(0,0,vis)):
            return vis
        return [[-1]]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix= []
		for i in range(n):
			a = list(map(int, input().split()))
			matrix.append(a)
		ob = Solution()
		ans = ob.ShortestDistance(matrix)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends