class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans=0
        m={'0':'0','1':'1','2':'5','3':-1,'4':-1,'5':'2','6':'9','7':-1,'8':'8','9':'6'}
        def check(i):
            t=""
            for j in str(i):
                if(m[j]!=-1):
                    t+=m[j]
                else:
                    return 0
            return t and int(t)!=i
        for i in range(1,n+1):
            if(check(i)):
                ans+=1
        return ans