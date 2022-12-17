import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        for i in range(len(tokens)):
            if(tokens[i]=="+"): 
                x=a[-2]+a[-1]
                a.pop()
                a.pop()
                a.append(x)
            elif(tokens[i]=="-"): 
                x=a[-2]-a[-1]
                a.pop()
                a.pop()
                a.append(x)
            elif(tokens[i]=="*"): 
                x=a[-2]*a[-1]
                a.pop()
                a.pop()
                a.append(x)
            elif(tokens[i]=="/"):
                x=int(truediv(a[-2],(a[-1])))
                a.pop()
                a.pop()
                a.append(x)
            else:
                a.append(int(tokens[i]))
        return a[-1]