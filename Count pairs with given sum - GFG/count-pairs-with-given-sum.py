#User function Template for python3
from collections import *
class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        z=Counter(arr)
        ans=0
        for i in set(arr):
            if(k-i==i):
                ans+=z[i]*(z[i]-1)
            else:
                ans+=z[k-i]*z[i]
        return ans//2
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends