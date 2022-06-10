#User function Template for python3

class Solution:
    def maxCoins(self, A, B, T, N):
        # code here 
        z=[[A[i],B[i]] for i in range(N)]
        z=sorted(z,key=lambda x:x[1],reverse=True)
        ans=0
        for i in range(N):
            if(z[i][0]<=T):
                T-=z[i][0]
                ans+=z[i][0]*z[i][1]
            else:
                ans+=T*z[i][1]
                break
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        T,N=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxCoins(A,B,T,N))
# } Driver Code Ends