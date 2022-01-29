#User function Template for python3

class Solution:
    def romanToDecimal(self, s): 
        # code here
        n=len(s)
        h={"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        ans=h[s[0]]
        for i in range(1,n):
            if(h[s[i]]<=h[s[i-1]]):
                ans+=h[s[i]]
            else:
                ans+=h[s[i]]-2*h[s[i-1]]
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends