#User function Template for python3

class Solution:
    def allPalindromicPerms(self, s):
        # code here 
        def solve(i,temp):
            if(i==n):
                ans.append(temp.copy())
                return
            x=""
            for j in range(i,n):
                x+=s[j]
                if(x==x[::-1]):
                    temp.append(x)
                    solve(j+1,temp)
                    temp.pop()
        ans=[]
        n=len(s)
        solve(0,[])
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
# } Driver Code Ends