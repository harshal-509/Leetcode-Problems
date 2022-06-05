class Solution:
    def __init__(self):
        self.ans=0
    def totalNQueens(self, n: int) -> int:
        def valid(i,j,temp):
            x=i
            y=j
            while(x>=0 and y>=0 and x<n and y<n):
                if(temp[x][y]=="Q"):
                    return 0
                y-=1
            x=i
            y=j
            while(x>=0 and y>=0 and x<n and y<n):
                if(temp[x][y]=="Q"):
                    return 0
                x-=1
                y-=1
            x=i
            y=j
            while(x>=0 and y>=0 and x<n and y<n):
                if(temp[x][y]=="Q"):
                    return 0
                x+=1
                y-=1
            return 1
        def solve(i,temp):
            if(i==n):
                self.ans+=1
                return 
            for j in range(n):
                if(valid(j,i,temp)):
                    temp[j][i]="Q"
                    solve(i+1,temp)
                    temp[j][i]="."
        temp=[['.' for i in range(n)] for i in range(n)]
        solve(0,temp)
        return self.ans