class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        arr= [0 for i in range(n)]
        for i in range(n):
            arr[i]=abs(ord(s[i])-ord(t[i]))
        i=0
        j=0
        t=0
        ans=0
        while(i<n and j<n):
            t+=arr[j] 
            j+=1
            if(t>maxCost):
                while(i<j and t>maxCost):
                    t-=arr[i]
                    i+=1
            ans=max(ans,j-i)
        return ans