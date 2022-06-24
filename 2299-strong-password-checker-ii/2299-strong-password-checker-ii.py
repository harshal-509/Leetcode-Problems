class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if(len(password)<8):
            return 0
        a,b,c,d=0,0,0,0
        for i in password:
            if(ord(i)>=97 and ord(i)<=122):
                a=1
            elif(ord(i)>=65 and ord(i)<=90):
                b=1
            elif(i.isnumeric()):
                c=1
            elif(i in "!@#$%^&*()-+"):
                d=1
        if(a and b and c and d):
            n=len(password)
            for i in range(n-1):
                if(password[i]==password[i+1]):
                    return 0
            return 1
        return 0
        