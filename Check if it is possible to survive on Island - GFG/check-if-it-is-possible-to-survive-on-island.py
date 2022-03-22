#User function Template for python3
import math
class Solution:
    def minimumDays(self, S, N, M):
        # code here
        if(N<M):
            return -1
        mindays=0
        currfood=0
        day=1
        while(day<=S):
            if(currfood<M):
                if(day%7==0):
                    if(mindays==day-1):
                        return -1
                mindays+=1
                currfood+=N
            currfood-=M
            day+=1
        return mindays
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, M = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.minimumDays(S, N, M))
# } Driver Code Ends