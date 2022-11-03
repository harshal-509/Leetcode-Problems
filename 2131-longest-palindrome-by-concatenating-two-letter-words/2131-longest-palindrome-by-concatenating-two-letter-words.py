class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        h=Counter(words)
        ans=0
        flag=0
        for i in h:
            if(i[0]!=i[1]):
                if(h[i] and h[i[::-1]]):
                    x=min(h[i],h[i[::-1]])
                    h[i]=0
                    h[i[::-1]]=0
                    ans+=x*4
        t=0
        x=""
        for i in h:
            if(h[i] and i[0]==i[1] and h[i]&1):
                if(t<h[i]):
                    t=h[i]
                    x=i
        if(x):
            h[x]=0
        ans+=t*2
        for i in h:
            if(h[i] and i[0]==i[1]):
                if(h[i]&1):
                    h[i]-=1
                ans+=h[i]*2
        return ans