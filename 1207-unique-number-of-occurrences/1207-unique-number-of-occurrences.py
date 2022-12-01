class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=dict()
        for i in (arr):
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        s=set()
        for i in d:
            s.add(d[i])
        return len(s)==len(d)