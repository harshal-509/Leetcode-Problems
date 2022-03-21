class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def check(h,h1):
            for i in range(26):
                if(h[i] and h1[i]):
                    return 0
            return 1
        ans=[]
        i=0
        t=1
        n=len(s)
        while(i<n):
            h=[0 for p in range(26)]
            h1=[0 for p in range(26)]
            j=0
            k=i+1
            while(j<=i):
                h[ord(s[j])-97]+=1
                j+=1
            while(k<n):
                h1[ord(s[k])-97]+=1
                k+=1
            #print(h,h1)
            if(check(h,h1)):
                ans.append(t)
                t=1
            else:
                t+=1
            i+=1
        return ans