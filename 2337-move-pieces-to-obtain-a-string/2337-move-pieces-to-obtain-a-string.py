class Solution:
    def canChange(self, start: str, target: str) -> bool:
        a=start.count('L')
        b=start.count('R')
        c=target.count('L')
        d=target.count('R')
        if(a!=c or b!=d):
            return False
        a1=[]
        a2=[]
        b1=[]
        b2=[]
        n=len(start)
        for i in range(n):
            if(start[i]=="L"):
                a1.append(i)
            elif(start[i]=="R"):
                a2.append(i)
        for i in range(n):
            if(target[i]=="L"):
                b1.append(i)
            elif(target[i]=="R"):
                b2.append(i)
        for i in range(len(a1)):
            if(a1[i]<b1[i]):
                return False
        for i in range(len(b2)):
            if(a2[i]>b2[i]):
                return False
        i=0
        j=0
        while(i<n and j<n):
            if(start[i]=="_"):
                i+=1
            elif(target[j]=="_"):
                j+=1
            else:
                if(start[i]!=target[j]):
                    return False
                i+=1
                j+=1
        return True