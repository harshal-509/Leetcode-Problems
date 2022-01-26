class Solution:
    def countAndSay(self, n: int) -> str:
        x=["1","11"]
        for i in range(n-2):
            y=[]
            t=1
            l=x[-1][0]
            for i in range(1,len(x[-1])):
                if(x[-1][i]==x[-1][i-1]):
                    t+=1
                else:
                    y.append(str(t))
                    y.append(l)
                    l=x[-1][i]
                    t=1
            y.append(str(t))
            y.append(l)
            x.append("".join(y))
        if(n==1):
            return x[0]
        return x[-1]