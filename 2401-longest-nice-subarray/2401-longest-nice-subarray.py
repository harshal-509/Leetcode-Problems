class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def add(x):
            i=31
            while(x):
                if(x&1):
                    arr[i]+=1
                x=x>>1
                i-=1
        def remove(x):
            i=31
            while(x):
                if(x&1):
                    arr[i]-=1
                x=x>>1
                i-=1
        def check(arr):
            for i in range(32):
                if(arr[i]>1):
                    return 1
            return 0
        i=0
        ans=1
        j=0
        n=len(nums)
        arr=[0 for i in range(32)]
        while(j<n):
            add(nums[j])
            x=check(arr)
            if(x):
                while(i<j and check(arr)):
                    remove(nums[i])
                    i+=1
            ans=max(ans,j-i+1)
            j+=1
        ans=max(ans,j-i)
        return ans