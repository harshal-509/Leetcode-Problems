class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(i,s,temp,ans,n):
            s.add(i)
            if(i==n-1):
                ans.append([0]+temp.copy())
                return 
            for j in graph[i]:
                if(j not in s):
                    temp.append(j)
                    dfs(j,s,temp,ans,n)
                    x=temp.pop()
                    s.remove(x)
        ans=[]
        n=len(graph)
        dfs(0,set(),[],ans,n)
        return ans