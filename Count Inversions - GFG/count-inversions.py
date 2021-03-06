
class Solution:
    def inversionCount(self, arr, n):
        # Your Code Here
        def ps(arr,temp,l,m,r):
            i=l
            j=m
            k=l
            ans=0
            while(i<m and j<=r):
                if(arr[i]<=arr[j]):
                    temp[k]=arr[i]
                    i+=1
                    k+=1
                else:
                    ans+=m-i
                    temp[k]=arr[j]
                    j+=1
                    k+=1
            while(i<m):
                temp[k]=arr[i]
                i+=1
                k+=1
            while(j<=r):
                temp[k]=arr[j]
                j+=1
                k+=1
            for t in range(l,r+1):
                arr[t]=temp[t]
            return ans
        def hs(arr,temp,i,j):
            ans=0
            if(i<j):
                m=i+(j-i)//2
                ans+=hs(arr,temp,i,m)
                ans+=hs(arr,temp,m+1,j)
                ans+=ps(arr,temp,i,m+1,j)
            return ans
        temp=[0 for i in range(n)]
        return hs(arr,temp,0,n-1)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends