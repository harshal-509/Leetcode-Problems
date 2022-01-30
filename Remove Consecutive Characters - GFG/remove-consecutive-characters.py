#User function Template for python3
import sys
sys.setrecursionlimit(1000000)
class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        def hs(s,i):
            if(i==len(s)-1):
                return s
            if(s[i]==s[i+1]):
                return hs(s[:i+1]+s[i+2:],i)
            else:
                return hs(s,i+1)
        return hs(S,0)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends