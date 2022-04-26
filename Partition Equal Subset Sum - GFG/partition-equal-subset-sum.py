# User function Template for Python3

class Solution:
    def equalPartition(self,n,arr):
        # code here
        def sub(i,s,p):
            if(p==s):
                return 1
            if(i>=n or p>s):
                return 0
            return sub(i+1,s,p+arr[i]) or sub(i+1,s,p)
        arr.sort()
        s=sum(arr)
        if(s%2):
            return 0
        s=s//2
        ans=0
        return sub(0,s,0)
#{ 
#  Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends