class Solution:
    def numTilings(self, n: int) -> int:
        mod=1000000007
        arr=[1 for i in range(n+1)]
        arr[1]=1
        if(n==1):
            return arr[n]
        arr[2]=2
        for i in range(3,n+1):
            arr[i]=((2*(arr[i-1])%mod)%mod+(arr[i-3])%mod)%mod
        return arr[n]