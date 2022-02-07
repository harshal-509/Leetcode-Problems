class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        z=Counter(s)
        z1=Counter(t)
        for i in z1:
            if(z1[i]>z[i]):
                return i