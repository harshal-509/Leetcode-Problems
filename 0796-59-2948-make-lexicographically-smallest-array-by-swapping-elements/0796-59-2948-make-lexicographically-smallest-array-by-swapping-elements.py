class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        d = []
        n = len(nums)
        p=[]
        for i in range(n):
            p.append([nums[i],i])
        v = sorted(p)
        t=[v[0]]
        for i in range(1,n):
            if(v[i][0]-v[i-1][0]<=limit):
                t.append(v[i])
            else:
                d.append(t)
                t=[v[i]]
        d.append(t)
        ans = [0 for i in range(n)]
        for i in d:
            l=[]
            m=[]
            for j in i:
                l.append(j[1])
                m.append(j[0])
            l.sort()
            for j in range(len(l)):
                ans[l[j]]=m[j]
        return ans