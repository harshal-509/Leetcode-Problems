class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class DisjointSet: 
            def __init__(self, size): 
                self.parent = [i for i in range(size+1)] 
                self.rank = [0] * (size+1) 
                self.n = n
                
            def find(self, i): 
                if self.parent[i] != i: 
                    self.parent[i] = self.find(self.parent[i])  # Path compression 
                return self.parent[i] 

            def union_by_rank(self, i, j): 
                irep = self.find(i) 
                jrep = self.find(j) 
                if irep == jrep: 
                    return 0
                irank = self.rank[irep] 
                jrank = self.rank[jrep] 
                if irank < jrank: 
                    self.parent[irep] = jrep 
                elif jrank < irank: 
                    self.parent[jrep] = irep 
                else: 
                    self.parent[irep] = jrep 
                    self.rank[jrep] += 1
                self.n-=1
                return 1
            def isvalid(self):
                return self.n==1
        alice = DisjointSet(n)
        bob = DisjointSet(n)
        edges.sort(reverse=True)
        ans=0
        for i in edges:
            x=i[1]
            y=i[2]
            t=i[0]
            if(t==3):
                ans+=alice.union_by_rank(x,y)
                bob.union_by_rank(x,y)
            else:
                if(t==1):
                    ans+=alice.union_by_rank(x,y)
                else:
                    ans+=bob.union_by_rank(x,y)
        if(alice.isvalid() and bob.isvalid()):
            return len(edges)-ans
        return -1        