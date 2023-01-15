class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        flag=0
        flag1=0
        if(length>=10000 or width>=10000 or height>=10000 or length*width*height>=1000000000):
            flag=1
        if(mass>=100):
            flag1=1
        if(flag and flag1):
            return "Both"
        if(flag and not(flag1)):
            return "Bulky"
        if(not(flag) and flag1):
            return "Heavy"
        if(not(flag) and not(flag1)):
            return "Neither"