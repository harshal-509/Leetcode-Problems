class Solution:
    def largestPalindromic(self, num: str) -> str:
        num=list(map(int,num))
        z=Counter(num)
        ans=""
        ans1=""
        temp=""
        for i in range(10,-1,-1):
            if(i==0):
                if(ans==""):
                    break
            t=z[i]//2
            p=z[i]%2
            if(p and temp==""):
                temp=str(i)
            ans+=str(i)*t
            ans1=str(i)*t+ans1
        if(ans+temp+ans1==""):
            return "0"
        return (ans+temp+ans1)