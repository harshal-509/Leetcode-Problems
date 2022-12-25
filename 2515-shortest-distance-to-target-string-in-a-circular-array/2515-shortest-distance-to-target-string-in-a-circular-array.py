class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans=0
        if(target not in words):
            return -1
        i=startIndex
        t=0
        n=len(words)
        t=0
        while(1):
            if(words[i]==target):
                break    
            t+=1
            i+=1
            if(i==n):
                i=0
        i=startIndex
        t1=0
        while(1):
            if(words[i]==target):
                break    
            t1+=1
            i-=1
            if(i==-1):
                i=n-1
        return min(t,t1)