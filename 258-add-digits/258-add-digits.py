class Solution:
    def addDigits(self, num: int) -> int:
        num=list(map(int,str(num)))
        while(len(num)>1):
            num=list(map(int,str(sum(num))))
        return num[0]