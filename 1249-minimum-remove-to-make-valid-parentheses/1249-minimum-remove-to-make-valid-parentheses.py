class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        false=[]
        for i in range(0,len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                if len(stack)==0:
                    false.append(i)
                else:
                    stack.pop(-1)
        str=""
        for i in range(0,len(s)):
            if i not in stack and i not in false:
                str+=s[i]
        return str