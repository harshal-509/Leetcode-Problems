#User function Template for python3

import bisect
class Solution:
    def median(self, matrix, r, c):
    	#code here
        def hs(m):
            ans=0
            for i in range(r):
                ans+=bisect.bisect_right(matrix[i],m)
            return ans
        min_=matrix[0][0]
        max_=0
        for i in range(r):
            min_=min(min_,matrix[i][0])
            max_=max(max_,matrix[i][c-1])
        i=min_
        j=max_
        ans=-1
        while(i<=j):
            m=i+(j-i)//2
            x=hs(m)
            if(x<(r*c+1)//2):
                i=m+1
            else:
                ans=m
                j=m-1
        return ans
          
    	  
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends