class Solution:
    def countAnagrams(self, s: str) -> int:
        def getdistinctcount(s):
            t=len(s)
            z=Counter(s)
            ans=factorial(t)
            for i in z:
                ans//=factorial(z[i])
            return ans
        ans=1
        s=s.split()
        for i in s:
            ans*=getdistinctcount(i)
        return ans%int(1e9+7)