#User function Template for python3
class Solution:
    def smallestNumber (self, S, D):
        # code here
        if(S>9*D):
            return -1
        ans=[9 for i in range(D)]
        s=9*D
        i=0
        while(s!=S and ans[i]!=1):
            s-=1
            ans[i]-=1
        i+=1
        while(s!=S and ans[i]!=0):
            s-=1
            ans[i]-=1
            if(ans[i]==0):
                i+=1
        ans1=""
        for i in ans:
            ans1+=str(i)
        return int(ans1)
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends