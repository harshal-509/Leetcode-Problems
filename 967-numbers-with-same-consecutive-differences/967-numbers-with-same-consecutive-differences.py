class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def solve(i,temp):
            if(i==n):
                x="".join(temp)
                ans.append(x)
                return
            for j in range(10):
                if(abs(int(temp[-1])-j)==k):
                    temp.append(str(j))
                    solve(i+1,temp)
                    temp.pop()
        ans=[]
        for i in range(1,10):
            temp=[str(i)]
            solve(1,temp)
        return ans