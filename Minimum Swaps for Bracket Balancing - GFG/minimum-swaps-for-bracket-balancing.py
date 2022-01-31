#User function Template for python3
class Solution:
    def minimumNumberOfSwaps(self,s):
        # code here
        ans,a,b,t=0,0,0,0
        n=len(s)
        for i in range(n):
            if(s[i]=="["):
                a+=1
                ans+=max(t,0)
            else:
                b+=1
            t=b-a
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        ob = Solution()
        print(ob.minimumNumberOfSwaps(S))
# } Driver Code Ends