class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag=1
        if(dividend<0 or divisor<0):
            flag=0
            if(dividend<0 and divisor<0):
                flag=1
        dividend=abs(dividend)
        divisor=abs(divisor)
        t=divisor
        ans=0
        m=1
        while(dividend>=t):
            if(divisor>dividend):
                m=1
                divisor=t
            ans+=m
            dividend-=divisor
            m+=m
            divisor+=divisor
        if(flag):
            return min(ans,pow(2,31)-1)
        return -ans