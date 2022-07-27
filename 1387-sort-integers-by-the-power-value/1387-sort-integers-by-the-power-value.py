class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def solve(n):
            if(n==1):
                return 0
            if(n%2==0):
                ans=solve(n//2)+1
            else:
                ans=solve(3*n+1)+1
            return ans
        arr=[]
        for i in range(lo,hi+1):
            arr.append((solve(i),i))
        arr.sort()
        return arr[k-1][1]