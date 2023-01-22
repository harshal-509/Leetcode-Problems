class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def pal(s):
            if(s==s[::-1]):
                return 1
            else:
                return 0
        k=set()
        def fun(s,ans,temp):
            if(len(s)==0):
                if(str(temp)  not in k):
                    ans.append(temp.copy())
                    k.add(str(temp.copy()))
                return 
            for i in range(n):
                p=s[:i+1]
                q=s[i+1:]
                if(pal(p)):
                    temp.append(p)
                    fun(q,ans,temp)
                    temp.pop()
        ans=[]
        n=len(s)
        fun(s,ans,[])
        return ans