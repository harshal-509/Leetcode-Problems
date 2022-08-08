class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(c,i,j):
            if(c==s):
                return 1
            if(i>=0 and i<n and j>=0 and j<m and vis[i][j]==0):
                if(board[i][j]!=word[c]):
                    return 0
                vis[i][j]=1
                if(solve(c+1,i+1,j)):
                    return 1
                if(solve(c+1,i-1,j)):
                    return 1
                if(solve(c+1,i,j+1)):
                    return 1
                if(solve(c+1,i,j-1)):
                    return 1
                vis[i][j]=0
        s=len(word)    
        n=len(board)
        m=len(board[0])
        vis=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if(board[i][j]==word[0]):
                    if(solve(0,i,j)):
                        return 1
        return 0