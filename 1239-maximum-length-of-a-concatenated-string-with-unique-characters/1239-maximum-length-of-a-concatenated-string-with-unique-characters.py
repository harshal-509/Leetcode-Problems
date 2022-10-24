class Solution:
    def __init__(self):
        self.ans=0
    def maxLength(self, arr: List[str]) -> int:
        def solve(i,t,z):
            if(i>=n):
                self.ans=max(self.ans,t)
                return 
            flag=0
            for j in arr[i]:
                if(z[j]):
                    flag=1
                z[j]+=1
            for j in arr[i]:
                z[j]-=1
            if(flag==0):
                for j in arr[i]:
                    z[j]+=1
                solve(i+1,t+len(arr[i]),z)
                for j in arr[i]:
                    z[j]-=1
            solve(i+1,t,z)
        n=len(arr)
        z=Counter([])
        solve(0,0,z)
        return self.ans