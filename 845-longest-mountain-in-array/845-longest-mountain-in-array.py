class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans=0
        j=0
        n=len(arr)
        t=0
        k=0
        while(j<n-1):
            while(j<n-1 and arr[j]>=arr[j+1]):
                j+=1
            while(j<n-1 and arr[j]<arr[j+1]):
                j+=1
                t+=1
            while(j<n-1 and arr[j]>arr[j+1]):
                j+=1
                k+=1
            if(t and k):
                ans=max(ans,t+k+1)
            t=0
            k=0
        return ans