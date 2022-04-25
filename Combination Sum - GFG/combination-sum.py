#{ 
#Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


 # } Driver Code Ends
#User function Template for python3
from collections import Counter
class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,a,b):
        # code here
        def solve(i,temp,s):
            if(s==b):
                ans.append(sorted(temp.copy()))
                return
            if(i>=n or s>b):
                return
            for j in range(i,n):
                temp.append(a[j])
                solve(j,temp,s+a[j])
                temp.pop()
        ans=[]
        h=Counter([])
        temp=[]
        a=list(set(a))
        n=len(a)
        solve(0,temp,0)
        return sorted(ans)
#{ 
#Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

#} Driver Code Ends