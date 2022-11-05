class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.isWord = 1
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # def solve1(word):
        #     def solve(c,i,j):
        #         if(c==s):
        #             return 1
        #         if(i>=0 and i<n and j>=0 and j<m and vis[i][j]==0):
        #             if(board[i][j]!=word[c]):
        #                 return 0
        #             vis[i][j]=1
        #             if(solve(c+1,i+1,j)):
        #                 return 1
        #             if(solve(c+1,i-1,j)):
        #                 return 1
        #             if(solve(c+1,i,j+1)):
        #                 return 1
        #             if(solve(c+1,i,j-1)):
        #                 return 1
        #             vis[i][j]=0
        #     s=len(word)    
        #     n=len(board)
        #     m=len(board[0])
        #     vis=[[0 for i in range(m)] for j in range(n)]
        #     for i in range(n):
        #         for j in range(m):
        #             if(board[i][j]==word[0]):
        #                 if(solve(0,i,j)):
        #                     return 1
        #     return 0
        # ans=[]
        # for i in words:
        #     if(solve1(i)):
        #         ans.append(i)
        # return ans
        def solve(i,j,temp,curr):
            if(self.count==0):
                return
            if(curr.isWord):
                ans.append(temp)
                curr.isWord=False
                self.count-=1
            if(i<0 or j<0 or i>=n or j>=m or board[i][j]==0):
                return
            q=board[i][j]
            if(q not in curr.children):
                return
            board[i][j]=0
            solve(i+1,j,temp+q,curr.children[q])
            solve(i,j+1,temp+q,curr.children[q])
            solve(i,j-1,temp+q,curr.children[q])
            solve(i-1,j,temp+q,curr.children[q])
            board[i][j]=q
        n=len(board)
        m=len(board[0])
        curr=Trie()
        for i in words:
            curr.insert(i)
        ans=[]
        self.count=len(words)
        for i in range(n):
            for j in range(m):
                solve(i,j,"",curr.root)
        return ans