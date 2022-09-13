class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.par=Counter([])
        self.up=[[-1 for i in range(32)] for j in range(n)]  
        for i in range(n):
            self.up[i][0]=parent[i]
        for i in range(n):
            for j in range(1,32):
                if(self.up[i][j-1]!=-1):
                    self.up[i][j]=self.up[self.up[i][j-1]][j-1]
    def getKthAncestor(self, node: int, k: int) -> int:
        curr=node
        t=bin(k)[2:]
        m=len(t)-1
        j=0
        while(curr):
            if(t[j]=='1'):
                k-=pow(2,m)
                curr=self.up[curr][m]
                if(curr==-1):
                    return curr
                if(k==0 and curr!=-1):
                    return curr
            m-=1
            j+=1
        return -1
# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)