class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        j=x-1
        if(x==1):
            return 1
        while(i<=j):
            m=i+(j-i)//2
            if(m*m<=x):
                i=m+1
            else:
                j=m-1
        return i-1
