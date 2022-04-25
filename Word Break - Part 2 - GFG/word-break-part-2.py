#User function Template for python3
from collections import Counter
class Solution:
    def wordBreak(self, n, dict, s):
        # code here
        def solve(i,temp):
            if(i==n):
                ans.append(temp.copy())
            x=""
            for j in range(i,n):
                x+=s[j]
                if(h[x]):
                    temp.append(x)
                    solve(j+1,temp)
                    temp.pop()
        h=Counter([])
        ans=[]
        n=len(s)
        for i in dict:
            h[i]=1
        solve(0,[])
        for i in range(len(ans)):
            ans[i]=" ".join(ans[i])
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dict = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dict, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends