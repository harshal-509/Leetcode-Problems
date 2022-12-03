class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1,n+1):
            a=0
            for j in range(1,i+1):
                a+=j
            b=0
            for j in range(i,n+1):
                b+=j
            if(a==b):
                return i
        return -1