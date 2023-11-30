class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        arr=list(bin(n)[2:])
        flag=1
        ans=0
        n=len(arr)
        for i in range(n):
            if(arr[i]=="1"):
                if(flag):
                    ans+=pow(2,n-i)-1
                else:
                    ans-=pow(2,n-i)-1
                flag^=1
        return ans