class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def check(s):
            p=[]
            for i in s:
                if(i==")"):
                    if(p and p[-1]=="("):
                        p.pop()
                    else:
                        return 0
                else:
                    p.append(i)
            return not(p)
        def solve(i,temp):
            if(i==2*n):
                if(check(temp)):
                    ans.append(temp)
                return
            solve(i+1,temp+"(")
            solve(i+1,temp+")")
        ans=[]
        solve(0,"")
        return ans