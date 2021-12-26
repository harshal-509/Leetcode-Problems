class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        c=""
        for i in b:
            c+=str(i)
        c=int(c)
        mod=1337
        ans=1
        while(c):
            if(c&1):
                ans=((ans)%mod*(a)%mod)%mod
            a=((a)%mod*(a)%mod)%mod
            c=c>>1
        return ans%mod