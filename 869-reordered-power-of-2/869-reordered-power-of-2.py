class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(31):
            z=Counter(str(2**i))
            p=Counter(str(n))
            if(len(p)==len(z)):
                t=0
                for i in p:
                    if(p[i]==z[i]):
                        t+=1
                if(t==len(p)):
                    return 1
        return 0