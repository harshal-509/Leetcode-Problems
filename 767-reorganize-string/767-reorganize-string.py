class Solution:
    def reorganizeString(self, s: str) -> str:
        h=[0 for i in range(26)]
        h1=[0 for i in range(26)]
        for i in s:
            h[ord(i)-97]+=1
            h1[ord(i)-97]+=1
        h.sort()
        for i in range(1,25):
            h[i]+=h[i-1]
        if(h[-2]>=h[-1]-1):
            temp=[[-1,""] for i in range(26)]
            for i in range(26):
                temp[i][0]=h1[i]
                temp[i][1]=chr(i+97)
            temp.sort()
            ans=["" for i in range(len(s))]
            i=25
            j=len(s)-1
            a=0
            while(i>=0):
                while(temp[i][0]):
                    a+=1
                    ans[j]=temp[i][1]
                    temp[i][0]-=1
                    j-=2
                    if(j<0):
                        j=len(s)-2
                if(not(temp[i][0])):
                    i-=1
            return "".join(ans)
        return ""