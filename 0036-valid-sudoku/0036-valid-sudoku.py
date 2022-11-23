class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            h=[0 for i in range(10)]
            for j in i:
                if(j!="."):
                    if(h[int(j)]==1):
                        return 0
                    h[int(j)]=1
        for j in range(9):
            h=[0 for i in range(10)]
            for i in range(9):
                if(board[i][j]!="."):
                    if(h[int(board[i][j])]==1):
                        return 0
                    h[int(board[i][j])]=1
        k=0
        while(k<=6):
            m=0
            while(m<=6):
                h=[0 for i in range(10)]
                for i in range(k,3+k):
                    for j in range(m,3+m):
                        if(board[i][j]!="."):
                            if(h[int(board[i][j])]==1):
                                return 0
                            h[int(board[i][j])]=1
                m+=3
            k+=3
        return 1