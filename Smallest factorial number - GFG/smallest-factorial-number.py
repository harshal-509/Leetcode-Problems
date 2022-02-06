#User function Template for python3

class Solution:
    def findNum(self, n : int):
        # Complete this function
        def hs(m):
            ans1=0
            i=5
            while(i<=m):
                ans1+=m//i
                i=i*5
            return ans1
        i=0
        j=100000
        ans=-1
        while(i<=j):
            m=i+(j-i)//2
            x=hs(m)
            if(x>=n):
                ans=m
                j=m-1
            elif(x<n):
                i=m+1
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends