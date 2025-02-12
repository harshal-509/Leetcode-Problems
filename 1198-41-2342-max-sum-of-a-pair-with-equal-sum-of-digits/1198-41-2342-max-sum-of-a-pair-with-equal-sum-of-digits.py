class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        z=defaultdict(list)
        for j in nums:
            t = list(str(j))
            for i in range(len(t)):
                t[i]=int(t[i])
            t=sum(t)
            z[t].append(j)
        ans=-1
        for i in z:
            z[i].sort(reverse=True)
            if(len(z[i])>=2):
                ans=max(ans,z[i][0]+z[i][1])
        return ans