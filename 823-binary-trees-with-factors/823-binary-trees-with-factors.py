class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        z=Counter([])
        arr.sort()
        n=len(arr)
        ans=0
        for i in range(n):
            x=arr[i]
            t=1
            p=int(math.sqrt(x))+1
            for j in range(i):
                if(x%arr[j]==0):
                    if(z[x//arr[j]]):
                        t+=z[arr[j]]*z[x//arr[j]]
            z[x]=t
            ans+=t
        return ans%int(1e9+7)