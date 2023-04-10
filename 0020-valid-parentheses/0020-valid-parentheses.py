class Solution:
    def isValid(self, s: str) -> bool:
        m=[]
        for i in s:
            if(i=="(" or i=="{" or i=="["):
                m.append(i)
            elif(i==")" and (len(m)==0 or m[-1]!="(")):
                return 0
            elif(i=="}" and (len(m)==0 or m[-1]!="{")):
                return 0
            elif(i=="]" and (len(m)==0 or m[-1]!="[")):
                return 0
            else:
                m.pop()
        if(len(m)!=0):
            return 0
        return 1