#User function Template for python3
from bisect import bisect_left as lb
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		ans=-1
		o=m-1
		j=m-1
        for i in range(n):
            while(j>=0 and arr[i][j]==1):
                j-=1
            if(j<o):
                o=j
                ans=i
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends