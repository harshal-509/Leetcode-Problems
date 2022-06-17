class Solution:
    def isBipartite(self, n, adj):
        color = [-1 for _ in range(n)]
        for i in range(n):
            if color[i] == -1:
                if not self.dfscheck(i,color,adj):
                    return False
        return True
        
    def dfscheck(self,node,color,adj):
        if color[node] == -1:
            color[node] = 1
        for i in adj[node]:
            if color[i] == -1:
                color[i] = 1 - color[node]
    
                if not self.dfscheck(i,color,adj):
                    return False
    
            elif color[i] == color[node]:
                return False
        return True
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends