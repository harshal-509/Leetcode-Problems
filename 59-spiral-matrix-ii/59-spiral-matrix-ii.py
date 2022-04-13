class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0 for i in range(n)] for i in range(n)]
        j=1
        a,b,c,d=0,0,n-1,n-1
        while(j<=n*n):
            for i in range(b,d+1):
                ans[a][i]=j
                j+=1
            a+=1
            for i in range(a,c+1):
                ans[i][d]=j
                j+=1
            d-=1
            for i in range(d,b-1,-1):
                ans[c][i]=j
                j+=1
            c-=1
            for i in range(c,a-1,-1):
                ans[i][b]=j
                j+=1
            b+=1
        return ans