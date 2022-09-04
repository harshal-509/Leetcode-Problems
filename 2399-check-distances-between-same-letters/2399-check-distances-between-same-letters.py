class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        z=Counter(s)
        n=len(s)
        for i in z:
            a=-1
            b=-1
            for j in range(n):
                if(s[j]==i):
                    if(a==-1):
                        a=j
                    else:
                        b=j
            if(b-a-1==distance[ord(i)-97]):
                pass
            else:
                return 0
        return 1