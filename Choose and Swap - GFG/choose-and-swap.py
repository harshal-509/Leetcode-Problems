#User function Template for python3


class Solution:
    def chooseandswap (self, s):
        # code here
        x=s[0]
        n=len(s)
        y="ab"
        h=[-1 for i in range(26)]
        for i in range(n):
            if(h[ord(s[i])-97]==-1):
                h[ord(s[i])-97]=i
        for i in range(n):
            x=s[i]
            for j in range(26):
                if(x>(chr(j+97)) and i<h[j]):
                    y=chr(j+97)
                    break
            if(y!="ab"):
                break
        if(y=="ab"):
            return s
        ans=""
        for i in range(n):
            if(s[i]==x):
                ans+=y
            elif(s[i]==y):
                ans+=x
            else:
                ans+=s[i]
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)


# } Driver Code Ends