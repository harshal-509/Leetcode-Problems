
#Back-end complete function Template for Python 3

class Solution:
    def transform(self, A, B): 
        #code here.
        n=len(A)
        m=len(B)
        if(n!=m):
            return -1
        a=sorted(A)
        b=sorted(B)
        for i in range(n):
            if(a[i]!=b[i]):
                return -1
        i=n-1
        j=n-1
        ans=0
        while(i>=0 and j>=0):
            if(A[i]!=B[j]):
                while(i>=0 and A[i]!=B[j]):
                    ans+=1
                    i-=1
            else:
                i-=1
                j-=1
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        ob = Solution()
        print(ob.transform(A,B))
# } Driver Code Ends