class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g=0
        p=0
        m=0
        for i in garbage:
            g+=i.count("G")
            p+=i.count("P")
            m+=i.count("M")
        ans=0
        a=garbage[0].count("G")
        b=garbage[0].count("P")
        c=garbage[0].count("M")
        ans+=a+b+c
        g-=a
        p-=b
        m-=c
        j=0
        for i in garbage[1:]:
            if(g):
                ans+=travel[j]
            if(p):
                ans+=travel[j]
            if(m):
                ans+=travel[j]
            a=i.count("G")
            b=i.count("P")
            c=i.count("M")
            ans+=a+b+c
            g-=a
            p-=b
            m-=c
            j+=1
        return ans