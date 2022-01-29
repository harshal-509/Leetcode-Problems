#User function Template for python3
class Solution:
    def minFlips(self, s):
        # Code here
        ans=0
        ans1=0
        n=len(s)
        x="0"
        y="1"
        for i in range(n):
            if(i%2==0):
                if(s[i]==x):
                    ans+=1
                else:
                    ans1+=1
            else:
                if(s[i]==x):
                    ans1+=1
                else:
                    ans+=1
        return min(ans,ans1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends