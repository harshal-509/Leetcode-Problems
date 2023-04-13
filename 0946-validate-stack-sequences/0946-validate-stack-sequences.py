class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s=[]
        i=0
        j=0
        n=len(pushed)
        while(i<n and j<n):
            if(s and s[-1]==popped[j]):
                s.pop()
                j+=1
            else:
                s.append(pushed[i])
                i+=1
        while(j<n):
            if(s and s[-1]==popped[j]):
                s.pop()
            j+=1
        if(s):
            return 0
        return 1