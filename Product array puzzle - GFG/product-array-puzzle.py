#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        x=nums.count(0)
        if(n==1):
            return [1]
        p=[0 for i in range(n)]
        a1=[1 for i in range(n)]
        a2=[1 for i in range(n)]
        a1[0]=nums[0]
        a2[n-1]=nums[n-1]
        for i in range(1,n):
            a1[i]=nums[i]*a1[i-1]
        for i in range(n-2,-1,-1):
            a2[i]=nums[i]*a2[i+1]
        p[n-1]=a1[n-2]
        p[0]=a2[1]
        for i in range(1,n-1):
            p[i]=a1[i-1]*a2[i+1]
        return p
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends