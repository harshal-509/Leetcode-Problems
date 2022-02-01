#User function Template for python3

class Solution:
    def countSquares(self, N):
        # code here 
        i=0
        j=N
        while(i<=j):
            m=i+(j-i)//2
            if(m*m<=N):
                ans=m
                i=m+1
            else:
                j=m-1
        if(ans*ans==N):
            return ans-1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends