#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        x=nums.count(0)
        p=[0 for i in range(n)]
        if(x==0):
            ans=1
            for i in range(n):
                ans=ans*nums[i]
            for i in range(n):
                p[i]=ans//nums[i]
        if(x==1):
            ans=1
            for i in range(n):
                if(nums[i]!=0):
                    ans=ans*nums[i]
            for i in range(n):
                if(nums[i]==0):
                    p[i]=ans
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