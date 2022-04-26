class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(i,temp,t):
            if(t==k):
                sol.append(temp.copy())
                return
            if(i>=n):
                return
            temp.append(ans[i])
            solve(i+1,temp,t+1)
            temp.pop()
            solve(i+1,temp,t)
        ans=[i for i in range(1,n+1)]
        sol=[]
        solve(0,[],0)
        return sol