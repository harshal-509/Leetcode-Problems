class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x=""
        if(n==0):
            return 1
        while(n):
            if(n&1):
                x="0"+x
            else:
                x="1"+x
            n=n>>1
        return int(x,2)