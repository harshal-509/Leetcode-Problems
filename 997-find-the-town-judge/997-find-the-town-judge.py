class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t=[0 for i in range(n+1)]
        q=[[0 for i in range(n+1)] for i in range(n+1)]
        for i in trust:
            t[i[0]]=1
            q[i[1]][i[0]]=1
        for i in range(1,n+1):
            if(t[i]==0):
                flag=1
                for j in range (1,n+1):
                    if(i!=j):
                        if(q[i][j]==0):
                            flag=0
                if(flag):
                    return i
        return -1
        