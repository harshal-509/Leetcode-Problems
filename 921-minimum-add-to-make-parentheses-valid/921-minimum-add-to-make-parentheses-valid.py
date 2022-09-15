class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        s1=[]
        for i in s:
            if(i=="("):
                s1.append(i)
            else:
                if(s1 and s1[-1]=="("):
                    s1.pop()
                else:
                    s1.append(i)
        return len(s1)