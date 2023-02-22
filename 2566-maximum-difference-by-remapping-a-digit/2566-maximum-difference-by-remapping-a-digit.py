class Solution:
    def minMaxDifference(self, num: int) -> int:
        m=""
        n=""
        p=9
        z=Counter([])
        flag=0
        for i in str(num):
            if(flag):
                if(z[i]):
                    m+=z[i]
                else:
                    m+=i
            else:
                if(p>int(i)):
                    m+=str(p)
                    z[i]=str(p)
                    flag=1
                else:
                    m+=str(p)
        p=0
        z=Counter([])
        flag=0
        for i in str(num):
            if(flag):
                if(z[i]):
                    n+=z[i]
                else:
                    n+=i
            else:
                if(p<int(i)):
                    n+=str(p)
                    z[i]=str(p)
                    flag=1
                else:
                    n+=str(p)
        return int(m)-int(n)