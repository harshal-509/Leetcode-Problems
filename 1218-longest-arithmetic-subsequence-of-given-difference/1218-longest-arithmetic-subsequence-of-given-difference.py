class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans=1
        z=Counter([])
        n=len(arr)
        for i in range(n):
            x=arr[i]-difference
            if(x in z):
                z[arr[i]]=max(z[x]+1,z[arr[i]])
                ans=max(ans,z[arr[i]])
            else:
                z[arr[i]]=1
        return ans
            