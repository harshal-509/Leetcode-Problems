class Solution:
    def calculate(self, s: str) -> int:
        def solve(tokens):
            a=[]
            for i in range(len(tokens)):
                if(tokens[i]=="+"): 
                    x=a[-2]+a[-1]
                    a.pop()
                    a.pop()
                    a.append(x)
                elif(tokens[i]=="-"):
                    if(len(a)==1):
                        a[-1]=-a[-1]
                    else:
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
        def InfixtoPostfix(exp):
            stack = []
            result = []
            precedence = dict(zip(list('(+-*/^'), [1, 2, 2, 3, 3, 4]))
            for char in exp:
                if char in precedence.keys() or char == ')':
                    if len(stack) == 0:
                        stack.append(char)
                    else:
                        if char == '(':
                            stack.append(char)
                        elif char == '^' and stack[-1] == '^':
                            stack.append(char)
                        elif char == ')':
                            out_char = stack.pop()
                            while out_char != '(':
                                result.append(out_char)
                                out_char = stack.pop()
                        elif precedence.get(char) == precedence.get(stack[-1]):
                            result.append(stack.pop())
                            stack.append(char)
                        elif precedence.get(char) > precedence.get(stack[-1]):
                            stack.append(char)
                        elif precedence.get(char) < precedence.get(stack[-1]):
                            while precedence.get(stack[-1]) >= precedence.get(char):
                                out_char = stack.pop()
                                result.append(out_char)
                                if len(stack) == 0:
                                    break
                            stack.append(char)
                else:
                    result.append(char)
            while len(stack) !=0:
                result.append(stack.pop())
            return result
        ans=[]
        temp=""
        s1=s
        s=""
        if(len(s1)<=1000):
            return eval(s1)
        for i in s1:
           if(i!=" "):
            s+=i
        n=len(s)
        i=0
        while(i<n):
            try:
                if(s[i]=='-' and temp=="" and ans and ans[-1]!=")"):
                    temp+=s[i]
                else:
                    x=int(s[i])
                    temp+=s[i]
            except:
                if(temp):
                    ans.append(temp)
                ans.append(s[i])
                temp=""
            i+=1
        if(temp):
            ans.append(temp)
        return solve(InfixtoPostfix(ans))