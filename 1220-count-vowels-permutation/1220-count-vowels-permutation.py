class Solution:
    def countVowelPermutation(self, n: int) -> int:
        def solve(i,temp):
            if(i==n):
                return 1
            if(temp and dp[i][z[temp[-1]]]!=-1):
                return dp[i][z[temp[-1]]]
            if(temp):
                a=0
                if(temp[-1]=="a"):
                    a+=solve(i+1,temp+"e")
                if(temp[-1]=="e"):
                    a+=solve(i+1,temp+"a")
                    a+=solve(i+1,temp+"i")
                if(temp[-1]=="i"):
                    a+=solve(i+1,temp+"a")
                    a+=solve(i+1,temp+"e")
                    a+=solve(i+1,temp+"o")
                    a+=solve(i+1,temp+"u")
                if(temp[-1]=="o"):
                    a+=solve(i+1,temp+"u")
                    a+=solve(i+1,temp+"i")
                if(temp[-1]=="u"):
                    a+=solve(i+1,temp+"a")
                dp[i][z[temp[-1]]]=a
                return a
            else:
                a=0
                a+=solve(i+1,temp+"a")
                a+=solve(i+1,temp+"e")
                a+=solve(i+1,temp+"i")
                a+=solve(i+1,temp+"o")
                a+=solve(i+1,temp+"u")
                dp[i][0]=a
                return a
        z={'a':1,'e':2,'i':3,'o':4,'u':5}
        dp=[[-1 for i in range(6)] for j in range(n+1)]
        mod=int(1e9+7)
        return solve(0,"")%mod