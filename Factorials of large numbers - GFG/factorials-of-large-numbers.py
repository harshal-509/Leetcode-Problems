#User function Template for python3

class Solution:
    def factorial(self, N):
        #code here
        ans=1
        for i in range(2,N+1):
            ans*=i
        return str(ans).split()
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends