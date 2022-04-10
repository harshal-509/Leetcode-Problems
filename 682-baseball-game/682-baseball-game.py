class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s=[]
        n=len(ops)
        for i in range(n):
            if(ops[i]=="+"):
                x=s[-2]
                y=s[-1]
                s.append(x+y)
            elif(ops[i]=="D"):
                x=s[-1]
                s.append(x*2)
            elif(ops[i]=="C"):
                s.pop()
            else:
                s.append(int(ops[i]))
        return sum(s)