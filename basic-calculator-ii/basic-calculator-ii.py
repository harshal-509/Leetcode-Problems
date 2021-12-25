class Solution:
    def calculate(self, s: str) -> int:
        a=[]
        n=len(s)
        b=[]
        y=""
        for i in range(n):
            if(s[i]=="+" or s[i]=="-" or s[i]=="*" or s[i]=="/"):
                b.append(int(y))
                b.append(s[i])
                y=""
            else:
                y+=s[i]
        if(y):
            b.append(int(y))
        n=len(b)
        for i in range(n):
            if(len(a)>=2):
                if(a[-2]=="*"):
                    x=int(a.pop())
                    a.pop()
                    y=int(a.pop())
                    a.append(x*y)
                elif(a[-2]=="/"):
                    x=int(a.pop())
                    a.pop()
                    y=int(a.pop())
                    a.append(y//x)
            a.append(b[i])
        if(len(a)>=2):
            if(a[-2]=="*"):
                x=int(a.pop())
                a.pop()
                y=int(a.pop())
                a.append(x*y)
            elif(a[-2]=="/"):
                x=int(a.pop())
                a.pop()
                y=int(a.pop())
                a.append(y//x)
        a=deque(a)
        while(len(a)>1):
            if(a[1]=="+"):
                x=int(a.popleft())
                a.popleft()
                y=int(a.popleft())
                a.appendleft(x+y)
            elif(a[1]=="-"):
                x=int(a.popleft())
                a.popleft()
                y=int(a.popleft())
                a.appendleft(x-y)
        return a[-1]