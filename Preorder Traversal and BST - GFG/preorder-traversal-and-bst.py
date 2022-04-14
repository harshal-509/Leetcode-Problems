#User function Template for python3

class Solution:
    def canRepresentBST(self, arr, N):
        # code here
        s=[]
        root=-float('inf')
        for i in arr:
            if(root>i):
                return 0
            while(s and s[-1]<i):
                root=s[-1]
                s.pop()
            s.append(i)
        return 1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.canRepresentBST(arr, N))
# } Driver Code Ends