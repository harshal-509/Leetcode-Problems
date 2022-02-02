#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        x=nums.count(0)
        if(n==1):
            return [1]
        p=[1 for i in range(n)]
        temp=nums[0]
        for i in range(1,n):
            p[i]=temp
            temp*=nums[i]
        temp=nums[n-1]
        for i in range(n-2,-1,-1):
            p[i]=p[i]*temp
            temp=temp*nums[i]
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