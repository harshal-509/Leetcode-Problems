#User function Template for python3

class Solution:
    def isPossible(self, s, n, x, a):
        # code here
        ans=[s]
        for i in range(n):
            ans.append(a[i])
        index=n
        for i in range(1,n+1):
            ans[i]+=s
            s+=ans[i]
            if(s>x):
                index=i
                break
        i=index
        while(i>=0):
            if(ans[i]<=x):
                x-=ans[i]
            if(x==0):
                return 1
            i-=1
        return x==0
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, X = [int(y) for y in input().split()]
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        if ob.isPossible(S, N, X, A) == 1:
            print("yes")
        else:
            print("no")
# } Driver Code Ends