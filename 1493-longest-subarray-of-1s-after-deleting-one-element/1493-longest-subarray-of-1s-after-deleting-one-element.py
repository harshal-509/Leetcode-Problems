class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        curr=0
        ans=0
        flag=0
        j=0
        while(i<n):
            if(nums[i]==1):
                curr+=1
                i+=1
            else:
                j=i+1
                p=0
                while(j<n):
                    if(nums[j]==1):
                        p+=1
                    else:
                        break
                    j+=1
                ans=max(ans,curr+p)  
                curr=p
                i=j
            ans=max(ans,curr)  
        ans=max(ans,curr)
        return min(ans,n-1)