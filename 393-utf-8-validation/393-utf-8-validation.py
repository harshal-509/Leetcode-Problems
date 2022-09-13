class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n=len(data)
        for i in range(n):
            x=bin(data[i])[2:]
            data[i]=(8-len(x))*"0"+x
        i=0
        l=data.copy()
        while(i<n):
            x=l[i]
            t=0
            for j in x:
                if(j=='1'):
                    t+=1
                else:
                    break
            if(t==0):
                i+=1  
            elif(t==2):
                if(i+1<n):
                    if(l[i+1][0]=='1' and l[i+1][1]=='0'):
                        pass
                    else:
                        return 0
                else:
                    return 0
                i+=2
            elif(t==3):
                if(i+1<n and i+2<n):
                    if(l[i+1][0]=='1' and l[i+1][1]=='0' and l[i+2][0]=='1' and l[i+2][1]=='0'):
                        pass
                    else:
                        return 0
                else:
                    return 0
                i+=3
            elif(t==4):
                if(i+1<n and i+2<n and i+3<n):
                    if(l[i+1][0]=='1' and l[i+1][1]=='0' and l[i+2][0]=='1' and l[i+2][1]=='0'  and l[i+3][0]=='1' and l[i+3][1]=='0'):
                        pass
                    else:
                        return 0
                else:
                    return 0
                i+=4
            else:
                return 0
        return 1