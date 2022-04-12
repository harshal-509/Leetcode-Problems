class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(i,j):
            if(i<n and i>=0 and j<m and j>=0 and board[i][j]==1):
                return 1
            return 0
        def check(i,j):
            c=0
            if(valid(i+1,j)):
                c+=1
            if(valid(i-1,j)):
                c+=1
            if(valid(i,j-1)):
                c+=1
            if(valid(i,j+1)):
                c+=1
            if(valid(i-1,j-1)):
                c+=1
            if(valid(i-1,j+1)):
                c+=1
            if(valid(i+1,j-1)):
                c+=1
            if(valid(i+1,j+1)):
                c+=1
            return c
        n=len(board)
        m=len(board[0])
        ans=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                x=check(i,j)
                if(board[i][j]==1):
                    if(x<2 or x>3):
                        ans[i][j]=0
                    else:
                        ans[i][j]=1
                else:
                    if(x==3):
                        ans[i][j]=1
        for i in range(n):
            for j in range(m):
                board[i][j]=ans[i][j]