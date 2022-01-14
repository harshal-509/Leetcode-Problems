import sys
class Solution:
    def myAtoi(self, s: str) -> int:
        ans=""
        flag=0
        p=0
        for i in range(len(s)):
            if(s[i].isnumeric() or s[i]=="+" or s[i]=="-" or s[i]==" "):
                if(s[i]=="+" and flag==0):
                    flag=1
                elif(s[i]=="-" and flag==0):
                    ans+="-"
                    flag=1
                elif(s[i]=="-" and flag):
                    break
                elif(s[i]=="+" and flag):
                    break
                elif(s[i]==" " and flag):
                    break
                elif(s[i]==" "):
                    pass
                else:
                    ans+=s[i]
                    flag=1
            else:
                break
        if(ans==""):
            return 0
        try:
            ans=int(ans)
        except:
            return 0
        if(ans<0):
            return max(int(ans),-pow(2,31)) 
        return min(int(ans),pow(2,31)-1)